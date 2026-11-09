# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/kill_cam_mode_helpers/kill_cam_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/kill_cam_mode_helpers/kill_cam_helpers.py
from __future__ import absolute_import
import Math
from projectile_trajectory import computeProjectileTrajectoryWithEnd
_SHELL_TRAJECTORY_EPSILON_CAMERA = 0.03

def calculateSPGTrajectory(start, end, velocity, gravity):
    points = computeProjectileTrajectoryWithEnd(start, end, velocity, gravity, _SHELL_TRAJECTORY_EPSILON_CAMERA)
    points.insert(0, start)
    return points


def getMiddlePointWithOffset(points, direction, offset):
    middlePoint = (points[-1] - points[0]) / 2.0
    offsetVector = Math.Vector3(middlePoint)
    offsetVector.normalise()
    offsetVector = offsetVector * Math.Vector3(0.0, direction, 0.0)
    middlePoint += offsetVector * offset
    middlePoint += points[0]
    return middlePoint
