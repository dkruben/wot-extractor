# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/components/gun_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/gun_components.py
from __future__ import absolute_import
from typing import TYPE_CHECKING, Tuple
from items.components import legacy_stuff
from py2to3.patched_future import with_metaclass
from soft_exception import SoftException
from wrapped_reflection_framework import reflectedNamedTuple
from wrapped_reflection_framework import ReflectionMetaclass
if TYPE_CHECKING:
    from items.vehicle_items import Shell
RecoilEffect = reflectedNamedTuple('RecoilEffect', ('lodDist', 'amplitude', 'backoffTime',
                                                    'returnTime'))

class GunShot(with_metaclass(ReflectionMetaclass, legacy_stuff.LegacyStuff)):
    __slots__ = ('shell', 'defaultPortion', 'piercingPower', 'speed', 'gravity', 'nominalMaxDistance',
                 'maxDistance', 'maxHeight')

    def __init__(self, shell, defaultPortion, piercingPower, speed, gravity, maxDistance, maxHeight):
        super(GunShot, self).__init__()
        self.shell = shell
        self.defaultPortion = defaultPortion
        self.piercingPower = piercingPower
        self.speed = speed
        self.gravity = gravity
        self.nominalMaxDistance = maxDistance
        self.maxDistance = maxDistance
        self.maxHeight = maxHeight

    def __repr__(self):
        return ('GunShot(shell = {}, ppower = {}, speed = {}, gravity = {}, nominalMaxDistance - {}, maxDistance = {}, maxHeight = {}))').format(self.shell, self.piercingPower, self.speed, self.gravity, self.nominalMaxDistance, self.maxDistance, self.maxHeight)

    def copy(self):
        raise SoftException('Operation "GunShot.copy" is not allowed')
