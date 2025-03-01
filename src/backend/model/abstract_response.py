from http import HTTPStatus
from pydantic import BaseModel


class AbstractResponse:

    message: str = "Success"
    status_code: HTTPStatus = HTTPStatus.OK
