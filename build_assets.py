import os

target_dir = r"C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\assets"
os.makedirs(target_dir, exist_ok=True)

# 1. Firefighter Helmet Symbol SVG (100x100)
helmet_symbol_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <defs>
    <linearGradient id="helmGrad" x1="20" y1="15" x2="80" y2="75" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#EF4444" />
      <stop offset="50%" stop-color="#DC2626" />
      <stop offset="100%" stop-color="#991B1B" />
    </linearGradient>
    <linearGradient id="shieldGrad" x1="38" y1="28" x2="62" y2="60" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="60%" stop-color="#EAB308" />
      <stop offset="100%" stop-color="#CA8A04" />
    </linearGradient>
    <linearGradient id="brimGrad" x1="10" y1="58" x2="90" y2="68" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1F2937" />
      <stop offset="50%" stop-color="#374151" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
    <filter id="helmShadow" x="-10%" y="-10%" width="120%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="2" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>
  
  <!-- Extended Rear Brim / Neck Protector -->
  <path d="M12 63 C12 63, 16 75, 50 75 C84 75, 88 63, 88 63 C94 65, 96 70, 85 78 C70 87, 30 87, 15 78 C4 70, 6 65, 12 63 Z" fill="#111827" />
  
  <!-- Main Front & Side Brim -->
  <path d="M8 60 C14 55, 30 52, 50 52 C70 52, 86 55, 92 60 C95 62, 94 66, 88 67 C70 71, 30 71, 12 67 C6 66, 5 62, 8 60 Z" fill="url(#brimGrad)" stroke="#4B5563" stroke-width="1.2" />
  
  <!-- Reflective Brim Trim -->
  <path d="M14 62 C26 57, 40 55, 50 55 C60 55, 74 57, 86 62" stroke="#FDE047" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.9"/>
  
  <!-- Helmet Dome (Crown) -->
  <path d="M18 56 C18 30, 30 18, 50 18 C70 18, 82 30, 82 56 C74 53, 58 51, 50 51 C42 51, 26 53, 18 56 Z" fill="url(#helmGrad)" filter="url(#helmShadow)"/>
  
  <!-- Helmet Central Ridge (Top Spine Ribbing) -->
  <path d="M47 18 C47 16, 53 16, 53 18 L52 46 C52 47, 48 47, 48 46 Z" fill="#F87171" opacity="0.8" />
  <path d="M49 18 L51 18 L50.5 46 L49.5 46 Z" fill="#FEF2F2" opacity="0.9" />

  <!-- Side Reinforcement Ribs -->
  <path d="M30 27 C34 35, 36 44, 37 51" stroke="#B91C1C" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M70 27 C66 35, 64 44, 63 51" stroke="#7F1D1D" stroke-width="2" stroke-linecap="round" fill="none"/>

  <!-- High-Visibility Reflective Tetrahedrons / Decals -->
  <polygon points="24,42 30,36 31,44" fill="#FACC15" opacity="0.95" />
  <polygon points="76,42 70,36 69,44" fill="#FACC15" opacity="0.95" />

  <!-- Traditional Firefighter Shield Plaque (Front Shield) -->
  <path d="M38 30 C38 30, 50 25, 62 30 C62 44, 57 55, 50 58 C43 55, 38 44, 38 30 Z" fill="url(#shieldGrad)" stroke="#78350F" stroke-width="1.2" filter="url(#helmShadow)"/>
  <path d="M40 32 C43 29, 57 29, 60 32 C60 43, 56 53, 50 55 C44 53, 40 43, 40 32 Z" fill="none" stroke="#FEF08A" stroke-width="0.8" opacity="0.8"/>

  <!-- Shield Insignia: Cross arms -->
  <g fill="#991B1B">
    <path d="M50 36 L47 33 L53 33 Z" />
    <path d="M50 44 L47 47 L53 47 Z" />
    <path d="M46 40 L43 37 L43 43 Z" />
    <path d="M54 40 L57 37 L57 43 Z" />
    <circle cx="50" cy="40" r="3.5" fill="#7F1D1D" stroke="#FEF08A" stroke-width="0.6"/>
  </g>
  <!-- Flame / Torch icon in badge -->
  <path d="M50 38.5 C49 39.5, 49 41, 50 42 C51 41, 51 39.5, 50 38.5 Z" fill="#FDE047" />
  <!-- Text on Shield: ENG -->
  <text x="50" y="52" font-family="'Segoe UI', Roboto, sans-serif" font-size="4.2" font-weight="900" fill="#78350F" text-anchor="middle" letter-spacing="0.5">ENG</text>
  
  <ellipse cx="50" cy="62" rx="4" ry="1.5" fill="#9CA3AF" opacity="0.7"/>
</svg>"""

with open(os.path.join(target_dir, "logo-symbol.svg"), "w", encoding="utf-8") as f:
    f.write(helmet_symbol_svg)

# 2. Favicon SVG
with open(os.path.join(target_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(helmet_symbol_svg)

# 3. Full Brand Logo: [Capacete] + Zégenheiro + Engenharia de Segurança & Incêndio (viewBox 0 0 320 64)
brand_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 68" fill="none">
  <!-- Group: Helmet Icon at x=0, y=2 -->
  <g transform="translate(0, 0) scale(0.68)">
""" + helmet_symbol_svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">', '').replace('</svg>', '') + """
  </g>
  
  <!-- Text Zégenheiro -->
  <g transform="translate(72, 0)">
    <text x="0" y="38" font-family="'Montserrat', 'Inter', 'Segoe UI', sans-serif" font-weight="800" font-size="31" letter-spacing="-0.5">
      <tspan fill="#FFFFFF">Zé</tspan><tspan fill="#EF4444">genheiro</tspan>
    </text>
    
    <!-- Subtitle / Tagline -->
    <text x="1" y="54" font-family="'Inter', 'Segoe UI', sans-serif" font-weight="600" font-size="8.8" fill="#94A3B8" letter-spacing="1.8">
      ENGENHARIA DE SEGURANÇA &amp; INCÊNDIO
    </text>
    
    <!-- Accent Line -->
    <rect x="1" y="60" width="46" height="2.5" rx="1.2" fill="#DC2626" />
    <rect x="50" y="60" width="16" height="2.5" rx="1.2" fill="#F59E0B" />
  </g>
</svg>"""

with open(os.path.join(target_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(brand_logo_svg)

# 4. White / High-Contrast Logo for Footer or Dark Surfaces
brand_logo_white = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 68" fill="none">
  <!-- Group: Helmet Icon at x=0, y=2 -->
  <g transform="translate(0, 0) scale(0.68)">
""" + helmet_symbol_svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">', '').replace('</svg>', '') + """
  </g>
  
  <!-- Text Zégenheiro -->
  <g transform="translate(72, 0)">
    <text x="0" y="38" font-family="'Montserrat', 'Inter', 'Segoe UI', sans-serif" font-weight="800" font-size="31" letter-spacing="-0.5">
      <tspan fill="#FFFFFF">Zé</tspan><tspan fill="#F87171">genheiro</tspan>
    </text>
    
    <!-- Subtitle / Tagline -->
    <text x="1" y="54" font-family="'Inter', 'Segoe UI', sans-serif" font-weight="600" font-size="8.8" fill="#CBD5E1" letter-spacing="1.8">
      ENGENHARIA DE SEGURANÇA &amp; INCÊNDIO
    </text>
    
    <!-- Accent Line -->
    <rect x="1" y="60" width="46" height="2.5" rx="1.2" fill="#EF4444" />
    <rect x="50" y="60" width="16" height="2.5" rx="1.2" fill="#FBBF24" />
  </g>
</svg>"""

with open(os.path.join(target_dir, "logo-white.svg"), "w", encoding="utf-8") as f:
    f.write(brand_logo_white)

print("Brand Logos created successfully!")

