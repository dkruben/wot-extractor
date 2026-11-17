# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/progression_screen_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from frontline.frontline_account_settings import getReceivedRewardTokens as getReceivedRewardTokens, setReceivedRewardTokens as setReceivedRewardTokens
from frontline.gui.frontline_bonus_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from frontline.gui.frontline_helpers import getFrontlineState as getFrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.progression_screen.progression_screen_model import ProgressionScreenModel as ProgressionScreenModel
from frontline.gui.impl.gen.view_models.views.lobby.views.progression_screen.tiers_section_model import TiersSectionModel as TiersSectionModel
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.event_dispatcher import showEpicRewardsSelectionWindow as showEpicRewardsSelectionWindow, showFrontlineAwards as showFrontlineAwards, showHangar as showHangar
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings

class ProgressionScreenView(ViewImpl, IGlobalListener):
    _COMMON_SOUND_SPACE: Any
    __epicController: Any
    __slots__: tuple
    __tooltipItems: Any
    __rewardsSelectionWindow: Any
    __hasNewRewards: Any
    __gameModeStatus: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def __frontlineLevel(self):
        ...
    @property
    def __frontlineProgress(self):
        ...
    @property
    def __levelUpXp(self):
        ...
    @property
    def __isMaxLevel(self):
        ...
    @property
    def __newRewardsCount(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
    def _updateFrontlineState(self, vm):
        ...
    def _fillTiersSection(self, vm):
        ...
    def _finalize(self):
        ...
    def __checkHasNewRewards(self):
        ...
    def __onClaimRewards(self):
        ...
    def __onEpicUpdated(self, diff):
        ...
    def __onGameModeStatusChange(self):
        ...
    def __onClose(self):
        ...
