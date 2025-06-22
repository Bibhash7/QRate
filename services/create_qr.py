import os
import qrcode
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def create_qr_image(full_url, qr_filename):
    try:
        qr_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', qr_filename)
        os.makedirs(os.path.dirname(qr_path), exist_ok=True)
        img = qrcode.make(full_url)
        img.save(qr_path)
        return qr_path
    except Exception as e:
        logger.error("Error creating qr image")
