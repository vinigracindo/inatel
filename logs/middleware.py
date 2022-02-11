import time

from django.http import RawPostDataException

from logs.models import Log
from logs.utils import get_client_ip


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Calculated execution time.
        _t = time.time()
        # Get response from view function.
        response = self.get_response(request)
        _t = int((time.time() - _t)*1000)

        # Create instance of our model and assign values
        try:
            body = str(request.body)
        except RawPostDataException:
            body = ''

        request_log = Log(
            endpoint=request.get_full_path(),
            response_code=response.status_code,
            method=request.method,
            remote_address=get_client_ip(request),
            exec_time=_t,
            body_response=str(response.content),
            body_request=str(body)
        )

        # Assign user to log if it's not an anonymous user
        if not request.user.is_anonymous:
            request_log.user_id = request.user.pk

        # Save log in db
        request_log.save(using='logs')
        return response
