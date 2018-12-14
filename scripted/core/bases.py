"""Entry point of framework."""
from scripted.core.helpers import Helpers


class BaseClass(object):
__all__ = ['Controller', 'View']


    """Base class of all Scripted classes."""

    fn = Helpers()

    def __str__(self):
        return self.__class__.__name__


class ControllerBaseClass(BaseClass):
    """Base class of all user defined controllers."""
    pass
