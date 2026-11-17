# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/mode_selector/story_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from story_mode.account_settings import isWelcomeScreenSeen as isWelcomeScreenSeen
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.loggers import SelectorCardLogger as SelectorCardLogger
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema
_rMode = R.strings.sm_lobby.mode
EVENT_SUFFIX = '_event'

class StoryModeSelectorItem(ModeSelectorLegacyItem):
    __slots__: tuple
    _storyModeCtrl: Any
    _uiLogger: Any
    def __init__(self, oldSelectorItem):
        ...
    def _setResourcesFolderName(self):
        ...
    def _getModeStringsRoot(self):
        ...
    def _setModeDescription(self, modeStrings):
        ...
    def _getPositionByModeName(self):
        ...
    def handleClick(self):
        ...
    def handleInfoPageClick(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def _isNewLabelVisible(self):
        ...
    @property
    def eventSuffix(self):
        ...
