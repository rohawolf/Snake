class SnakeExc:
    """Exception Parent Class for all Snake Exceptions"""

    class CollideItself(Exception):
        """This Exception Class represents when Snake collides itself"""
        pass

    class OutOfBoundary(Exception):
        """This Exception Class represents when Snake goes outside of Game Board Boundary"""
        pass
