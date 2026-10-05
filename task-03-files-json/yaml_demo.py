import yaml
from pathlib import Path

data = {
    "version": 1,
    "servers": [
        {"name": "web-1", "port": 80},
        {"name": "db-1", "port": 5432},
    ],
}

with open("config.yaml", "w") as f:
    yaml.safe_dump(data, f, sort_keys=False)

with open("config.yaml", "r") as f:
    loaded = yaml.safe_load(f)

print(loaded)
