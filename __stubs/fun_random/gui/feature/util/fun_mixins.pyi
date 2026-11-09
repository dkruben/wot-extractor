# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/util/fun_mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from fun_random.gui.fun_account_settings import FunSubModeAccountSettings as FunSubModeAccountSettings
from fun_random.gui.fun_gui_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from fun_random.gui.feature.util.fun_helpers import notifyCaller as notifyCaller
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression, hasAnySubMode as hasAnySubMode, hasSingleSubMode as hasSingleSubMode, hasSpecifiedSubMode as hasSpecifiedSubMode
from fun_random.gui.shared.events import FunEventType as FunEventType, FunEventScope as FunEventScope
from fun_random.gui.shared.event_dispatcher import showFunRandomInfoPage as showFunRandomInfoPage, showFunRandomProgressionWindow as showFunRandomProgressionWindow, showFunRandomModeSubSelectorWindow as showFunRandomModeSubSelectorWindow
from gui.impl import backport as backport
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from fun_random.gui.feature.configs.modes.assets_pack import FunModeAssetsPackConfigurationModel as FunModeAssetsPackConfigurationModel
from fun_random.gui.feature.models.common import FunSubModesStatus as FunSubModesStatus
from fun_random.gui.feature.models.progressions import FunProgression as FunProgression
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode
from skeletons.gui.battle_session import IClientArenaVisitor as IClientArenaVisitor
_logger: Any

class FunAssetPacksMixin(object):
    _funRandomCtrl: Any
    @classmethod
    def getModeAssetsConfiguration(cls):
        ...
    @classmethod
    def getModeAssetsPointer(cls):
        ...
    @classmethod
    def getModeIconsResRoot(cls):
        ...
    @classmethod
    def getModeLocalsResRoot(cls):
        ...
    @classmethod
    def getModeNameKwargs(cls):
        ...
    @classmethod
    def getModeUserName(cls):
        ...
    @classmethod
    def getModeDetailedUserName(cls, **kwargs):
        ...
    @classmethod
    def getPrebattleConditionIcon(cls):
        ...

class FunProgressionWatcher(object):
    _funRandomCtrl: Any
    @classmethod
    # decorador original: @hasActiveProgression(...)
    def showActiveProgressionPage(cls):
        ...
    @classmethod
    def getActiveProgression(cls):
        ...
    def startProgressionListening(self, updateMethod, tickMethod=None):
        ...
    def stopProgressionListening(self, updateMethod, tickMethod=None):
        ...

class FunSubModesWatcher(object):
    _funRandomCtrl: Any
    @classmethod
    def getBattleSubMode(cls, arenaVisitor=None):
        ...
    @classmethod
    def getDesiredSubMode(cls):
        ...
    @classmethod
    def getSubMode(cls, subModeID):
        ...
    @classmethod
    def getSubModes(cls, subModesIDs=None, isOrdered=False):
        ...
    @classmethod
    def getSubModesStatus(cls, subModesIDs=None):
        ...
    @classmethod
    # decorador original: @hasAnySubMode(...)
    def showCommonInfoPage(cls):
        ...
    # decorador original: @hasSpecifiedSubMode(...)
    def showSubModeInfoPage(self, subModeID):
        ...
    # decorador original: @hasSingleSubMode(...)
    def showSubModesInfoPage(self):
        ...
    def startSubSelectionListening(self, method):
        ...
    def startSubSettingsListening(self, method, desiredOnly=False):
        ...
    def startSubStatusListening(self, updateMethod, desiredOnly=False, tickMethod=None):
        ...
    def stopSubSelectionListening(self, method):
        ...
    def stopSubSettingsListening(self, method, desiredOnly=False):
        ...
    def stopSubStatusListening(self, updateMethod, desiredOnly=False, tickMethod=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def selectFunRandomBattle(self, subModeID=..., callback=None):
        ...

class FunSubModeHolder(FunSubModesWatcher):
    __subMode: Any
    def __init__(self):
        ...
    def getHoldingSubMode(self):
        ...
    def catchSubMode(self, subModeID):
        ...
    def releaseSubMode(self):
        ...
