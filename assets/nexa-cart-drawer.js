(function() {
  window.NexaCart = {
    open: function() {
      // Trigger Dawn's cart drawer or redirect to cart
      const cartDrawer = document.querySelector('cart-drawer');
      if (cartDrawer && typeof cartDrawer.open === 'function') {
        cartDrawer.open();
      } else {
        document.documentElement.dispatchEvent(new CustomEvent('cart:open'));
        const activeDrawer = document.querySelector('.drawer[is="cart-drawer"]');
        if (activeDrawer) {
          activeDrawer.classList.add('active');
          document.body.classList.add('overflow-hidden');
        } else {
          // fallback
          window.location.href = '/cart';
        }
      }
    },
    refresh: function() {
      // Trigger cart refresh
      document.documentElement.dispatchEvent(new CustomEvent('cart:updated'));
      const cartDrawer = document.querySelector('cart-drawer');
      if (cartDrawer && cartDrawer.classList.contains('is-empty')) {
        // Force reload if empty state is stuck
        fetch('/cart.js')
          .then(res => res.json())
          .then(cart => {
            if (cart.item_count > 0) window.location.reload();
          });
      }
    }
  };

  function addToCart(items) {
    return fetch(window.Shopify.routes.root + 'cart/add.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/javascript'
      },
      body: JSON.stringify({ items: items })
    })
    .then(response => {
      if (!response.ok) throw new Error('Error adding to cart');
      return response.json();
    })
    .then(data => {
      window.NexaCart.refresh();
      window.NexaCart.open();
      return data;
    })
    .catch(error => {
      console.error('NexaCart Error:', error);
      alert('Could not add to cart. Please try again.');
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    // Quick Add Single Item
    document.querySelectorAll('.js-quick-add').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        const variantId = this.getAttribute('data-id');
        if (!variantId) return;
        
        const originalText = this.innerText;
        this.innerText = 'Adding...';
        this.disabled = true;

        addToCart([{ id: variantId, quantity: 1 }]).finally(() => {
          this.innerText = originalText;
          this.disabled = false;
        });
      });
    });

    // Add Bundle (2 items)
    document.querySelectorAll('.js-add-bundle').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        const item1 = this.getAttribute('data-item1');
        const item2 = this.getAttribute('data-item2');
        if (!item1 || !item2) return;

        const originalText = this.innerText;
        this.innerText = 'Bundling...';
        this.disabled = true;

        addToCart([
          { id: item1, quantity: 1 },
          { id: item2, quantity: 1 }
        ]).finally(() => {
          this.innerText = originalText;
          this.disabled = false;
        });
      });
    });
  });
})();