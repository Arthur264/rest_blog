from rest_framework.response import Response


def ResponseHandler(data=None, error=None, statusCode=200):
    result = {}
    result['data'] = dict(data) if data is not None else {}
    result['error'] = error if error is not None else False
    result['status'] = error == None
    return Response(result, status=statusCode)
