# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/holiday_final_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from future.utils import viewitems as viewitems
from battle_pass_common import BattlePassConsts as BattlePassConsts, BattlePassTankmenSource as BattlePassTankmenSource, FinalReward as FinalReward
from gui.battle_pass.battle_pass_award import BattlePassAwardsManager as BattlePassAwardsManager
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_constants import ChapterState as ChapterState
from gui.battle_pass.battle_pass_helpers import getAllFinalRewards as getAllFinalRewards, getReceivedTankmenCount as getReceivedTankmenCount, getTankmenShopPackages as getTankmenShopPackages, getVehicleInfoForChapter as getVehicleInfoForChapter, isSeasonEndingSoon as isSeasonEndingSoon, showFinalRewardPreviewBattlePassState as showFinalRewardPreviewBattlePassState
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.holiday_final_view_model import FinalRewardTypes as FinalRewardTypes, HolidayFinalViewModel as HolidayFinalViewModel, ChapterStates as ChapterStates
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import events as events
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar, showBattlePassTankmenVoiceover as showBattlePassTankmenVoiceover, showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_logger: Any
_CHAPTER_STATES: dict

# base nao representavel no stub: ViewComponent[...]
class HolidayFinalPresenter:
    __battlePass: Any
    __itemsCache: Any
    __chapterID: Any
    __tooltipItems: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def getTooltipData(self, event):
        ...
    def updateInitialData(self, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __fillModel(self):
        ...
    def __setChapter(self):
        ...
    def __isTankmenReceived(self, shopPackages):
        ...
    def __update(self):
        ...
    def __onBattlePassSettingsChanged(self, *_):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateRewardChoice(self, model=None):
        ...
    def __updateDetailRewards(self):
        ...
    def __getRewards(self):
        ...
    def __showRewards(self):
        ...
    def __updateState(self):
        ...
    def __getFinalRewardType(self):
        ...
    def __onPreview(self):
        ...
    def __takeAllRewards(self):
        ...
    def __showTankmen(self):
        ...
    def __showHangar(self):
        ...
    def __onAwardViewClose(self, *_):
        ...
