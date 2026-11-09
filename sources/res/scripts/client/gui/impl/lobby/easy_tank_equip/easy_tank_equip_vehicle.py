# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_vehicle.py


class _EasyTankEquipCopyVehicle(object):
    __slots__ = ('__vehicle', )

    def __init__(self):
        super(_EasyTankEquipCopyVehicle, self).__init__()
        self.__vehicle = None
        return

    def setVehicle(self, value):
        self.__vehicle = value

    @property
    def item(self):
        return self.__vehicle

    def isPresent(self):
        return self.__vehicle is not None

    def clear(self):
        self.__vehicle = None
        return


g_easyTankEquipCopyVehicle = _EasyTankEquipCopyVehicle()
