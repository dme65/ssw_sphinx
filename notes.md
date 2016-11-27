1. Install Sphinx with pip
2. Run sphinx-quickstart
3. Walk through the different options
4. Compile the documentation and show that it's empty and boring
5. Add a caption and add a source_code file to the toctree
6. Fill out the source_code file:
    ```rst
    Source code
    ===========

    ssw_sphinx module
    -----------------

    .. autoclass:: ssw_sphinx.MyCoolClass
        :members:
    ```
7. Compile again and show that the module and the Class is showing up
8. Fill out some class documentation
    ```python  
    """
    .. module:: ssw_sphinx
       :synopsis: A pretty useless class

    .. moduleauthor:: David Eriksson <dme65@cornell.edu>

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
    ```
9. This theme is pretty ugly, so show them how to switch html theme to sphinx_rtd_theme.
10. Show them how to add another section
