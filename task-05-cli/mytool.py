import click
import json
from pathlib import Path

DEFAULT_DB = Path("~/.mytool/servers.json").expanduser()


def load_db() -> list[dict]:
    if not DEFAULT_DB.exists():
        return []
    return json.loads(DEFAULT_DB.read_text())


def save_db(servers: list[dict]) -> None:
    DEFAULT_DB.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_DB.write_text(json.dumps(servers, indent=2, ensure_ascii=False))


@click.group()
def cli():
    """Mytool — управление списком серверов."""
    pass


@cli.command()
def list():
    """Показать все серверы."""
    servers = load_db()
    if not servers:
        click.echo("Пусто. Добавь через `mytool add`.")
        return
    for s in servers:
        click.echo(f"  {s['name']:<15} {s['ip']:<15} :{s['port']}")


@cli.command()
@click.argument("name")
@click.option("--ip", required=True, help="IP-адрес сервера")
@click.option("--port", default=22, type=int, show_default=True, help="Порт")
def add(name: str, ip: str, port: int):
    """Добавить сервер."""
    servers = load_db()
    if any(s["name"] == name for s in servers):
        click.echo(f"Сервер '{name}' уже есть", err=True)
        raise click.Abort()
    servers.append({"name": name, "ip": ip, "port": port})
    save_db(servers)
    click.echo(f"Добавлен {name} ({ip}:{port})")


@cli.command()
@click.argument("name")
@click.confirmation_option(prompt="Точно удалить?")
def delete(name: str):
    """Удалить сервер."""
    servers = load_db()
    new_servers = [s for s in servers if s["name"] != name]
    if len(new_servers) == len(servers):
        click.echo(f"Сервер '{name}' не найден", err=True)
        raise click.Abort()
    save_db(new_servers)
    click.echo(f"Удалён {name}")


@cli.command()
@click.argument("name")
def ping(name: str):
    """Пингануть сервер."""
    import subprocess
    servers = load_db()
    server = next((s for s in servers if s["name"] == name), None)
    if not server:
        click.echo(f"Не найден: {name}", err=True)
        raise click.Abort()
    result = subprocess.run(
        ["ping", "-c", "3", server["ip"]],
        capture_output=True,
        text=True,
    )
    click.echo(result.stdout)
    if result.returncode != 0:
        click.echo(result.stderr, err=True)


if __name__ == "__main__":
    cli()
