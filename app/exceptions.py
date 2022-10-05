class BaseServiceError(Exception):
    code = 500


class BadRequest(BaseServiceError):
    code = 400


class NotAuthorized(BaseServiceError):
    code = 401


class ItemNotFound(BaseServiceError):
    code = 404
