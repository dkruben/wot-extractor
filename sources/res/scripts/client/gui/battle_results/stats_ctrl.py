# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/stats_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/stats_ctrl.py
import typing
from collections import namedtuple
from frameworks.wulf import ViewModel
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
    BattleResultsModelType = typing.TypeVar('BattleResultsModelType', bound=ViewModel)
    TooltipModelType = typing.TypeVar('TooltipModelType', bound=ViewModel)
BattleResults = namedtuple('BattleResults', ('results', 'reusable'))

class IBattleResultStatsCtrl(object):
    CTRL_IMPL_TYPE_GAMEFACE = 0
    CTRL_IMPL_TYPE_FLASH = 1

    def clear(self):
        raise NotImplementedError

    @property
    def ctrlImplType(self):
        return self.CTRL_IMPL_TYPE_FLASH

    def setResults(self, results, reusable):
        raise NotImplementedError

    def getResults(self):
        return

    def getVO(self):
        raise NotImplementedError

    def onResultsPosted(self, arenaUniqueID):
        raise NotImplementedError

    @staticmethod
    def onShowResults(arenaUniqueID):
        raise NotImplementedError

    @classmethod
    def representativeArenaBonusType(cls):
        return
