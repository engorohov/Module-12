import logging
from pythonjsonlogger import jsonlogger

handler = logging.StreamHandler()
handler.setFormatter(
    jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
)

log = logging.getLogger()
log.addHandler(handler)
log.setLevel(logging.INFO)

log.info("user logged in", extra={"user_id": 42, "ip": "10.0.0.1"})