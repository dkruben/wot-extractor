# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_vehicle.py
from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class _TankSetupVehicle(object):
    __slots__ = ('__vehicle', )
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(_TankSetupVehicle, self).__init__()
        self.__vehicle = None
        return

    def setVehicle(self, value):
        self.__vehicle = value

    @property
    def item(self):
        return self.__vehicle or g_currentVehicle.item

    @property
    def defaultItem(self):
        if g_currentVehicle.isPresent():
            return g_currentVehicle.item
        else:
            return

    def isPresent(self):
        return self.__vehicle is not None

    def dispose(self):
        self.__vehicle = None
        return


g_tankSetupVehicle = _TankSetupVehicle()
