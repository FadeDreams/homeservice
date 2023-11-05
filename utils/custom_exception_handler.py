from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    # print(exception_handler)
    if response is not None:
        response.data['status_code'] = response.status_code

    if exception_class == 'AuthenticationFailed':
        response.data['detail'] = 'Please provide valid credentials.'

    if exception_class == 'NotAuthenticated':
        response.data['detail'] = 'Authentication credentials were not provided.'

    if exception_class == 'PermissionDenied':
        response.data['detail'] = 'You do not have permission to perform this action.'

    if exception_class == 'NotFound':
        response.data['detail'] = 'Not found.'

    if exception_class == 'MethodNotAllowed':
        response.data['detail'] = 'Method not allowed.'

    if exception_class == 'ValidationError':
        response.data['detail'] = 'Bad request.'

    if exception_class == 'ParseError':
        response.data['detail'] = 'Malformed request.'

    if exception_class == 'UnsupportedMediaType':
        response.data['detail'] = 'Unsupported media type.'

    if exception_class == 'Throttled':
        response.data['detail'] = 'Request was throttled.'

    return response


