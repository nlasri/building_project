import unittest

from visualisation import *

class Visualisation1Test(unittest.TestCase):
    building = np.array([[[0, 0, 4, 4], [5, 0, 4, 4]],[[0, 4, 4, 4], [5, 4, 4, 4]]])
    couloir = np.array([[[4, 0, 1, 8]]])
    longueur = building[0][-1][0] + building[0][-1][2]
    largeur = building[-1][-1][1] + building[0][-1][3]
    design_building = np.zeros((largeur, longueur))

    placer_room(building, design_building, 1)
    placer_room(couloir, design_building, 2)

    def test_visualisation1(self):
        expected_building = np.array([[1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.],
                                [1., 1., 1., 1., 2., 1., 1., 1., 1.]])
        self.assertTrue((design_building == expected_building).all())


if __name__ == '__main__':
    unittest.main()
