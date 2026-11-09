# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/nation_specific.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/nation_specific.py
from __future__ import absolute_import
from past.builtins import cmp
from dossiers2.custom import cache
from dossiers2.custom.cache import getCache as getDossiersCache
from gui import nationSortKeyByIndex
from gui.shared.gui_items.dossier.achievements.abstract.simple_progress import SimpleProgressAchievement

class NationSpecificAchievement(SimpleProgressAchievement):
    __slots__ = ('_nationID', )
    _NATIONAL_VEHICLES = 'vehiclesInTreesByNation'
    _LIST_NAME = ''

    def __init__(self, namePrefix, nationID, block, dossier, value=None):
        self._nationID = nationID
        super(NationSpecificAchievement, self).__init__(self.makeFullName(namePrefix, nationID), block, dossier, value)

    def getNationID(self):
        return self._nationID

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    @classmethod
    def makeFullName(cls, name, nationID):
        if nationID != -1:
            name += str(nationID)
        return name

    def _readValue(self, dossier):
        return 0

    def _readLevelUpTotalValue(self, dossier):
        dossierCache = cache.getCache()
        if self._nationID != -1:
            return len(dossierCache[self._NATIONAL_VEHICLES].get(self._nationID, []))
        return len(self._getAllSuitableVehicles())

    @classmethod
    def _getAllSuitableVehicles(cls):
        return getDossiersCache()['vehiclesInTrees']

    def _getDoneStatus(self, dossier):
        return bool(dossier.getRecordValue(*self.getRecordName()))

    def _compare(self, other):
        res = super(NationSpecificAchievement, self)._compare(other)
        if res:
            return res
        if isinstance(other, NationSpecificAchievement):
            if self._nationID != -1 and other._nationID != -1:
                return cmp(nationSortKeyByIndex(self._nationID), nationSortKeyByIndex(other._nationID))
        return 0
