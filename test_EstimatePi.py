import math
from unittest import TestCase

from EstimatePi import estimar_pi, estimar_pi_bloques


class Test(TestCase):

    def test_estimar_pi(self):
        estimacion_de_pi=estimar_pi(1000000)
        self.assertAlmostEqual(estimacion_de_pi, math.pi, 2)


    def test_estimar_pi_bloques(self):
        estimacion_de_pi=estimar_pi_bloques(1000000,4)
        self.assertAlmostEqual(estimacion_de_pi, math.pi, 2)