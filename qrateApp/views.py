import uuid
import threading
import logging
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from services.delete_qr import delete_qr_image
from services.create_qr import create_qr_image
from services.clear_db import clear_db_objects
from .constants import BASE_URL
from .models import CodeSnippet


logger = logging.getLogger(__name__)

def home(request):
    """
    Home view of Qrate.
    :param request: HttpResquest, conatins pasted code
    :return: Renders html page
    """
    try:
        if request.method == 'POST':
            clear_db_objects()
            code = request.POST.get('code')
            if not code.strip():
                return render(request, 'qrateApp/home.html', {'error': 'Please enter some code.'})

            snippet = CodeSnippet.objects.create(code=code)
            full_url = f"{BASE_URL}/{snippet.slug}/"
            qr_filename = f'{uuid.uuid4().hex}.png'

            qr_path = create_qr_image(full_url, qr_filename)

            delete_thread = threading.Thread(target=delete_qr_image, args=(qr_path,))
            delete_thread.daemon = True
            delete_thread.start()

            return render(request, 'qrateApp/home.html', {
                'qr_url': settings.MEDIA_URL + 'qrcodes/' + qr_filename,
                'full_url': full_url,
            })

        return render(request, 'qrateApp/home.html')

    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="qrateApp/internal_server_error.html",
            status=500
        )

def handle_unknown_routes(request):
    """
    API to handle unknown routes.
    :param request:
    :return render template:
    """
    try:
        return render(
            request,
            template_name="qrateApp/unknown_routes.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="qrateApp/internal_server_error.html",
            status=500
        )
def view_code(request, slug):
    """
    View the copied code.
    :param request: HttpResquest,
    :param slug: Str, The slug
    :return: Render_template that renders the template.
    """
    try:
        snippet = get_object_or_404(CodeSnippet, slug=slug)
        return render(request, 'qrateApp/view_code.html', {'code': snippet.code})

    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="qrateApp/internal_server_error.html",
            status=500
        )
