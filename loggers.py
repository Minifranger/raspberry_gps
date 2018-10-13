import logging.handlers

MODE = "a"
MAX_BYTES = 2 * 1024 * 1024
BACKUP = 1

formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")

handler = logging.handlers.RotatingFileHandler("gps_data.log", mode=MODE, maxBytes=MAX_BYTES, backupCount=BACKUP)
handler.setFormatter(formatter)

gps_data = logging.getLogger("gps_data")
gps_data.setLevel(logging.INFO)
gps_data.addHandler(handler)
