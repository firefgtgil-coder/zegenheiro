import os

output_path = r"C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\assets\blueprint-fire-bg.svg"

# Dimensions
width = 1920
height = 1080

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">')

# Definitions: Patterns, markers, symbols
defs = """
<defs>
  <!-- Fine Grid Pattern (20x20) -->
  <pattern id="smallGrid" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#0369a1" stroke-width="0.35" stroke-opacity="0.28" />
  </pattern>
  <!-- Major Grid Pattern (100x100) with technical dots -->
  <pattern id="cadGrid" width="100" height="100" patternUnits="userSpaceOnUse">
    <rect width="100" height="100" fill="url(#smallGrid)" />
    <path d="M 100 0 L 0 0 0 100" fill="none" stroke="#38bdf8" stroke-width="0.75" stroke-opacity="0.4" />
    <circle cx="0" cy="0" r="1.5" fill="#38bdf8" fill-opacity="0.5" />
    <circle cx="100" cy="0" r="1.5" fill="#38bdf8" fill-opacity="0.5" />
    <circle cx="0" cy="100" r="1.5" fill="#38bdf8" fill-opacity="0.5" />
    <circle cx="100" cy="100" r="1.5" fill="#38bdf8" fill-opacity="0.5" />
  </pattern>

  <!-- Arrow Marker for dimensions and flow -->
  <marker id="cadArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#38bdf8" fill-opacity="0.8"/>
  </marker>
  <marker id="redArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#ef4444" fill-opacity="0.9"/>
  </marker>
  <marker id="greenArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#22c55e" fill-opacity="0.9"/>
  </marker>

  <!-- Sprinkler Head Symbol (NBR 10897) -->
  <g id="sprinklerSymbol">
    <circle cx="0" cy="0" r="7" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="-7" y1="0" x2="7" y2="0" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="0" y1="-7" x2="0" y2="7" stroke="#38bdf8" stroke-width="1.2" />
    <circle cx="0" cy="0" r="2.5" fill="#ef4444" />
  </g>

  <!-- Hydrant Box Symbol (NBR 13714) -->
  <g id="hydrantSymbol">
    <rect x="-11" y="-11" width="22" height="22" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.8" />
    <circle cx="0" cy="0" r="8" fill="none" stroke="#fca5a5" stroke-width="1" />
    <text x="0" y="4" font-family="'Courier New', monospace" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">H</text>
  </g>

  <!-- Smoke Detector Symbol (NBR 17240) -->
  <g id="detectorSymbol">
    <circle cx="0" cy="0" r="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.4" />
    <text x="0" y="3.5" font-family="'Courier New', monospace" font-size="7.5" font-weight="900" fill="#fbbf24" text-anchor="middle">DF</text>
    <circle cx="0" cy="0" r="11" fill="none" stroke="#f59e0b" stroke-width="0.8" stroke-dasharray="2,2" opacity="0.7"/>
  </g>

  <!-- Manual Alarm Pull Station (AM) -->
  <g id="alarmPullSymbol">
    <rect x="-8" y="-8" width="16" height="16" fill="#991b1b" stroke="#f87171" stroke-width="1.5" />
    <text x="0" y="3" font-family="'Courier New', monospace" font-size="6.5" font-weight="900" fill="#ffffff" text-anchor="middle">AM</text>
  </g>

  <!-- Extinguisher Symbol (NBR 12693) -->
  <g id="extinguisherSymbol">
    <polygon points="0,-10 9,6 -9,6" fill="#dc2626" stroke="#fca5a5" stroke-width="1.2" />
    <circle cx="0" cy="1" r="3" fill="#ffffff" />
    <text x="0" y="14" font-family="'Segoe UI', sans-serif" font-size="6.5" font-weight="bold" fill="#ef4444" text-anchor="middle">EXT PQS</text>
  </g>

  <!-- Emergency Exit Sign Block -->
  <g id="exitSignSymbol">
    <rect x="-14" y="-7" width="28" height="14" rx="2" fill="#14532d" stroke="#4ade80" stroke-width="1.2" />
    <text x="0" y="3.5" font-family="'Segoe UI', sans-serif" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">SAÍDA ➔</text>
  </g>
</defs>
"""
svg_parts.append(defs)

# Background color of the blueprint: deep engineering navy blueprint (#070d18)
svg_parts.append('<rect width="100%" height="100%" fill="#070d18" />')
# Overlay CAD grid
svg_parts.append('<rect width="100%" height="100%" fill="url(#cadGrid)" />')

# Group for blueprint drawing with technical styling
svg_parts.append('<g font-family="\'Courier New\', monospace" letter-spacing="0.5">')

# 1. Structural Architectural Grid Axes & Coordinates (Eixos Estruturais)
axes_x = [(220, "1"), (460, "2"), (760, "3"), (1060, "4"), (1360, "5"), (1680, "6")]
axes_y = [(140, "A"), (360, "B"), (620, "C"), (880, "D")]

# Draw axis lines
for x, label in axes_x:
    svg_parts.append(f'<line x1="{x}" y1="80" x2="{x}" y2="980" stroke="#0284c7" stroke-width="0.8" stroke-dasharray="14,4,3,4" opacity="0.45" />')
    # Bubble top
    svg_parts.append(f'<circle cx="{x}" cy="65" r="13" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.2" opacity="0.8"/>')
    svg_parts.append(f'<text x="{x}" y="70" font-size="12" font-weight="bold" fill="#bae6fd" text-anchor="middle">{label}</text>')
    # Bubble bottom
    svg_parts.append(f'<circle cx="{x}" cy="995" r="13" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.2" opacity="0.8"/>')
    svg_parts.append(f'<text x="{x}" y="1000" font-size="12" font-weight="bold" fill="#bae6fd" text-anchor="middle">{label}</text>')

for y, label in axes_y:
    svg_parts.append(f'<line x1="160" y1="{y}" x2="1760" y2="{y}" stroke="#0284c7" stroke-width="0.8" stroke-dasharray="14,4,3,4" opacity="0.45" />')
    # Bubble left
    svg_parts.append(f'<circle cx="140" cy="{y}" r="13" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.2" opacity="0.8"/>')
    svg_parts.append(f'<text x="140" y="{y+4}" font-size="12" font-weight="bold" fill="#bae6fd" text-anchor="middle">{label}</text>')
    # Bubble right
    svg_parts.append(f'<circle cx="1780" cy="{y}" r="13" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.2" opacity="0.8"/>')
    svg_parts.append(f'<text x="1780" y="{y+4}" font-size="12" font-weight="bold" fill="#bae6fd" text-anchor="middle">{label}</text>')

# 2. Main Architectural Walls & Partitions (Industrial Plant & Admin Complex)
walls = """
<!-- Exterior & Main Boundary Walls (Galpão Principal) -->
<rect x="220" y="140" width="1460" height="740" fill="none" stroke="#38bdf8" stroke-width="3" opacity="0.85" />
<rect x="224" y="144" width="1452" height="732" fill="none" stroke="#0284c7" stroke-width="1.2" opacity="0.5" />

<!-- Structural Columns (Pilares) -->
"""
svg_parts.append(walls)

# Generate columns at grid intersections
for x, _ in axes_x:
    for y, _ in axes_y:
        svg_parts.append(f'<rect x="{x-7}" y="{y-7}" width="14" height="14" fill="#0369a1" stroke="#38bdf8" stroke-width="1.4" opacity="0.9" />')

# Internal Partitions:
# Area 1: Casa de Bombas & Reservatório (Upper Left: x=220..460, y=140..360)
# Area 2: Mezanino Administrativo / Escritórios (Upper Right: x=1060..1680, y=140..360)
# Area 3: Galpão de Estocagem e Produção (Center: x=460..1680, y=360..880)
# Area 4: Docas de Carga e Saída de Emergência (Bottom: x=460..1360, y=880)
partitions = """
<!-- Casa de Bombas CBI Partition -->
<rect x="220" y="140" width="240" height="220" fill="#0f172a" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2" />
<text x="340" y="170" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">SALA DE BOMBAS (CBI)</text>
<text x="340" y="186" font-size="8.5" fill="#38bdf8" text-anchor="middle">ÁREA TÉCNICA - NÍVEL ±0.00</text>

<!-- Mezanino Escritórios / Apoio -->
<rect x="1060" y="140" width="620" height="220" fill="#0f172a" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2" />
<line x1="1360" y1="140" x2="1360" y2="360" stroke="#38bdf8" stroke-width="1.5" />
<text x="1210" y="170" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">ESCRITÓRIOS &amp; ENGENHARIA</text>
<text x="1520" y="170" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">RECEPÇÃO / EXPEDIÇÃO</text>

<!-- Central de Alarme CIE Room -->
<rect x="1060" y="270" width="120" height="90" fill="#0c4a6e" fill-opacity="0.5" stroke="#ef4444" stroke-width="1.6" />
<text x="1120" y="310" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">CENTRAL ALARME</text>
<text x="1120" y="324" font-size="8" fill="#f87171" text-anchor="middle">CIE - 24V (NBR 17240)</text>

<!-- Main Storage / Production Hall Label -->
<text x="760" y="520" font-size="16" font-weight="900" fill="#0284c7" fill-opacity="0.35" text-anchor="middle" letter-spacing="4">GALPÃO LOGÍSTICO / PRODUÇÃO</text>
<text x="760" y="544" font-size="11" font-weight="bold" fill="#0369a1" fill-opacity="0.4" text-anchor="middle">PÉ DIREITO LIVRE = 12.00m | CARGA DE INCÊNDIO: ALTO RISCO (J-4)</text>

<!-- Docas de Carga -->
<rect x="460" y="810" width="600" height="70" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,6" />
<text x="760" y="850" font-size="11" font-weight="bold" fill="#38bdf8" opacity="0.7" text-anchor="middle">DOCAS DE LOGÍSTICA &amp; EXPEDIÇÃO (PORTAS AUTOMÁTICAS)</text>
"""
svg_parts.append(partitions)

# 3. Fire Protection Equipment Details:
# RTI (Reservatório Técnico de Incêndio)
rti = """
<!-- RTI (Reservatório Cilíndrico Externo) at x=110, y=250 -->
<circle cx="110" cy="250" r="70" fill="#0c4a6e" fill-opacity="0.3" stroke="#ef4444" stroke-width="2.5" />
<circle cx="110" cy="250" r="66" fill="none" stroke="#f87171" stroke-width="1" stroke-dasharray="4,4" />
<circle cx="110" cy="250" r="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" />
<text x="110" y="246" font-size="9" font-weight="900" fill="#fee2e2" text-anchor="middle">RTI</text>
<text x="110" y="258" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">65.000L</text>
<text x="110" y="340" font-size="8.5" font-weight="bold" fill="#ef4444" text-anchor="middle">RESERVATÓRIO METÁLICO</text>
<text x="110" y="352" font-size="7.5" fill="#fca5a5" text-anchor="middle">RESERVA TÉCNICA DE INCÊNDIO</text>

<!-- RTI Suction Pipe to CBI -->
<path d="M 180 250 L 260 250 L 260 210" fill="none" stroke="#ef4444" stroke-width="3" />
<text x="215" y="242" font-size="7.5" fill="#fca5a5">SUCÇÃO ⌀ 4"</text>
"""
svg_parts.append(rti)

# CBI Equipment (Pumps)
cbi_pumps = """
<!-- Bomba Principal Elétrica (B-01) -->
<rect x="250" y="190" width="30" height="20" rx="3" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
<text x="265" y="203" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">B-01</text>
<text x="265" y="222" font-size="6.5" fill="#fca5a5" text-anchor="middle">25 CV (ELÉTRICA)</text>

<!-- Bomba Reserva Diesel (B-02) -->
<rect x="310" y="190" width="30" height="20" rx="3" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
<text x="325" y="203" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">B-02</text>
<text x="325" y="222" font-size="6.5" fill="#fde68a" text-anchor="middle">30 CV (DIESEL)</text>

<!-- Bomba Jockey (BJ) -->
<rect x="370" y="190" width="20" height="16" rx="2" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2" />
<text x="380" y="201" font-size="6" font-weight="bold" fill="#ffffff" text-anchor="middle">BJ</text>
<text x="380" y="218" font-size="6" fill="#7dd3fc" text-anchor="middle">3 CV</text>

<!-- Barrilete Geral de Incêndio da Casa de Bombas -->
<path d="M 265 190 L 265 160 L 440 160 L 440 370" fill="none" stroke="#ef4444" stroke-width="3.5" />
<line x1="325" y1="190" x2="325" y2="160" stroke="#ef4444" stroke-width="2.5" />
<line x1="380" y1="190" x2="380" y2="160" stroke="#ef4444" stroke-width="1.8" />
<text x="345" y="153" font-size="8" font-weight="bold" fill="#fee2e2">BARRILETE PRINCIPAL ⌀ 4" (SCH 40)</text>
"""
svg_parts.append(cbi_pumps)

# 4. Main Hydraulic Ring (Anel de Hidrantes / Tubulação de Incêndio)
# Highlighting the fire network in bold CAD red and cyan
fire_network = """
<!-- Main Trunk Distribution Piping (Anel Fechado de Incêndio) -->
<path d="M 440 370 L 440 850 L 1650 850 L 1650 370 L 440 370 Z" fill="none" stroke="#ef4444" stroke-width="3.2" opacity="0.9" />

<!-- Piping diameter callouts -->
<text x="448" y="620" font-size="8.5" font-weight="bold" fill="#fca5a5" transform="rotate(-90 448 620)">REDE DE INCÊNDIO ⌀ 2½" (65mm)</text>
<text x="1050" y="842" font-size="8.5" font-weight="bold" fill="#fca5a5">COLUNA / ANEL DE COMBATE A INCÊNDIO ⌀ 2½" (65mm)</text>
<text x="1660" y="620" font-size="8.5" font-weight="bold" fill="#fca5a5" transform="rotate(90 1660 620)">COLUNA DE HIDRANTES ⌀ 2½" (65mm)</text>
<text x="1050" y="382" font-size="8.5" font-weight="bold" fill="#fca5a5">ALIMENTAÇÃO HIDRANTES &amp; SPRINKLERS ⌀ 3"</text>

<!-- Branch connection to Siamese street intake (Registro de Recalque de Passeio) -->
<path d="M 440 850 L 440 940 L 320 940" fill="none" stroke="#ef4444" stroke-width="3" marker-end="url(#redArrow)" />
<circle cx="320" cy="940" r="12" fill="#7f1d1d" stroke="#f87171" stroke-width="2" />
<text x="320" y="943" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">RP</text>
<text x="320" y="966" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">REGISTRO DE RECALQUE</text>
<text x="320" y="977" font-size="7" fill="#fca5a5" text-anchor="middle">PASSEIO PÚBLICO (DUPLO ⌀ 2½")</text>
"""
svg_parts.append(fire_network)

# Hydrants Placement (Símbolos H-01 a H-08)
hydrants = [
    (440, 370, "H-01", "HIDRANTE DUPLO - ABRIGO 90x60cm"),
    (440, 610, "H-02", "HIDRANTE SIMPLES - MANG. 30m"),
    (440, 850, "H-03", "HIDRANTE DUPLO - DOCAS"),
    (800, 850, "H-04", "HIDRANTE SIMPLES - PRODUÇÃO"),
    (1200, 850, "H-05", "HIDRANTE SIMPLES - ESTOQUE"),
    (1650, 850, "H-06", "HIDRANTE DUPLO - EXPEDIÇÃO"),
    (1650, 610, "H-07", "HIDRANTE SIMPLES - CORREDOR"),
    (1650, 370, "H-08", "HIDRANTE DUPLO - MEZANINO"),
    (1060, 370, "H-09", "HIDRANTE DE COLUNA - ADM"),
]

for hx, hy, hid, desc in hydrants:
    svg_parts.append(f'<use href="#hydrantSymbol" x="{hx}" y="{hy}" />')
    offset_y = -18 if hy > 500 else 24
    svg_parts.append(f'<text x="{hx}" y="{hy+offset_y}" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">{hid}</text>')

# 5. Sprinkler Grid & Piping (Chuveiros Automáticos)
# Sprinkler branch lines from x=540 to 1560, y from 420 to 780
sprinkler_svg = ['<!-- Rede de Sprinklers / Chuveiros Automáticos -->']
for sy in range(430, 810, 70):
    sprinkler_svg.append(f'<line x1="500" y1="{sy}" x2="1580" y2="{sy}" stroke="#0284c7" stroke-width="1.4" opacity="0.75" />')
    sprinkler_svg.append(f'<text x="480" y="{sy+3}" font-size="7" fill="#38bdf8" text-anchor="end">RAMAL ⌀ 1¼"</text>')
    # Add sprinkler heads along the line
    for sx in range(540, 1560, 90):
        sprinkler_svg.append(f'<use href="#sprinklerSymbol" x="{sx}" y="{sy}" />')

# Sprinkler Submain feeding line
sprinkler_svg.append('<line x1="1050" y1="370" x2="1050" y2="790" stroke="#0ea5e9" stroke-width="2.5" />')
sprinkler_svg.append('<text x="1058" y="450" font-size="8" font-weight="bold" fill="#7dd3fc">SUB-TRONCO SPRINKLER ⌀ 3"</text>')
sprinkler_svg.append('<rect x="1040" y="380" width="20" height="20" fill="#0369a1" stroke="#38bdf8" stroke-width="1.2" />')
sprinkler_svg.append('<text x="1050" y="394" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">VGA</text>')
sprinkler_svg.append('<text x="1050" y="415" font-size="6.5" fill="#38bdf8" text-anchor="middle">VÁLVULA GOVERNO</text>')

svg_parts.append('\n'.join(sprinkler_svg))

# 6. Fire Alarm Detectors & Manual Pull Stations
detectors = [
    (1140, 200), (1280, 200), (1420, 200), (1560, 200),
    (1140, 300), (1280, 300), (1420, 300), (1560, 300),
    (600, 480), (900, 480), (1200, 480), (1500, 480),
    (600, 720), (900, 720), (1200, 720), (1500, 720)
]
for dx, dy in detectors:
    svg_parts.append(f'<use href="#detectorSymbol" x="{dx}" y="{dy}" />')

# Alarm loops (dashed orange lines connecting detectors)
svg_parts.append('<path d="M 1120 270 L 1120 200 L 1560 200 L 1560 300 L 1180 300" fill="none" stroke="#f59e0b" stroke-width="0.9" stroke-dasharray="3,3" opacity="0.65" />')

# Alarm manual pull stations
pull_stations = [(465, 875), (1060, 875), (1675, 875), (1065, 145), (1675, 145)]
for px, py in pull_stations:
    svg_parts.append(f'<use href="#alarmPullSymbol" x="{px}" y="{py}" />')

# 7. Extinguishers Placement (PQS, CO2, AP)
extinguishers = [
    (430, 480), (430, 740), (760, 860), (1360, 860), (1665, 480), (1665, 740), (1250, 360), (1500, 360)
]
for ex, ey in extinguishers:
    svg_parts.append(f'<use href="#extinguisherSymbol" x="{ex}" y="{ey}" />')

# 8. Evacuation Routes & Emergency Exit Signs (Rotas de Fuga)
evac_routes = """
<!-- Rotas de Fuga com Setas Fotoluminescentes -->
<path d="M 760 600 L 760 810 L 760 880" fill="none" stroke="#22c55e" stroke-width="2.2" stroke-dasharray="10,5" marker-end="url(#greenArrow)" opacity="0.85" />
<path d="M 1360 600 L 1360 810 L 1360 880" fill="none" stroke="#22c55e" stroke-width="2.2" stroke-dasharray="10,5" marker-end="url(#greenArrow)" opacity="0.85" />
<path d="M 1400 240 L 1400 360 L 1650 360 L 1680 360" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="8,4" marker-end="url(#greenArrow)" opacity="0.85" />

<!-- Emergency Exit Signs (Saídas de Emergência) -->
<use href="#exitSignSymbol" x="760" y="878" />
<use href="#exitSignSymbol" x="1360" y="878" />
<use href="#exitSignSymbol" x="1680" y="360" />
<use href="#exitSignSymbol" x="220" y="360" />

<text x="760" y="904" font-size="7.5" font-weight="bold" fill="#4ade80" text-anchor="middle">SAÍDA DE EMERGÊNCIA S-01 (P.C.F. P-90)</text>
<text x="1360" y="904" font-size="7.5" font-weight="bold" fill="#4ade80" text-anchor="middle">SAÍDA DE EMERGÊNCIA S-02 (P.C.F. P-90)</text>
"""
svg_parts.append(evac_routes)

# 9. Technical Dimension Lines (Cotas de Engenharia em Metros)
dimensions = """
<!-- Dimension Line Top: Overall Length = 73.00m -->
<line x1="220" y1="105" x2="1680" y2="105" stroke="#38bdf8" stroke-width="1.2" marker-start="url(#cadArrow)" marker-end="url(#cadArrow)" />
<line x1="220" y1="95" x2="220" y2="135" stroke="#38bdf8" stroke-width="0.8" />
<line x1="1680" y1="95" x2="1680" y2="135" stroke="#38bdf8" stroke-width="0.8" />
<rect x="910" y="95" width="80" height="18" fill="#070d18" stroke="#0284c7" stroke-width="0.8" rx="2" />
<text x="950" y="108" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">73.00 m</text>

<!-- Dimension Line Left: Overall Width = 37.00m -->
<line x1="185" y1="140" x2="185" y2="880" stroke="#38bdf8" stroke-width="1.2" marker-start="url(#cadArrow)" marker-end="url(#cadArrow)" />
<line x1="175" y1="140" x2="215" y2="140" stroke="#38bdf8" stroke-width="0.8" />
<line x1="175" y1="880" x2="215" y2="880" stroke="#38bdf8" stroke-width="0.8" />
<rect x="155" y="495" width="60" height="18" fill="#070d18" stroke="#0284c7" stroke-width="0.8" rx="2" transform="rotate(-90 185 504)" />
<text x="185" y="508" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle" transform="rotate(-90 185 508)">37.00 m</text>
"""
svg_parts.append(dimensions)

# 10. Technical Notes Box (Notas de Engenharia e Legislação) - Upper Left Area
tech_notes = """
<!-- Quadro de Notas Técnicas de Projeto -->
<g transform="translate(480, 160)">
  <rect x="0" y="0" width="550" height="180" fill="#0f172a" fill-opacity="0.85" stroke="#0284c7" stroke-width="1.4" rx="4" />
  <rect x="0" y="0" width="550" height="24" fill="#0369a1" fill-opacity="0.4" stroke="#0284c7" stroke-width="1.4" rx="4" />
  <text x="15" y="17" font-size="10" font-weight="900" fill="#bae6fd" letter-spacing="1">NOTAS TÉCNICAS DE SEGURANÇA CONTRA INCÊNDIO &amp; PÂNICO (PPCI)</text>
  
  <text x="15" y="42" font-size="7.8" fill="#e0f2fe">1. PROJETO ELABORADO CONFORME DECRETO ESTADUAL Nº 63.911/18 E INSTRUÇÕES TÉCNICAS (IT) DO CBPMESP.</text>
  <text x="15" y="58" font-size="7.8" fill="#e0f2fe">2. OCUPAÇÃO: DIVISÃO J-4 (DEPÓSITOS DE GRANDE PORTE E CARGA COMBUSTÍVEL ELEVADA / NBR 14432).</text>
  <text x="15" y="74" font-size="7.8" fill="#e0f2fe">3. SISTEMAS INSTALADOS: ACESSO DE VIATURAS (IT-06), SAÍDAS DE EMERGÊNCIA (IT-11), BRIGADA (IT-17),</text>
  <text x="32" y="88" font-size="7.8" fill="#e0f2fe">ILUMINAÇÃO DE EMERGÊNCIA (IT-18), ALARME (IT-19), EXTINTORES (IT-21), HIDRANTES (IT-22) E SPRINKLERS (IT-23).</text>
  <text x="15" y="104" font-size="7.8" fill="#e0f2fe">4. REDE DE HIDRANTES CALCULADA HIDRAULICAMENTE COM PRESSÃO MÍNIMA RESIDUAL DE 10.0 mca NO BICO MAIS DESFAVORÁVEL.</text>
  <text x="15" y="120" font-size="7.8" fill="#e0f2fe">5. RESERVA TÉCNICA DE INCÊNDIO (RTI) EFETIVA: 65,000 LITROS EXCLUSIVA PARA HIDRANTES E CHUVEIROS AUTOMÁTICOS.</text>
  <text x="15" y="136" font-size="7.8" fill="#e0f2fe">6. ART DE PROJETO E RESPONSABILIDADE TÉCNICA REGISTRADA NO CREA-SP SOB RESPONSABILIDADE DO ENG. JOSÉ LUIS.</text>
  
  <!-- Stamp Indicator -->
  <rect x="15" y="148" width="130" height="22" fill="#14532d" stroke="#22c55e" stroke-width="1" rx="2" />
  <text x="80" y="162" font-size="8" font-weight="bold" fill="#86efac" text-anchor="middle">✔ CONFORME CORPO BOMBEIROS</text>
  
  <rect x="155" y="148" width="120" height="22" fill="#7f1d1d" stroke="#ef4444" stroke-width="1" rx="2" />
  <text x="215" y="162" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">ART CREA-SP REGISTRADA</text>
</g>
"""
svg_parts.append(tech_notes)

# 11. Engineering Title Block / Stamp (Carimbo de Engenharia Oficial ABNT) - Bottom Right Corner
stamp = """
<!-- Carimbo Oficial de Engenharia do Projeto (Title Block) -->
<g transform="translate(1180, 895)">
  <rect x="0" y="0" width="500" height="150" fill="#0a101d" stroke="#38bdf8" stroke-width="2" />
  
  <!-- Internal grid of the title block -->
  <line x1="0" y1="36" x2="500" y2="36" stroke="#0284c7" stroke-width="1" />
  <line x1="0" y1="88" x2="500" y2="88" stroke="#0284c7" stroke-width="1" />
  <line x1="0" y1="120" x2="500" y2="120" stroke="#0284c7" stroke-width="1" />
  
  <line x1="160" y1="0" x2="160" y2="88" stroke="#0284c7" stroke-width="1" />
  <line x1="340" y1="88" x2="340" y2="150" stroke="#0284c7" stroke-width="1" />
  
  <!-- Brand logo inside the stamp -->
  <text x="80" y="22" font-family="'Montserrat', sans-serif" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">
    Zé<tspan fill="#ef4444">genheiro</tspan>
  </text>
  <text x="80" y="32" font-size="6.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">ENGENHARIA DE SEGURANÇA</text>
  <text x="80" y="55" font-size="7.5" fill="#bae6fd" text-anchor="middle">PROJETOS &amp; CONSULTORIA</text>
  <text x="80" y="68" font-size="7" fill="#7dd3fc" text-anchor="middle">COMBATE A INCÊNDIO &amp; AVCB</text>
  <text x="80" y="80" font-size="6.5" fill="#38bdf8" text-anchor="middle">VALE DO PARAÍBA - SP</text>
  
  <!-- Project Title and Details -->
  <text x="170" y="16" font-size="7.5" fill="#7dd3fc">PROJETO TÉCNICO DE COMBATE A INCÊNDIO (PPCI)</text>
  <text x="170" y="30" font-size="11" font-weight="900" fill="#ffffff">SISTEMAS DE HIDRANTES, SPRINKLERS &amp; ALARME</text>
  
  <text x="170" y="52" font-size="7.5" fill="#7dd3fc">RESPONSÁVEL TÉCNICO:</text>
  <text x="170" y="66" font-size="10.5" font-weight="bold" fill="#fde047">ENG. JOSÉ LUIS - ENGENHEIRO DE SEGURANÇA</text>
  <text x="170" y="80" font-size="7.5" fill="#e0f2fe">REGISTRO CREA-SP / ART Nº 2802723009418 - VIA FÁCIL BOMBEIROS</text>
  
  <!-- Metadata bottom row -->
  <text x="10" y="104" font-size="7.5" fill="#7dd3fc">LOCAL: COMPLEXO INDUSTRIAL &amp; LOGÍSTICO</text>
  <text x="10" y="115" font-size="7" fill="#bae6fd">CONFORMIDADE: NBR 13714 / NBR 10897 / NBR 17240 / IT-CBPMESP</text>
  <text x="10" y="136" font-size="7" fill="#64748b">PROPRIEDADE TÉCNICA RESERVADA - ZÉGENHEIRO</text>
  
  <!-- Right metrics -->
  <text x="350" y="104" font-size="7.5" fill="#7dd3fc">ESCALA: 1:100</text>
  <text x="420" y="104" font-size="7.5" fill="#7dd3fc">DATA: 2026</text>
  <text x="350" y="115" font-size="7.5" fill="#7dd3fc">ETAPA: APROVAÇÃO AVCB</text>
  <text x="350" y="138" font-size="9" font-weight="bold" fill="#4ade80">SITUAÇÃO: APROVADO</text>
  <text x="455" y="138" font-size="10" font-weight="bold" fill="#38bdf8">FL 01/01</text>
</g>
"""
svg_parts.append(stamp)

# Close group and svg
svg_parts.append('</g>')
svg_parts.append('</svg>')

full_svg = '\n'.join(svg_parts)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_svg)

print(f"Blueprint SVG generated successfully: {len(full_svg)} bytes written to {output_path}")

