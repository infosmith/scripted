"""Entry point of framework."""
from scripted.core.helpers import Helpers


__all__ = ['Controller', 'View']


class Base(object):
    """Base class of all Scripted classes."""

    fn = Helpers()

    def __str__(self):
        return self.__class__.__name__


class Controller(Base):
    """Base class of all user defined controllers."""
    pass
