import requests
from pathlib import Path

token = Path("~/.config/github_token").expanduser().read_text().strip()

response = requests.get(
    "https://api.github.com/user/repos",
    headers={"Authorization": f"Bearer {token}"},
    params={"per_page": 5, "sort": "updated"},
    timeout=10,
)
response.raise_for_status()

for r in response.json():
    print(f"{r['name']}: {r['description'] or '-'}")
