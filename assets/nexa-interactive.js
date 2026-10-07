/**
 * Nexa Precision Workstation - Interactive Client Engine
 * Handles Setup Wizard, Compatibility Logic, Blueprints, Port Tooltips, and Modals.
 */

(function () {
  'use strict';

  // --- Global Nexa Namespace ---
  window.NexaEngine = {
    state: {
      profile: null,
      dock: null,
      monitor: null,
      accessories: [],
      currentStep: 1,
      totalSteps: 4
    },

    // --- Device Profiles Spec Matrix ---
    deviceProfiles: {
      P1: {
        code: 'P1',
        label: 'Studio 65',
        os: 'macOS',
        connector: 'Thunderbolt 4 / USB-C',
        minPower: 65,
        video: 'Dual 4K / Single 5K'
      },
      P2: {
        code: 'P2',
        label: 'Studio 100',
        os: 'macOS',
        connector: 'Thunderbolt 4 / USB-C',
        minPower: 100,
        video: 'Dual 6K / Triple 4K'
      },
      P3: {
        code: 'P3',
        label: 'Creator 65',
        os: 'Windows / Linux',
        connector: 'USB-C DP Alt Mode',
        minPower: 65,
        video: 'Dual 4K MST'
      },
      P4: {
        code: 'P4',
        label: 'Classic A',
        os: 'Universal',
        connector: 'USB-A / Legacy USB-C',
        minPower: 0,
        video: 'DisplayLink Dual 1080p'
      }
    },

    init: function () {
      this.initHeaderMorph();
      this.initPortDiagrams();
      this.initStickyBuyBar();
      this.initSetupWizard();
      this.initModalTriggers();
    },

    // 1. Morphing Glass Header
    initHeaderMorph: function () {
      const header = document.querySelector('.nexa-header');
      if (!header) return;

      window.addEventListener('scroll', function () {
        if (window.scrollY > 40) {
          header.classList.add('scrolled', 'header-morphed');
        } else {
          header.classList.remove('scrolled', 'header-morphed');
        }
      }, { passive: true });
    },

    // 2. Interactive Port Tooltips & Pins
    initPortDiagrams: function () {
      const pins = document.querySelectorAll('.port-pin, .port-slot');
      pins.forEach(pin => {
        pin.addEventListener('mouseenter', function (e) {
          const spec = this.getAttribute('data-port-spec');
          const title = this.getAttribute('data-port-title') || 'Port Specification';
          if (!spec) return;

          let tooltip = document.getElementById('nexa-port-tooltip');
          if (!tooltip) {
            tooltip = document.createElement('div');
            tooltip.id = 'nexa-port-tooltip';
            tooltip.className = 'nexa-glass nexa-tooltip';
            tooltip.style.position = 'fixed';
            tooltip.style.zIndex = '9999';
            tooltip.style.pointerEvents = 'none';
            tooltip.style.padding = '8px 12px';
            tooltip.style.borderRadius = '8px';
            tooltip.style.fontSize = '12px';
            tooltip.style.color = '#f8fafc';
            tooltip.style.border = '1px solid rgba(59, 130, 246, 0.4)';
            tooltip.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.8)';
            document.body.appendChild(tooltip);
          }

          tooltip.innerHTML = `<div style="font-weight:600; color:#38bdf8; margin-bottom:2px;">${title}</div><div>${spec}</div>`;
          tooltip.style.display = 'block';

          const rect = this.getBoundingClientRect();
          tooltip.style.left = `${rect.left + window.scrollX - 20}px`;
          tooltip.style.top = `${rect.top - 45}px`;
        });

        pin.addEventListener('mouseleave', function () {
          const tooltip = document.getElementById('nexa-port-tooltip');
          if (tooltip) tooltip.style.display = 'none';
        });
      });
    },

    // 3. Floating Sticky Buy Bar for PDP
    initStickyBuyBar: function () {
      const stickyBar = document.querySelector('.nexa-sticky-bar');
      const buyBtn = document.querySelector('.product-form__submit, [name="add"]');
      if (!stickyBar || !buyBtn) return;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (!entry.isIntersecting && entry.boundingClientRect.top < 0) {
            stickyBar.classList.add('visible');
          } else {
            stickyBar.classList.remove('visible');
          }
        });
      }, { threshold: 0.1 });

      observer.observe(buyBtn);
    },

    // 4. Setup Wizard & Compatibility Engine
    initSetupWizard: function () {
      const wizardContainer = document.querySelector('.nexa-wizard-container');
      if (!wizardContainer) return;

      const self = this;

      // Profile Selectors
      const profileCards = wizardContainer.querySelectorAll('.profile-card');
      profileCards.forEach(card => {
        card.addEventListener('click', function () {
          profileCards.forEach(c => c.classList.remove('active'));
          this.classList.add('active');
          const code = this.getAttribute('data-profile-code');
          self.state.profile = self.deviceProfiles[code] || null;
          self.validateDockSelection();
          self.updateBlueprint();
        });
      });

      // Wizard Nav Buttons
      const nextBtn = wizardContainer.querySelector('.wizard-next-btn');
      const prevBtn = wizardContainer.querySelector('.wizard-prev-btn');

      if (nextBtn) {
        nextBtn.addEventListener('click', function () {
          if (self.state.currentStep < self.state.totalSteps) {
            self.setWizardStep(self.state.currentStep + 1);
          }
        });
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', function () {
          if (self.state.currentStep > 1) {
            self.setWizardStep(self.state.currentStep - 1);
          }
        });
      }
    },

    setWizardStep: function (step) {
      this.state.currentStep = step;
      document.querySelectorAll('.wizard-step-pane').forEach(pane => {
        pane.classList.remove('active');
        if (parseInt(pane.getAttribute('data-step')) === step) {
          pane.classList.add('active');
        }
      });

      document.querySelectorAll('.wizard-progress-dot').forEach((dot, idx) => {
        if (idx + 1 <= step) dot.classList.add('active');
        else dot.classList.remove('active');
      });

      this.updateBlueprint();
    },

    validateDockSelection: function () {
      if (!this.state.profile) return;
      const dockCards = document.querySelectorAll('.wizard-dock-card');

      dockCards.forEach(card => {
        const dockPower = parseInt(card.getAttribute('data-dock-power') || '0', 10);
        const reqPower = this.state.profile.minPower;

        if (dockPower < reqPower) {
          card.classList.add('incompatible');
          card.setAttribute('data-incompatible-reason', `Insufficient charging power (${dockPower}W vs ${reqPower}W required)`);
        } else {
          card.classList.remove('incompatible');
          card.removeAttribute('data-incompatible-reason');
        }
      });
    },

    updateBlueprint: function () {
      const blueprintSvg = document.getElementById('workstation-blueprint-svg');
      if (!blueprintSvg) return;

      const profile = this.state.profile;
      const laptopNode = document.getElementById('blueprint-laptop-node');
      const cablePath = document.getElementById('blueprint-cable-path');

      if (profile && laptopNode) {
        laptopNode.classList.add('node-active');
        laptopNode.querySelector('.node-label')?.setTextContent?.(profile.label);
      }

      if (cablePath && profile) {
        cablePath.classList.add('flowing');
      }
    },

    // 5. Accessible Modal System
    initModalTriggers: function () {
      document.querySelectorAll('[data-nexa-modal-open]').forEach(btn => {
        btn.addEventListener('click', function () {
          const targetId = this.getAttribute('data-nexa-modal-open');
          const modal = document.getElementById(targetId);
          if (modal) {
            modal.classList.add('modal-open');
            document.body.style.overflow = 'hidden';
          }
        });
      });

      document.querySelectorAll('[data-nexa-modal-close], .nexa-modal-backdrop').forEach(el => {
        el.addEventListener('click', function (e) {
          if (e.target === this) {
            const modal = this.closest('.nexa-modal');
            if (modal) {
              modal.classList.remove('modal-open');
              document.body.style.overflow = '';
            }
          }
        });
      });
    }
  };

  // Auto-boot on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => window.NexaEngine.init());
  } else {
    window.NexaEngine.init();
  }
})();
