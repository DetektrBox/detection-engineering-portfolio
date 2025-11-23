# automation/enrich_mitre.py
import yaml, os, sys

for root, _, files in os.walk("sigma"):
    for f in files:
        if f.endswith(".yml"):
            path = os.path.join(root, f)
            with open(path) as fd:
                data = yaml.safe_load(fd)
            if 'tags' not in data:
                data['tags'] = []
            if not any(t.startswith("attack.t") for t in data['tags']):
                data['tags'].append("attack.txxxx")  # placeholder
                with open(path, "w") as fd:
                    yaml.dump(data, fd, sort_keys=False)
                print(f"Enriched {path}")