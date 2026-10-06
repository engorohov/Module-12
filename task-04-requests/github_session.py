import requests

session = requests.Session()
session.headers.update({"User-Agent": "my-cli/1.0"})

for user in ["engorohov", "kelseyhightower", "stefanprodan"]:
    r = session.get(f"https://api.github.com/users/{user}", timeout=10)
    r.raise_for_status()
    print(r.json()["name"])