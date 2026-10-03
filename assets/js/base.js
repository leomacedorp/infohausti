/**
 * INFOHAUS RP — BASE JS
 * Componentes interativos essenciais: Menu mobile acessível, Voltar ao Topo e LGPD.
 * Zero dependências externas.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initMobileMenu();
    initBackToTop();
    initLgpdBanner();
  });

  /**
   * 1. Menu Mobile com suporte a Acessibilidade (ARIA + Teclado)
   */
  function initMobileMenu() {
    var menuToggle = document.querySelector('[data-menu-toggle]');
    var menuNav = document.querySelector('[data-menu-nav]');

    if (!menuToggle || !menuNav) return;

    function toggleMenu(forceState) {
      var isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      var nextState = typeof forceState === 'boolean' ? forceState : !isExpanded;

      menuToggle.setAttribute('aria-expanded', String(nextState));
      menuNav.classList.toggle('is-open', nextState);

      if (nextState) {
        var firstLink = menuNav.querySelector('a');
        if (firstLink) firstLink.focus();
      }
    }

    menuToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      toggleMenu();
    });

    // Fechar ao pressionar Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
        toggleMenu(false);
        menuToggle.focus();
      }
    });

    // Fechar ao clicar fora
    document.addEventListener('click', function (e) {
      if (menuToggle.getAttribute('aria-expanded') === 'true' && !menuNav.contains(e.target) && e.target !== menuToggle) {
        toggleMenu(false);
      }
    });
  }

  /**
   * 2. Botão Voltar ao Topo
   */
  function initBackToTop() {
    var btn = document.querySelector('[data-back-to-top]');
    if (!btn) return;

    var isTicking = false;

    window.addEventListener('scroll', function () {
      if (!isTicking) {
        window.requestAnimationFrame(function () {
          if (window.scrollY > 300) {
            btn.classList.add('is-visible');
          } else {
            btn.classList.remove('is-visible');
          }
          isTicking = false;
        });
        isTicking = true;
      }
    });

    btn.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
      // Retornar foco ao skip link para acessibilidade
      var skip = document.querySelector('.skip-link');
      if (skip) skip.focus();
    });
  }

  /**
   * 3. Banner de Conformidade LGPD
   */
  function initLgpdBanner() {
    var banner = document.querySelector('[data-lgpd-banner]');
    var acceptBtn = document.querySelector('[data-lgpd-accept]');

    if (!banner) return;

    var consentKey = 'infohausti_lgpd_consent';

    try {
      if (!localStorage.getItem(consentKey)) {
        banner.classList.add('is-active');
      }
    } catch (e) {
      // LocalStorage desativado ou navegação privada restrita
      banner.classList.add('is-active');
    }

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function () {
        try {
          localStorage.setItem(consentKey, 'accepted_' + new Date().toISOString());
        } catch (e) {
          // Ignora falha de escrita em storage restrito
        }
        banner.classList.remove('is-active');
      });
    }
  }
})();
