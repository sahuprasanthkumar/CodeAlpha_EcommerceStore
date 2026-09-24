// CodeAlpha E-Commerce Store - Client-Side Interactions

document.addEventListener('DOMContentLoaded', () => {
    // Quantity increment and decrement handlers
    document.querySelectorAll('.btn-quantity-minus').forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.closest('.input-group').querySelector('input[type="number"]');
            let val = parseInt(input.value) || 1;
            if (val > 1) {
                input.value = val - 1;
                // If inside a cart form, auto submit
                const form = input.closest('form.cart-update-form');
                if (form) form.submit();
            }
        });
    });

    document.querySelectorAll('.btn-quantity-plus').forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.closest('.input-group').querySelector('input[type="number"]');
            let max = parseInt(input.getAttribute('max')) || 999;
            let val = parseInt(input.value) || 1;
            if (val < max) {
                input.value = val + 1;
                // If inside a cart form, auto submit
                const form = input.closest('form.cart-update-form');
                if (form) form.submit();
            } else {
                showToast(`Maximum stock limit of ${max} reached!`, 'warning');
            }
        });
    });

    // Auto-dismiss alerts after 4 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 4000);
    });

    // AJAX Add to Cart for instant responsiveness
    document.querySelectorAll('.ajax-add-to-cart').forEach(form => {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Adding...';

            const formData = new FormData(this);
            const url = this.getAttribute('action');

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    // Update cart count badge in navbar
                    const badge = document.getElementById('cart-badge');
                    if (badge) {
                        badge.textContent = data.cart_count;
                        badge.classList.remove('d-none');
                        // Animate badge
                        badge.style.transform = 'scale(1.3)';
                        setTimeout(() => badge.style.transform = 'scale(1)', 200);
                    }
                    showToast(data.message || 'Product added to cart!', 'success');
                } else {
                    this.submit(); // fallback to standard POST
                }
            } catch (err) {
                console.warn('AJAX cart add fallback', err);
                this.submit();
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        });
    });
});

// Toast notification helper
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const bgClass = type === 'success' ? 'text-bg-success' : type === 'warning' ? 'text-bg-warning' : 'text-bg-primary';
    const toastEl = document.createElement('div');
    toastEl.className = `toast align-items-center ${bgClass} border-0 shadow`;
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');
    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body fw-semibold">
                <i class="bi bi-check-circle-fill me-2"></i> ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;

    container.appendChild(toastEl);
    const toast = new bootstrap.Toast(toastEl, { delay: 3500 });
    toast.show();
    toastEl.addEventListener('hidden.bs.toast', () => toastEl.remove());
}
