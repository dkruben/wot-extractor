# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/interfaces.py
import typing
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel, Array
    from gui.battle_results.stats_ctrl import BattleResults
    from gui.battle_results.reusable.shared import VehicleSummarizeInfo
    from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import SimpleStatsParameterModel
    BattleResultsComponentModelType = typing.TypeVar('BattleResultsComponentModelType', bound=ViewModel)
    TooltipModelType = typing.TypeVar('TooltipModelType', bound=ViewModel)

class IBattleResultsPacker(object):

    @classmethod
    def packModel(cls, model, battleResults):
        raise NotImplementedError

    @classmethod
    def updateModel(cls, model, battleResults, ctx=None, isFullUpdate=True):
        pass


class ICurrencyPacker(object):

    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        pass


class IStatisticsPacker(object):

    @classmethod
    def packModel(cls, model, info, battleResult):
        pass


class ITooltipPacker(object):

    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        raise NotImplementedError
