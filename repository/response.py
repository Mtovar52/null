from starlette import status
from fastapi import Response
import json

class Response():

    '''def exception_error(e):
        try:
            raise e
        except Exception as e:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            error_message = "Error saving book: " + str(e)

        data = {"message": error_message, "is_ok": False, "status_code": status_code}
        return Response(status_code=status_code, content=json.dumps(data), media_type="application/json")'''

    def  response_book(self, data):
        return Response(status_code=200, content=json.dumps(data), media_type="application/json")
