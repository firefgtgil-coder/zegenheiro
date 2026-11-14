# 🚒 Landing Page Zégenheiro | Engenharia de Segurança & Combate a Incêndio

Landing page institucional e de alta conversão para a **Zégenheiro**, liderada pelo engenheiro responsável **Eng. José Luis**, com foco em serviços especializados de Engenharia de Segurança e Combate a Incêndio (PPCI, emissão e renovação de AVCB/CLCB, hidrantes, laudos e consultoria).

---

## 📋 Características e Requisitos Atendidos

1. **Identidade da Marca:**
   - Ordem estrita respeitada: `[Logo do capacete de combate a incêndio]` + `Zégenheiro` tanto no cabeçalho fixo quanto no rodapé e no modal.
   - Símbolo de capacete estrutural de bombeiro com escudo de engenharia (`ENG`) em alta resolução vetorial.
   - Tipografia de impacto com destaque cromático em Vermelho Fogo (`#EF4444` / `#DC2626`) e Dourado de Segurança (`#F59E0B`).

2. **Background Temático de Engenharia (Blueprint de Combate a Incêndio):**
   - Ilustração vetorial rica (`blueprint-fire-bg.svg`) retratando uma planta baixa técnica de complexo industrial e comercial com:
     - Reservatório Técnico de Incêndio (RTI de 65.000 L)
     - Casa de Bombas de Incêndio (CBI com bomba elétrica, bomba diesel e bomba jockey)
     - Tubulações e anel hidráulico de hidrantes (aço carbono SCH 40 ⌀ 2½")
     - Malha de chuveiros automáticos / sprinklers (NBR 10897) e Válvula de Governo e Alarme (VGA)
     - Detectores de fumaça óticos e acionadores manuais endereçáveis (NBR 17240)
     - Rotas de fuga e saídas de emergência com portas corta-fogo P-90 e sinalização fotoluminescente
     - Cotas técnicas em metros e carimbo oficial de engenharia ABNT / Corpo de Bombeiros.
   - **Película escura superposta com transparência superior a 70% (`rgba(10, 15, 26, 0.78)`):** assegura contraste e legibilidade impecáveis para o texto em qualquer tela, mantendo a sofisticação do projeto CAD visível ao fundo.

3. **Copywriting Profissional & Persuasivo:**
   - Alerta direto para gestores, síndicos e diretores sobre os riscos severos de operar sem projeto aprovado ou com AVCB vencido:
     - Responsabilidade Civil e Criminal
     - Interdição Imediata e Lacração pelo Corpo de Bombeiros / Prefeitura
     - Recusa Total de Indenização por Seguradoras em Sinistros
     - Ameaça Real à Vida de Colaboradores e Ocupantes
   - A engenharia preventiva apresentada como investimento estratégico em tranquilidade e conformidade legal.

4. **Engenheiro Responsável Técnico:**
   - Destaque ao **Eng. José Luis**, com ênfase em sua atuação técnica, registro no CREA-SP, emissão de ART (Anotação de Responsabilidade Técnica) e agilidade na tramitação sem exigências travadas no sistema Via Fácil Bombeiros.

5. **Prova Social & Depoimentos:**
   - Casos reais/fictícios de sucesso abrangendo clientes industriais (Vanguard Indústria Metalmecânica), condomínios de grande porte (Grand Tower) e centros de distribuição (Apex Logística).

6. **Carrossel Infinito de Clientes (Logo Marquee / Ticker):**
   - Faixa contínua com logotipos vetorizados de indústrias, construtoras, shoppings e centros logísticos (Vanguard, Apex, Titan Engenharia, Horizonte Condomínios, Metrópole Center, Valetec, Alfa Farma).
   - Animação CSS suave em loop infinito com pausa automática ao passar o mouse.

7. **Chamadas para Ação (CTAs) & Integração WhatsApp:**
   - Número oficial: **`+55 12 997683642`** (Exibição: `(12) 99768-3642`)
   - Links com mensagens personalizadas e URL-encoded para cada ponto de contato (topo, hero, serviços, simulador e rodapé).
   - **Simulador Interativo de Regularização:** permite ao visitante escolher tipo de imóvel, área construída e situação atual, gerando um resumo pronto enviado direto ao WhatsApp.
   - **Botão Flutuante do WhatsApp:** fixo no canto inferior direito com animação de pulso luminoso e tooltip.
   - **Modal de Contato Rápido:** acionado com um clique em botões da página ou atalho ESC.

---

## 📂 Arquitetura de Arquivos

```
zegenheiro-landing-page/
├── index.html                 # Estrutura HTML5 semântica e acessível
├── css/
│   └── styles.css             # Design system completo, responsivo e estilizado
├── js/
│   └── main.js                # Interatividades, scrollspy, calculadora e WhatsApp
├── assets/
│   ├── logo.svg               # Logo completa horizontal com capacete e tipografia
│   ├── logo-symbol.svg        # Símbolo vetorial isolado do capacete de bombeiro
│   ├── logo-white.svg         # Versão em alto contraste para fundos escuros
│   ├── blueprint-fire-bg.svg  # Planta técnica CAD/Blueprint de combate a incêndio
│   ├── favicon.svg            # Favicon SVG moderno
│   └── favicon.ico            # Favicon ICO padrão
├── README.md                  # Documentação do projeto
├── build_assets.py            # Script auxiliar de geração dos vetores da marca
├── generate_blueprint.py      # Script de desenho da planta técnica em SVG
└── make_ico.py                # Gerador binário do favicon.ico
```

---

## 🚀 Como Visualizar Localmente

### Opção 1: Abrir diretamente no navegador
Basta dar um duplo clique no arquivo `index.html` ou abri-lo pelo seu navegador favorito (Google Chrome, Microsoft Edge, Firefox, Safari).

### Opção 2: Iniciar um servidor HTTP local simples
Se desejar rodar via servidor local (recomendado):

No PowerShell / Terminal:
```powershell
cd "C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page"
python -m http.server 8080
```
Depois, abra no navegador: `http://localhost:8080`

---

## 📞 Dados de Contato Configurados
- **Empresa:** Zégenheiro - Engenharia de Segurança & Combate a Incêndio
- **Responsável:** Eng. José Luis
- **WhatsApp:** +55 12 997683642
- **Região:** Vale do Paraíba, Litoral Norte, Serra da Mantiqueira e Grande São Paulo

