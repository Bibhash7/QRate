import os
import time
import logging
logger = logging.getLogger(__name__)

def delete_qr_image(qr_path):
    try:
        time.sleep(20)
        if os.path.exists(qr_path):
            os.remove(qr_path)
    except Exception as e:
        logger.error("Error deleting qr code")

