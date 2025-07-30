import logging
import uuid
from verificationapp.models import MiddelwareRequestID

logger = logging.getLogger('verificationapp.middleware')  


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.request_id = str(uuid.uuid4())

        logger.info(
            f"Incoming request {request.method} {request.path} - Request ID: {request.request_id}"
        )

        response = self.get_response(request)

        response["X-Request-ID"] = request.request_id

        MiddelwareRequestID.objects.create(
        request_id=request.request_id,
        path=request.path,
        method=request.method,
        status_code =response.status_code
    )

        logger.info(
            f"Response status: {response.status_code} - Request ID: {request.request_id}"
        )
        return response
