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

HELP_TEXT = '''
Scientific Calculator
Commands:
  help      Show this help text
  exit      Quit the calculator
  quit      Quit the calculator

Supported operators:
  +  -  *  /  **  %  //

Supported functions:
  sin(x), cos(x), tan(x)
  asin(x), acos(x), atan(x)
  sinh(x), cosh(x), tanh(x)
  sqrt(x), log(x), log10(x), log2(x), exp(x)
  degrees(x), radians(x)
  abs(x), round(x), floor(x), ceil(x), factorial(x)

Constants:
  pi, e, tau, inf, nan

Examples:
  sin(pi / 2)
  log(100, 10)
  sqrt(2) ** 2
  factorial(5)
'''


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)

    if isinstance(node, ast.Num):
        return node.n

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError('Invalid constant type')

    if isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
        raise ValueError(f'Unsupported operator: {op_type.__name__}')

    if isinstance(node, ast.UnaryOp):
        operand = safe_eval(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError(f'Unsupported unary operator: {op_type.__name__}')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError('Only named functions are allowed')
        func_name = node.func.id
        if func_name not in ALLOWED_NAMES or not callable(ALLOWED_NAMES[func_name]):
            raise ValueError(f'Function {func_name} is not allowed')
        func = ALLOWED_NAMES[func_name]
        args = [safe_eval(arg) for arg in node.args]
        kwargs = {kw.arg: safe_eval(kw.value) for kw in node.keywords}
        return func(*args, **kwargs)

    if isinstance(node, ast.Name):
        if node.id in ALLOWED_NAMES:
            value = ALLOWED_NAMES[node.id]
            if callable(value):
                raise ValueError(f'Function {node.id} requires parentheses')
            return value
        raise ValueError(f'Name {node.id} is not allowed')

    raise ValueError(f'Unsupported expression: {type(node).__name__}')


def evaluate_expression(expression):
    expression = expression.strip()
    if not expression:
        raise ValueError('Empty expression')
    parsed = ast.parse(expression, mode='eval')
    return safe_eval(parsed)


def main():
    print(HELP_TEXT)
    while True:
        try:
            text = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break

        if not text:
            continue
        if text.lower() in {'help', 'h'}:
            print(HELP_TEXT)
            continue
        if text.lower() in {'exit', 'quit', 'q'}:
            print('Goodbye!')
            break

        try:
            result = evaluate_expression(text)
            print(result)
        except Exception as exc:
            print(f'Error: {exc}')


if __name__ == '__main__':
    main()
