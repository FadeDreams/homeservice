from django.http import JsonResponse

def error_400(request, exception):
    return JsonResponse({
        'error': 'Bad Request',
        'status': 400
    }, status=400)

def error_403(request, exception):
    return JsonResponse({
        'error': 'Forbidden',
        'status': 403
    }, status=403)

def error_404(request, exception):
    return JsonResponse({
        'error': 'Not Found',
        'status': 404
    }, status=404)

def error_500(request):
    return JsonResponse({
        'error': 'Internal Server Error',
        'status': 500
    }, status=500)


