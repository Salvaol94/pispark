import math
from unittest import TestCase

from EstimatePi import estimar_pi


class Test(TestCase):

    def test_estimar_pi(self):
        estimacion_de_pi=estimar_pi(1000000)
        self.assertAlmostEqual(estimacion_de_pi, math.pi, 2)

