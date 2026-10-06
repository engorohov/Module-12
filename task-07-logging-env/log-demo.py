import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr,
)

log = logging.getLogger("myapp")


def do_work(user: str):
    log.debug("debug — обычно не видно")
    log.info(f"Старт работы для пользователя {user}")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        log.exception("Поделили на ноль!")
    log.warning("Закончили с ошибкой")


do_work("ivan")
