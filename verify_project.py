with open(r'C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert '5512997683642' in html, 'WhatsApp number missing in index.html'
assert 'José Luis' in html, 'Eng. José Luis missing in index.html'
assert 'PPCI' in html, 'PPCI missing in index.html'
assert 'AVCB' in html, 'AVCB missing in index.html'
assert 'assets/logo-symbol.svg' in html, 'Logo symbol missing in index.html'
assert 'Zégenheiro' in html or 'Zé<span class="red-accent">genheiro</span>' in html, 'Brand typography missing in index.html'
assert 'marqueeTrack' in html, 'Marquee track missing in index.html'

with open(r'C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

assert 'rgba(10, 15, 26, 0.78)' in css, 'Opacity overlay missing in styles.css'
assert 'blueprint-background' in css, 'Blueprint background missing in styles.css'

with open(r'C:\Users\firef\.gemini\antigravity\scratch\zegenheiro-landing-page\js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

assert '5512997683642' in js, 'WhatsApp number missing in js'

print('All validation assertions passed 100% successfully!')

