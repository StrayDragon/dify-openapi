# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
from ..types.error import Error


class ConflictError(ApiError):
    def __init__(self, body: Error):
        super().__init__(status_code=409, body=body)
