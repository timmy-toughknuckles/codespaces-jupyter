const DATA_URL = "./data/products.json";

export async function loadProducts() {
  const response = await fetch(DATA_URL);

  if (!response.ok) {
    throw new Error(`Failed to load products: ${response.status}`);
  }

  return response.json();
}

export async function loadProductById(productId) {
  const products = await loadProducts();
  return products.find((product) => product.id === productId) ?? null;
}
