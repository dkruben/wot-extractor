# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_vehicle.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class _PostProgressionVehicle(object):
    __slots__ = ('__customVehicle', '__defaultVehicle', '__diffVehicle')

    def __init__(self):
        super(_PostProgressionVehicle, self).__init__()
        self.__customVehicle = None
        self.__defaultVehicle = None
        self.__diffVehicle = None
        return

    def setCustomVehicle(self, value):
        self.__customVehicle = value

    def setDefaultVehicle(self, value):
        self.__defaultVehicle = value

    def setDiffVehicle(self, value):
        self.__diffVehicle = value

    @property
    def defaultItem(self):
        return self.__defaultVehicle

    @property
    def diffItem(self):
        result = self.__diffVehicle or self.__defaultVehicle
        self.__diffVehicle = None
        return result

    @property
    def item(self):
        return self.__customVehicle or self.__defaultVehicle

    def isPresent(self):
        return self.item is not None

    def clear(self):
        self.__customVehicle = None
        self.__defaultVehicle = None
        self.__diffVehicle = None
        return


g_postProgressionVehicle = _PostProgressionVehicle()
