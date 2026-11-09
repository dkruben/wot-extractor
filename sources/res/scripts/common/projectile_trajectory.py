# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/projectile_trajectory.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/projectile_trajectory.py
from __future__ import absolute_import, division
import BigWorld, Math

def computeProjectileTrajectory(beginPoint, velocity, gravity, time, epsilon):
    endPoint = beginPoint + velocity.scale(time) + gravity.scale(time * time * 0.5)
    return computeProjectileTrajectoryWithEnd(beginPoint, endPoint, velocity, gravity, epsilon)


def computeProjectileTrajectoryWithEnd(beginPoint, endPoint, velocity, gravity, epsilon):
    checkPoints = []
    stack = [
     (
      velocity, beginPoint, endPoint)]
    while len(stack) > 0:
        lastIdx = len(stack) - 1
        v1, p1, p2 = stack[lastIdx]
        del stack[lastIdx]
        delta = p2 - p1
        xzNormal = Math.Vector3(-delta.z, 0.0, delta.x)
        normal = xzNormal * delta
        if abs(normal.y) < epsilon:
            checkPoints.append(p2)
            continue
        normal.normalise()
        extremeTime = normal.dot(v1) / (-gravity.y * normal.y)
        extremePoint = v1.scale(extremeTime) + gravity.scale(extremeTime * extremeTime * 0.5)
        dist = abs(normal.dot(extremePoint))
        if dist > epsilon:
            extremeVelocity = v1 + gravity.scale(extremeTime)
            stack.append((extremeVelocity, p1 + extremePoint, p2))
            stack.append((v1, p1, p1 + extremePoint))
        else:
            checkPoints.append(p2)

    return checkPoints


try:
    computeProjectileTrajectory = BigWorld.wg_computeProjectileTrajectory
    computeProjectileTrajectoryWithEnd = BigWorld.wg_computeProjectileTrajectoryWithEnd
except AttributeError:
    pass

def getShotAngles(vehTypeDescr, vehMatrix, point, overrideGunPosition=None, overrideShotDescr=None):
    shot = overrideShotDescr or vehTypeDescr.shot
    return BigWorld.getAimingAngles(point, vehMatrix, vehTypeDescr.chassis.hullPosition + vehTypeDescr.hull.turretPositions[0], vehTypeDescr.activeGunShotPosition if overrideGunPosition is None else overrideGunPosition, shot.speed, shot.gravity)
