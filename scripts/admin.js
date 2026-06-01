const ORDER_STORAGE_KEY = "fidget-orbit-orders";
const ADMIN_PASSWORD = "orbit-admin";

const form = document.querySelector("[data-admin-form]");
const status = document.querySelector("[data-admin-status]");
const ordersRoot = document.querySelector("[data-admin-orders]");

function getOrders() {
  return JSON.parse(window.localStorage.getItem(ORDER_STORAGE_KEY) ?? "[]");
}

function renderOrders() {
  const orders = getOrders();

  if (orders.length === 0) {
    ordersRoot.innerHTML = `
      <p class="eyebrow">Saved orders</p>
      <h2 class="admin-title">No orders yet</h2>
      <p class="admin-empty">This browser has not saved any orders yet.</p>
    `;
    return;
  }

  ordersRoot.innerHTML = `
    <p class="eyebrow">Saved orders</p>
    <h2 class="admin-title">All browser orders</h2>
    <ul class="admin-list">
      ${orders
        .map(
          (order) => `
            <li class="admin-order">
              <h3>#${order.id} ${order.productName}</h3>
              <p><strong>Customer:</strong> ${order.customerName}</p>
              <p><strong>Product ID:</strong> ${order.productId}</p>
              <p><strong>Price:</strong> $${order.price}</p>
              <p class="admin-order-meta">${new Date(
                order.orderDate
              ).toLocaleString()}</p>
            </li>
          `
        )
        .join("")}
    </ul>
  `;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const password = String(formData.get("password") ?? "");

  if (password !== ADMIN_PASSWORD) {
    status.textContent = "Wrong password.";
    ordersRoot.hidden = true;
    return;
  }

  status.textContent = "Login successful.";
  ordersRoot.hidden = false;
  renderOrders();
  form.reset();
});
