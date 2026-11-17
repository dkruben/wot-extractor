# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/award_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from gui.game_control.AwardController import ServiceChannelHandler as ServiceChannelHandler
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_story_point_controller import ILSStoryPointController as ILSStoryPointController
from last_stand.gui.shared.event_dispatcher import showAttachmentRewardWindow as showAttachmentRewardWindow, showDifficultyView as showDifficultyView, showLootBoxMainViewInQueue as showLootBoxMainViewInQueue, showStageRewardWindow as showStageRewardWindow, showNarrationWindowView as showNarrationWindowView
from last_stand_common.last_stand_constants import DifficultyMissionsSettings as DifficultyMissionsSettings, MsgDataCacheKeys as MsgDataCacheKeys
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.impl.gen import R as R
from gui import SystemMessages as SystemMessages
from frameworks.wulf import WindowStatus as WindowStatus
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.gui.ls_gui_constants import DIFFICULTY_LEVEL_TO_TOKEN as DIFFICULTY_LEVEL_TO_TOKEN, DIFFICULTY_TOKEN_TO_LEVEL as DIFFICULTY_TOKEN_TO_LEVEL, DifficultyLevel as DifficultyLevel
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui import ls_account_settings as settings
_logger: Any

class LSAwardWindowHandler(ServiceChannelHandler):
    difficultyCtrl: Any
    lsArtifactsCtrl: Any
    lsStoryPointCtrl: Any
    lsCtrl: Any
    settingsCore: Any
    guiLoader: Any
    _storedMessages: Any
    def __init__(self, awardCtrl):
        ...
    def stop(self):
        ...
    def start(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def _show(self, data):
        ...
    def _showDifficulty(self, data):
        ...
    def _showNarrationStoryPoint(self, data):
        ...
    def _showDifficultyMissions(self, data):
        ...
    def _showArtefacts(self, data):
        ...
    def _isFinalRewardArtefactToken(self, token):
        ...
    def _showAttachmentView(self, element):
        ...
    def _onSettingsUpdate(self):
        ...
    def _onEventDisabled(self):
        ...
    def __onWindowStatusChanged(self, uniqueID, newState):
        ...
    def __handleWindowStatus(self):
        ...
    def __hasAnyNotShownAward(self):
        ...
