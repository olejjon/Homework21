
class BaseError(Exception):
    message = NotImplemented

class RequestError(BaseError):
    message = NotImplemented

class LogisticError(BaseError):
    message = NotImplemented

class NotEnoughSpace(LogisticError):
    message = "Недостаточно места на складе"

class NotEnoughItem(LogisticError):
    message = "Недостаточно товара на складе"

class UnknownItem(LogisticError):
    message = "Неизвестный товар"

class TooManyDifferentItems(LogisticError):
    message = "Слишком много разных товаров"

class InvalidRequest(RequestError):
    message = "Кривой запрос"

class InvalidStorageName(RequestError):
    message = "Неправильное имя склада"