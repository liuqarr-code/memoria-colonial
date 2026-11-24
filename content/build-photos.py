from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent
photos=json.loads((r/'content/photos-metadata.json').read_text())
assert set(photos)==set(map(str,range(10)))
public={id:{k:v for k,v in p.items() if k in ['src','page','author','license','licenseUrl','date']} for id,p in photos.items()}
for p in public.values():
 assert (r/'dist'/p['src']).is_file(),p['src']
 assert p['license'] and p['author'] and p['licenseUrl']
(r/'dist/photos.js').write_text('const PHOTOS='+json.dumps(public,ensure_ascii=False)+';\n')
print('Validated ten photograph assets and credits')
