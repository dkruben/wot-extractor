# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/base_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod
import typing as typing
import Event as Event
from frameworks.wulf import WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel as ModeSelectorNormalCardModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_reward_model import ModeSelectorRewardModel as ModeSelectorRewardModel
from gui.impl.lobby.mode_selector.items.items_constants import COLUMN_SETTINGS as COLUMN_SETTINGS, DEFAULT_PRIORITY as DEFAULT_PRIORITY, DEFAULT_COLUMN as DEFAULT_COLUMN, ModeSelectorRewardID as ModeSelectorRewardID, DEFAULT_MODE_SETTING as DEFAULT_MODE_SETTING
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.shared.formatters import time_formatters as time_formatters
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from soft_exception import SoftException as SoftException
from typing import Callable as Callable, Optional as Optional, Type as Type, Union as Union
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_model import ModeSelectorCardModel as ModeSelectorCardModel
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import SelectorItem as SelectorItem
from frameworks.wulf import PyResAccessor as PyResAccessor
_rMode = R.strings.mode_selector.mode
_INFO_PAGE_KEY_TEMPLATE = 'infoPage%s'

class ModeSelectorItem(object, metaclass=ABCMeta):
    __slots__: tuple
    _VIEW_MODEL = None
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.DEFAULT
    __limitedUIController: Any
    _initialized: Any
    _viewModel: Any
    _preferredColumn: Any
    _priority: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    @abstractmethod
    def modeName(self):
        ...
    @property
    def preferredColumn(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def isSelectable(self):
        ...
    @property
    def isVisible(self):
        ...
    @property
    def disabledTooltipText(self):
        ...
    def getFactory(self):
        ...
    def handleClick(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...
    def checkHeaderNavigation(self):
        ...
    def handleInfoPageClick(self):
        ...
    def _onInitializing(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def _isNewLabelVisible(self):
        ...
    def _onDisposing(self):
        ...
    def _getDisabledTooltipText(self):
        ...
    def _getIsDisabled(self):
        ...
    def _getIsNew(self):
        ...
    def _getPositionByModeName(self):
        ...
    def _urlProcessing(self, url):
        ...

class ModeSelectorNormalCardItem(ModeSelectorItem):
    __slots__: tuple
    _VIEW_MODEL = ModeSelectorNormalCardModel
    onCardChange: Any
    _preferredColumn: Any
    _priority: Any
    def __init__(self):
        ...
    @property
    def modeName(self):
        ...
    @property
    def calendarTooltipText(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def hasExtendedCalendarTooltip(self):
        ...
    def getExtendedCalendarTooltip(self, parentWindow):
        ...
    def _isNeedToHideCard(self):
        ...
    def _getModeStringsRoot(self):
        ...
    def _onInitializing(self):
        ...
    def _setResourcesFolderName(self):
        ...
    def _setModeDescription(self, modeStrings):
        ...
    def _setModeTexts(self):
        ...
    def _addReward(self, rewardID, locParams=None, icon=None, **params):
        ...
    def _onDisposing(self):
        ...

class ModeSelectorLegacyItem(ModeSelectorNormalCardItem):
    __slots__: tuple
    _legacySelectorItem: Any
    def __init__(self, oldSelectorItem):
        ...
    @property
    def modeName(self):
        ...
    @property
    def isSelectable(self):
        ...
    @property
    def isVisible(self):
        ...
    def getFactory(self):
        ...
    def _getIsNew(self):
        ...
    def _getIsDisabled(self):
        ...
    def _onInitializing(self):
        ...

def getFormattedTimeLeft(seconds):
    ...
def formatSeasonLeftTime(currentSeason):
    ...
def getInfoPageKey(modeName):
    ...
