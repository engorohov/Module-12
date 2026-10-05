import json
from pathlib import Path


def load_servers(path: Path) -> list[dict]:
    """Загрузить список серверов из JSON."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_servers(path: Path, servers: list[dict]) -> None:
    """Сохранить с красивым форматированием."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(servers, f, indent=2, ensure_ascii=False)


def main():
    path = Path("servers.json")
    servers = load_servers(path)
    print(f"Всего серверов: {len(servers)}")

    by_tag = {}
    for s in servers:
        for tag in s["tags"]:
            by_tag.setdefault(tag, []).append(s["name"])

    print("\nПо тегам:")
    for tag, names in by_tag.items():
        print(f"  {tag}: {', '.join(names)}")

    servers.append({
        "name": "monitor-1",
        "ip": "10.0.2.1",
        "port": 9090,
        "tags": ["monitoring"],
    })
    save_servers(Path("servers-updated.json"), servers)
    print("\nСохранено в servers-updated.json")


if __name__ == "__main__":
    main()
