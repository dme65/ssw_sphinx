"""
:Module: ssw_sphinx
:Author: David Eriksson <dme65@cornell.edu>
"""

class Gravity:
    """
    This class knows how to handle gravity

    And here is a lot of more info .....

    :type v0: float
    :param v0: Initial velocity
    :type g: float
    :ivar g: Gravity constant

    .. note:: This class is completely useless

    .. warning:: Make sure you know how to handle gravity
    """

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def speed(self, t):
        """
        Computes the speed at time :math:`t`

        Computes the speed at time :math:`t` using the formula

        .. math::

            v(t) = v_0t - \\frac{gt^2}{2}

        :type t: float
        :param t: Time for which we want to compute the speed
        :rtype: float
        :return: Speed at time t

        .. todo:: Check that t is non-negative
        """

        return self.v0*t - 0.5*self.g*t**2
