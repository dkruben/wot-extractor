# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/award_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from halloween.gui.impl.lobby.hw_helpers import getEnemyByArtefactID as getEnemyByArtefactID
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from helpers import dependency as dependency
from gui.game_control.AwardController import RecruitHandler as RecruitHandler, ServiceChannelHandler as ServiceChannelHandler
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.gui.shared.event_dispatcher import showAttachmentRewardView as showAttachmentRewardView, showDifficultyView as showDifficultyView, showKingRewardCongratsView as showKingRewardCongratsView, showDecryptWindowView as showDecryptWindowView, showTwitchConExchangeView as showTwitchConExchangeView, showBestiaryWindow as showBestiaryWindow, showStoryChoiceWindow as showStoryChoiceWindow, showOutroVideo as showOutroVideo
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.impl.gen import R as R
from gui import SystemMessages as SystemMessages
from frameworks.wulf import WindowStatus as WindowStatus
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.gui import halloween_account_settings as halloween_account_settings
from halloween.gui.game_control.halloween_bestiary_controller import EnemyData as EnemyData
_logger: Any

class HWArtefactAwardWindowHandler(ServiceChannelHandler):
    hwArtifactsCtrl: Any
    hwBestiaryCtrl: Any
    settingsCore: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def _isKingRewardToken(self, artefactID):
        ...
    def _showAttachmentView(self, element):
        ...

class HWDifficultyAwardWindowHandler(ServiceChannelHandler):
    difficultyCtrl: Any
    hwController: Any
    guiLoader: Any
    __battleResultsWindowID: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def __checkBattleResultOpened(self):
        ...
    def __onWindowStatusChanged(self, uniqueID, newState):
        ...
    def __handleWindowStatus(self):
        ...

class HWRecruitHandler(RecruitHandler):
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
