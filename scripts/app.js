import { loadProducts } from "./data.js";

const productGrid = document.querySelector("#product-grid");

function getGradientClass(name) {
  return `theme-${name}`;
}

function renderProductCard(product) {
  return `
    <article class="product-card ${getGradientClass(product.gradient)}">
      <p class="product-meta">${product.category} · ${product.quietLevel}</p>
      <h3>${product.name}</h3>
      <p class="product-tagline">${product.tagline}</p>
      <p class="product-price">$${product.price}</p>
      <ul class="chip-list" aria-label="${product.name} quick details">
        <li>${product.ageRange}</li>
        <li>${product.colors.length} colors</li>
        <li>${product.features[0]}</li>
      </ul>
      <a class="button button-secondary" href="./product.html?id=${product.id}">
        View details
      </a>
    </article>
  `;
}

async function initHomePage() {
  try {
    const products = await loadProducts();
    productGrid.innerHTML = products.map(renderProductCard).join("");
  } catch (error) {
    productGrid.innerHTML = `
      <p class="status-card" role="alert">
        We could not load the catalog right now. Try refreshing the page.
      </p>
    `;
    console.error(error);
  } finally {
    productGrid.removeAttribute("aria-busy");
  }
}

initHomePage();
