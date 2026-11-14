/**
 * ZÉGENHEIRO - Engenharia de Segurança & Combate a Incêndio
 * Script de Interatividade e Conversão
 * Eng. Responsável: José Luis | Tel / WhatsApp: +55 12 997683642
 */

document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_NUMBER = '5512997683642';

  // ------------------------------------------------------------------------
  // 1. Header Scroll Effect
  // ------------------------------------------------------------------------
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // ------------------------------------------------------------------------
  // 2. Mobile Menu Toggle
  // ------------------------------------------------------------------------
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close menu when clicking any nav link
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });
  }

  // ------------------------------------------------------------------------
  // 3. Active Nav Link on Scroll (Scrollspy)
  // ------------------------------------------------------------------------
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  function updateActiveNav() {
    const scrollPos = window.scrollY + 120;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }
  window.addEventListener('scroll', updateActiveNav);

  // ------------------------------------------------------------------------
  // 4. Interactive Quick Regularization Calculator
  // ------------------------------------------------------------------------
  const calcState = {
    tipo: 'Galpão Industrial / Logístico',
    area: '1.500m² a 5.000m²',
    situacao: 'Projeto Novo / Implantação de PPCI'
  };

  const tipoBtns = document.querySelectorAll('[data-calc-tipo]');
  const areaBtns = document.querySelectorAll('[data-calc-area]');
  const sitBtns = document.querySelectorAll('[data-calc-sit]');
  const calcSummaryEl = document.getElementById('calcSummaryText');
  const calcWaBtn = document.getElementById('calcWaBtn');

  function updateCalcDisplay() {
    if (calcSummaryEl) {
      calcSummaryEl.innerHTML = `<strong>${calcState.tipo}</strong> • Área: <strong>${calcState.area}</strong> • Situação: <strong>${calcState.situacao}</strong>`;
    }

    if (calcWaBtn) {
      const msg = `Olá Eng. José Luis, fiz uma simulação no site da Zégenheiro:\n- Tipo de Imóvel: ${calcState.tipo}\n- Metragem estimada: ${calcState.area}\n- Situação atual: ${calcState.situacao}\nGostaria de solicitar uma análise técnica e orçamento.`;
      calcWaBtn.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
    }
  }

  tipoBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tipoBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.tipo = btn.getAttribute('data-calc-tipo');
      updateCalcDisplay();
    });
  });

  areaBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      areaBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.area = btn.getAttribute('data-calc-area');
      updateCalcDisplay();
    });
  });

  sitBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      sitBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.situacao = btn.getAttribute('data-calc-sit');
      updateCalcDisplay();
    });
  });

  // Initial calc display call
  updateCalcDisplay();

  // ------------------------------------------------------------------------
  // 5. Hero Quick Form submission directly to WhatsApp
  // ------------------------------------------------------------------------
  const heroForm = document.getElementById('heroQuoteForm');
  if (heroForm) {
    heroForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = document.getElementById('heroNome')?.value || 'Não informado';
      const fone = document.getElementById('heroTelefone')?.value || 'Não informado';
      const tipo = document.getElementById('heroTipo')?.value || 'Não informado';
      const cidade = document.getElementById('heroCidade')?.value || 'Vale do Paraíba/SP';

      const msg = `Olá Eng. José Luis, solicito orçamento via formulário rápido Zégenheiro:\n- Nome: ${nome}\n- Telefone: ${fone}\n- Tipo de Imóvel: ${tipo}\n- Cidade/Região: ${cidade}\nAguardo seu retorno técnico.`;
      window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`, '_blank');
    });
  }

  // ------------------------------------------------------------------------
  // 6. Contact Form submission directly to WhatsApp
  // ------------------------------------------------------------------------
  const contactForm = document.getElementById('mainContactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = document.getElementById('contactNome')?.value || '';
      const empresa = document.getElementById('contactEmpresa')?.value || 'Particular';
      const fone = document.getElementById('contactTelefone')?.value || '';
      const servico = document.getElementById('contactServico')?.value || 'Geral';
      const msgTexto = document.getElementById('contactMensagem')?.value || '';

      const msg = `Olá Eng. José Luis (Zégenheiro),\nEntro em contato através do formulário do site:\n- Nome: ${nome}\n- Empresa/Condomínio: ${empresa}\n- Telefone: ${fone}\n- Serviço de Interesse: ${servico}\n- Detalhes: ${msgTexto}`;
      window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`, '_blank');
    });
  }

  // ------------------------------------------------------------------------
  // 7. Modal Form (Contact / Orçamento Modal)
  // ------------------------------------------------------------------------
  const modalBackdrop = document.getElementById('contactModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const openModalBtns = document.querySelectorAll('[data-open-modal="contact"]');

  function openModal() {
    if (modalBackdrop) {
      modalBackdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeModal() {
    if (modalBackdrop) {
      modalBackdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  openModalBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal();
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeModal);
  }

  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) {
        closeModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalBackdrop?.classList.contains('open')) {
      closeModal();
    }
  });

  // Modal form submit
  const modalForm = document.getElementById('modalQuoteForm');
  if (modalForm) {
    modalForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = document.getElementById('modalNome')?.value || '';
      const tel = document.getElementById('modalTelefone')?.value || '';
      const assunto = document.getElementById('modalAssunto')?.value || 'Consulta Técnica';
      const detalhe = document.getElementById('modalMensagem')?.value || '';

      const msg = `Olá Eng. José Luis, mensagem via modal de contato Zégenheiro:\n- Nome: ${nome}\n- Telefone: ${tel}\n- Assunto: ${assunto}\n- Mensagem: ${detalhe}`;
      closeModal();
      window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`, '_blank');
    });
  }

  // ------------------------------------------------------------------------
  // 8. FAQ Accordion
  // ------------------------------------------------------------------------
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question-btn');
    if (questionBtn) {
      questionBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        // Close all
        faqItems.forEach(i => i.classList.remove('active'));
        // Toggle current
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });

  // ------------------------------------------------------------------------
  // 9. Marquee Duplicate Elements for Infinite Smooth Scroll
  // ------------------------------------------------------------------------
  const marqueeTrack = document.getElementById('marqueeTrack');
  if (marqueeTrack) {
    // Clone children to ensure seamless endless loop
    const clone = marqueeTrack.innerHTML;
    marqueeTrack.innerHTML += clone;
  }
});

