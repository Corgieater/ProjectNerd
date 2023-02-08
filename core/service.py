from rest_framework.response import Response
from rest_framework import status


class APIResponse(Response):
    def __init__(self, data=None, success=True, status=status.HTTP_200_OK, error=None,
                 headers=None, content_type=None):
        if error:
            super().__init__(data={'success': success, 'error': error},
                             status=status, headers=headers,
                             content_type=content_type)
        else:
            super().__init__(data={'success': success, 'data': data},
                             status=status, headers=headers,
                             content_type=content_type)


