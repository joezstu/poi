from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def import_excel(request):
    return HttpResponse(9889)
