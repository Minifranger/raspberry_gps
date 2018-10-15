import logging.handlers
import properties

MODE = "a"
MAX_BYTES = 200 * 1024 * 1024
BACKUP = 12

formatter = logging.Formatter("%(asctime)s %(message)s")

handler = logging.handlers.RotatingFileHandler(properties.GPS_DATA, mode=MODE, maxBytes=MAX_BYTES, backupCount=BACKUP)
handler.setFormatter(formatter)

gps_data = logging.getLogger("gps_data")
gps_data.setLevel(logging.INFO)
gps_data.addHandler(handler)
