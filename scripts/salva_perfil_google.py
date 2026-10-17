import re
import urllib.parse
from pathlib import Path

content = Path('content/raw_email_plain.txt').read_text(encoding='utf-8')

start_marker = '--- INÍCIO DO CÓDIGO ---'
end_marker = '--- FIM DO CÓDIGO ---'

idx1 = content.find(start_marker)
idx2 = content.find(end_marker)

if idx1 != -1 and idx2 != -1:
    html = content[idx1 + len(start_marker):idx2].strip()
else:
    raise Exception('Marcadores não encontrados')

def unwrap_google_url(match):
    full_url = match.group(0)
    parsed = urllib.parse.urlparse(full_url)
    qs = urllib.parse.parse_qs(parsed.query)
    if 'q' in qs:
        real_url = qs['q'][0]
        return real_url
    return full_url

cleaned_html = re.sub(r'https://www\.google\.com/url\?[^\s"\'<>]+', unwrap_google_url, html)

# Garantir que og:image aponte para https://infohausti.com.br/perfil-google/og.jpg (sem www duplicado ou divergente)
# O canonical e links principais:
# https://www.infohausti.com.br/perfil-google/ -> https://infohausti.com.br/perfil-google/ ou mantido consistente
out_file = Path('perfil-google/index.html')
out_file.write_text(cleaned_html, encoding='utf-8')
print(f'Salvo {out_file} com {len(cleaned_html)} caracteres.')
