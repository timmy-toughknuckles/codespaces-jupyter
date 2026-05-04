import ast
import math
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

ALLOWED_NAMES = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'inf': math.inf,
    'nan': math.nan,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'sinh': math.sinh,
    'cosh': math.cosh,
    'tanh': math.tanh,
    'asinh': math.asinh,
    'acosh': math.acosh,
    'atanh': math.atanh,
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'log2': math.log2,
    'exp': math.exp,
    'degrees': math.degrees,
    'radians': math.radians,
    'abs': abs,
    'round': round,
    'floor': math.floor,
    'ceil': math.ceil,
    'factorial': math.factorial,
}

CHEEKY_BANNER = '''
Welcome to the Cheeky Calculator!
No nonsense, just numbers, angles, and occasional sass.
Type expressions like `sin(pi/2)`, `log10(100)`, or `factorial(5)`.
Type `quit`, `exit`, or `q` if you want to abandon the adventure.
'''

ERROR_RESPONSES = [
    "Oopsie daisy. That one didn't compute.",
    "Math says no. Try something else.",
    "You broke it. Nice job."
]


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError('I only understand numbers.')

    if isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
        raise ValueError('That operator is out of bounds.')

    if isinstance(node, ast.UnaryOp):
        operand = safe_eval(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError('Nope, not doing that one.')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError('Fancy calls are banned.')
        func_name = node.func.id
        if func_name not in ALLOWED_NAMES or not callable(ALLOWED_NAMES[func_name]):
            raise ValueError(f'{func_name} is not on the VIP list.')
        func = ALLOWED_NAMES[func_name]
        args = [safe_eval(arg) for arg in node.args]
        kwargs = {kw.arg: safe_eval(kw.value) for kw in node.keywords}
        return func(*args, **kwargs)

    if isinstance(node, ast.Name):
        if node.id in ALLOWED_NAMES:
            value = ALLOWED_NAMES[node.id]
            if callable(value):
                raise ValueError(f'Use {node.id}() with parentheses, genius.')
            return value
        raise ValueError(f'{node.id} is not allowed in this party.')

    raise ValueError('I refused to evaluate that strange thing.')


def evaluate_expression(expression):
    if not expression.strip():
        raise ValueError('Empty expression? Really?')
    parsed = ast.parse(expression, mode='eval')
    return safe_eval(parsed)


def main():
    print(CHEEKY_BANNER)
    while True:
        try:
            line = input('cheeky-calc> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nFine. Walk away. Bye.')
            break

        if not line:
            print('Say something. Numbers count.')
            continue

        if line.lower() in {'exit', 'quit', 'q'}:
            print('You escaped. Until next time.')
            break

        try:
            result = evaluate_expression(line)
            print(f'Result: {result}')
        except Exception as exc:
            print(f'Error: {exc}')
            print(ERROR_RESPONSES[hash(line) % len(ERROR_RESPONSES)])


if __name__ == '__main__':
    main()
