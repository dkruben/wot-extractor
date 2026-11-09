# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/HasVehicleList.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/HasVehicleList.py
from __future__ import absolute_import
from collections import namedtuple
from gui import nationSortKeyByIndex
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class HasVehiclesList(object):
    _LIST_NAME = 'vehicles'
    VehicleData = namedtuple('VehicleData', 'name nation level type icon innationID')
    itemsCache = dependency.descriptor(IItemsCache)

    def getVehiclesData(self):
        result = []
        for vCD in self._getVehiclesDescrsList():
            vehicle = self.itemsCache.items.getItemByCD(vCD)
            result.append(self.VehicleData(vehicle.userName, vehicle.nationID, vehicle.level, vehicle.type, vehicle.iconSmall, vehicle.innationID))

        return [i._asdict() for i in sorted(result, key=self._sortKey)]

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    def _getVehiclesDescrsList(self):
        raise NotImplementedError

    def hasVehiclesList(self):
        return True

    @classmethod
    def _sortKey(cls, v):
        return (v.level, nationSortKeyByIndex(v.nation))
