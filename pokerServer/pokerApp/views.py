from django.http import JsonResponse
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

@renderer_classes(JSONRenderer)
def get_settings(request):
    return JsonResponse({})
