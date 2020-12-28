class BaseSnakeException(Exception):
    """Base Snake Exception Class"""
    pass


class SnakeCollideItselfException(BaseSnakeException):
    """This Exception Class represents when Snake collides itself"""
    pass


class SnakeOutOfBoundaryException(BaseSnakeException):
    """This Exception Class represents when Snake goes outside of Game Board Boundary"""
    pass
