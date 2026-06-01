import { loadProductById } from "./data.js";

const detailRoot = document.querySelector("#product-detail");
const params = new URLSearchParams(window.location.search);
const productId = params.get("id");

function clearBusyState() {
  detailRoot.removeAttribute("aria-busy");
}

function renderMissingState() {
  detailRoot.innerHTML = `
    <section class="status-card">
      <p class="eyebrow">Catalog note</p>
      <h1>We could not find that toy.</h1>
      <p class="hero-copy">Return to the catalog and choose another fidget.</p>
      <a class="button button-primary" href="./index.html#catalog">Back to shop</a>
    </section>
  `;
  clearBusyState();
}

const ORDER_STORAGE_KEY = "fidget-orbit-orders";

function placeOrder(order) {
  const existingOrders = JSON.parse(
    window.localStorage.getItem(ORDER_STORAGE_KEY) ?? "[]"
  );
  const savedOrder = {
    id: existingOrders.length + 1,
    ...order,
  };

  existingOrders.push(savedOrder);
  window.localStorage.setItem(
    ORDER_STORAGE_KEY,
    JSON.stringify(existingOrders, null, 2)
  );

  return savedOrder;
}

function getSavedOrders() {
  return JSON.parse(window.localStorage.getItem(ORDER_STORAGE_KEY) ?? "[]");
}

function renderSavedOrders(product) {
  const savedOrders = getSavedOrders().filter(
    (order) => order.productId === product.id
  );

  if (savedOrders.length === 0) {
    return `
      <p class="saved-orders-empty">
        No saved orders for ${product.name} yet.
      </p>
    `;
  }

  return `
    <ul class="saved-orders-list">
      ${savedOrders
        .map(
          (order) => `
            <li class="saved-orders-item">
              <strong>#${order.id}</strong> ${order.customerName}
              <span>${new Date(order.orderDate).toLocaleString()}</span>
            </li>
          `
        )
        .join("")}
    </ul>
  `;
}

function attachOrderForm(product) {
  const toggleButton = detailRoot.querySelector("[data-order-toggle]");
  const fetchButton = detailRoot.querySelector("[data-order-fetch]");
  const orderForm = detailRoot.querySelector("[data-order-form]");
  const nameInput = detailRoot.querySelector("[data-order-name]");
  const status = detailRoot.querySelector("[data-order-status]");
  const savedOrdersPanel = detailRoot.querySelector("[data-saved-orders]");

  if (
    !toggleButton ||
    !fetchButton ||
    !orderForm ||
    !nameInput ||
    !status ||
    !savedOrdersPanel
  ) {
    return;
  }

  toggleButton.addEventListener("click", () => {
    orderForm.hidden = false;
    toggleButton.hidden = true;
    nameInput.focus();
  });

  fetchButton.addEventListener("click", () => {
    savedOrdersPanel.hidden = false;
    savedOrdersPanel.innerHTML = renderSavedOrders(product);
  });

  orderForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const customerName = nameInput.value.trim();
    const submitButton = orderForm.querySelector('button[type="submit"]');

    if (!customerName) {
      status.textContent = "Please enter your name first.";
      return;
    }

    const order = {
      orderDate: new Date().toISOString(),
      customerName,
      productId: product.id,
      productName: product.name,
      price: product.price,
    };

    try {
      submitButton.disabled = true;
      status.textContent = "Placing order...";
      const savedOrder = placeOrder(order);
      status.textContent = `Placed order #${savedOrder.id} for ${customerName}. Saved in this browser.`;
      savedOrdersPanel.hidden = false;
      savedOrdersPanel.innerHTML = renderSavedOrders(product);
      orderForm.reset();
    } catch (error) {
      console.error(error);
      status.textContent = "Could not place the order right now.";
    } finally {
      submitButton.disabled = false;
    }
  });
}

function renderProduct(product) {
  detailRoot.innerHTML = `
    <section class="detail-hero theme-${product.gradient}">
      <div class="detail-visual">
        <div class="detail-image-frame">
          <img
            class="detail-image"
            src="${product.image}"
            alt="${product.imageAlt}"
          />
        </div>
      </div>
      <div class="detail-copy">
        <p class="eyebrow">${product.category} · ${product.quietLevel}</p>
        <h1>${product.name}</h1>
        <p class="hero-copy">${product.description}</p>
        <div class="detail-actions">
          <span class="price-badge">$${product.price}</span>
          <button class="button button-secondary" type="button" data-order-toggle>
            Order now
          </button>
          <button class="button button-ghost" type="button" data-order-fetch>
            View saved orders
          </button>
          <a class="button button-primary" href="./index.html#catalog">Keep shopping</a>
        </div>
        <form class="order-form" data-order-form hidden>
          <label class="order-label" for="customer-name">Enter your name</label>
          <div class="order-row">
            <input
              class="order-input"
              id="customer-name"
              name="customerName"
              type="text"
              placeholder="Your name"
              data-order-name
              required
            />
            <button class="button button-primary" type="submit">
              Place
            </button>
          </div>
          <p class="order-status" data-order-status aria-live="polite"></p>
        </form>
        <section class="saved-orders-panel" data-saved-orders hidden></section>
      </div>
      <aside class="detail-panel">
        <div class="hero-panel-icon">
          <img src="./assets/icons/cart.svg" alt="" />
        </div>
        <h2>Quick facts</h2>
        <ul class="detail-list">
          <li><strong>Age:</strong> ${product.ageRange}</li>
          <li><strong>Colors:</strong> ${product.colors.join(", ")}</li>
          <li><strong>Feel:</strong> ${product.tagline}</li>
        </ul>
      </aside>
    </section>
    <section class="detail-body">
      <article class="detail-section">
        <h2>Why students like it</h2>
        <ul class="feature-list">
          ${product.features.map((feature) => `<li>${feature}</li>`).join("")}
        </ul>
      </article>
    </section>
  `;
  attachOrderForm(product);
  clearBusyState();
}

async function initProductPage() {
  if (!productId) {
    renderMissingState();
    return;
  }

  try {
    const product = await loadProductById(productId);

    if (!product) {
      renderMissingState();
      return;
    }

    document.title = `${product.name} | Fidget Orbit`;
    renderProduct(product);
  } catch (error) {
    console.error(error);
    renderMissingState();
  }
}

initProductPage();
