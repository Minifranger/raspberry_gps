import logging.handlers
import properties

mode = "a"
max_bytes = 200 * 1024 * 1024
backup = 1

formatter = logging.Formatter("%(asctime)s %(message)s")

handler = logging.handlers.RotatingFileHandler(properties.LOGS, mode=mode, maxBytes=max_bytes, backupCount=backup)
handler.setFormatter(formatter)

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
