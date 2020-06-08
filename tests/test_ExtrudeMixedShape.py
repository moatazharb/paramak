"""
This file is part of PARAMAK which is a design tool capable
of creating 3D CAD models compatible with automated neutronics
analysis.

PARAMAK is released under GNU General Public License v3.0.
Go to https://github.com/Shimwell/paramak/blob/master/LICENSE
for full license details.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Copyright (C) 2019  UKAEA

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
"""

import unittest

import pytest

from paramak import ExtrudeMixedShape


class test_object_properties(unittest.TestCase):
    def test_absolute_shape_volume(self):
        """creates an extruded shape with one placement angle using straight \
                and spline connections and checks the volume is correct"""

        test_shape = ExtrudeMixedShape(
            points=[
                (0, 0, "straight"),
                (0, 20, "straight"),
                (20, 20, "spline"),
                (20, 0, "spline"),
                (0, 0),
            ],
            distance=30,
        )

        test_shape.create_solid()

        assert test_shape.solid is not None
        assert test_shape.volume > 20 * 20 * 30

    def test_extruded_shape_relative_volume(self):
        """creates two extruded shapes with different placement angles using \
                straight and spline connections and checks their relative \
                volumes are correct"""

        test_shape_1 = ExtrudeMixedShape(
            points=[
                (5, 0, "straight"),
                (5, 20, "straight"),
                (10, 20, "spline"),
                (20, 10, "spline"),
                (10, 0, "straight"),
                (5, 0),
            ],
            distance=10,
        )

        test_shape_1.azimuth_placement_angle = 0

        # test_shape_2 is test_shape_1 extruded 4 times

        test_shape_2 = ExtrudeMixedShape(
            points=[
                (5, 0, "straight"),
                (5, 20, "straight"),
                (10, 20, "spline"),
                (20, 10, "spline"),
                (10, 0, "straight"),
                (5, 0),
            ],
            distance=10,
        )
        test_shape_2.azimuth_placement_angle = [0, 90, 180, 270]

        assert test_shape_1.volume * 4 == pytest.approx(test_shape_2.volume)

    def test_cut_volume(self):
        """creates an extruded shape with one placement angle using straight and \
                spline connections with another shape cut out and checks the \
                volume is correct"""

        inner_shape = ExtrudeMixedShape(
            points=[
                (5, 5, "straight"),
                (5, 10, "spline"),
                (10, 10, "spline"),
                (10, 5, "spline"),
                (5, 5),
            ],
            distance=30,
        )

        outer_shape = ExtrudeMixedShape(
            points=[
                (3, 3, "straight"),
                (3, 12, "spline"),
                (12, 12, "spline"),
                (12, 3, "spline"),
                (3, 3),
            ],
            distance=30,
        )

        outer_shape_with_cut = ExtrudeMixedShape(
            points=[
                (3, 3, "straight"),
                (3, 12, "spline"),
                (12, 12, "spline"),
                (12, 3, "spline"),
                (3, 3),
            ],
            cut=inner_shape,
            distance=30,
        )

        assert inner_shape.volume == pytest.approx(1068.75)
        assert outer_shape.volume == pytest.approx(3462.75)
        assert outer_shape_with_cut.volume == pytest.approx(3462.75 - 1068.75, abs=0.1)


if __name__ == "__main__":
    unittest.main()