from pathlib import Path
import json,subprocess,sys
root=Path(__file__).resolve().parent
source=json.loads((root/'content/source-es.json').read_text())
assert len(source['records'])==10
(root/'dist/data-es.json').write_text(json.dumps(source,ensure_ascii=False))
for script in ['translate-ca.py','build-ui.py','build-photos.py']:
 subprocess.run([sys.executable,str(root/'content'/script)],check=True,cwd=root)
for lang in ['es','ca']:
 data=json.loads((root/f'dist/data-{lang}.json').read_text())
 assert len(data['records'])==10
 assert [len(r['paragraphs']) for r in data['records']]==[len(r['paragraphs']) for r in source['records']]
print('Validated both languages and all ten records')
