from pathlib import Path
import hashlib,json,csv
from PIL import Image
from jsonschema import validate
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'exercises.json').read_text()); schema=json.loads((root/'schema/exercises.schema.json').read_text());validate(data,schema)
manifest=json.loads((root/'qa/image-manifest.json').read_text()); ids=set(); hashes=set(); pixels=set(); paths=set(); webps=set()
for ex in data['exercises']:
    eid=ex['id']; assert eid not in ids; ids.add(eid)
    assert ex['frame_order']==['a','b','c']
    assert json.loads((root/'exercise'/eid/'index.json').read_text())==ex
    for phase in 'abc':
        m=manifest[eid][phase]
        for key,typ,seen in [('original','png',paths),('ownpace','webp',webps)]:
            rel=ex['images'][key][phase];assert rel==m[typ] and rel not in seen;seen.add(rel)
            p=root/rel;assert p.is_file() and p.resolve().is_relative_to(root)
            with Image.open(p) as im:
                im.load();assert im.size==(512,512) and im.format==typ.upper()
                if typ=='png':
                    h=hashlib.sha256(p.read_bytes()).hexdigest(); ph=hashlib.sha256(im.convert('RGB').tobytes()).hexdigest()
                    assert h==m['sha256'] and h not in hashes;hashes.add(h)
                    assert ph==m['pixel_sha256'] and ph not in pixels;pixels.add(ph)
assert ids==set(manifest) and len(ids)==data['count']
assert len(paths)==len(webps)==data['frame_count']==3*len(ids)
assert paths=={str(p.relative_to(root)) for p in (root/'images/original').glob('*.png')}
assert webps=={str(p.relative_to(root)) for p in (root/'images/webp').glob('*.webp')}
with (root/'exercises.csv').open() as f: assert {r['id'] for r in csv.DictReader(f)}==ids
js=(root/'assets/catalog.js').read_text().strip();assert json.loads(js.removeprefix('window.OWNPACE_DATA = ').removesuffix(';'))==data
print(f'PASS: {len(ids)} exercises, {len(paths)} original PNGs, {len(webps)} WebPs; schema, paths, exports and original hashes verified.')
print('Biomechanics and rights are NOT certified by this script.')
