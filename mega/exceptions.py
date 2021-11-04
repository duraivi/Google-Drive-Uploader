# -*- coding: utf-8 -*-


class MegaException(Exception):
    pass
    
class MegaIncorrectPasswordExcetion(MegaException):
    """
    A correct password or email was given.
    """

class MegaRequestException(MegaException):
    """
    There was an download in the request.
    """
    pass
