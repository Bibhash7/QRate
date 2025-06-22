from qrateApp.models import CodeSnippet
import logging

logger = logging.getLogger(__name__)

def clear_db_objects():
    try:
        snippet_object = CodeSnippet.objects.all()
        if snippet_object.count() >= 100:
            snippet_object.delete()
            logger.info("DB cleanup successful.")
    except Exception as e:
        logger.error("Error in DB")


