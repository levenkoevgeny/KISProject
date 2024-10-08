from applogging.models import LogData
from django.contrib.auth.models import User

METHODS = ['POST', 'PUT', 'DELETE']
UNTRACKED_URLS = ['/admin/login']


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in METHODS:
            user = request.user if isinstance(request.user, User) else None
            # LogData.objects.create(user=user, request_method=request.method, request_body=request.body,
            #                        request_path=request.path)

        response = self.get_response(request)
        return response
