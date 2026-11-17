# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/difficulty_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings, setSettings as setSettings
from halloween.gui.impl.gen.view_models.views.lobby.difficulty_window_view_model import DifficultyWindowViewModel as DifficultyWindowViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView, HWLobbyNotificationWindow as HWLobbyNotificationWindow
from halloween.gui.impl.lobby.hw_helpers.anomalies_helpers import isAnomaliesSystemAvailable as isAnomaliesSystemAvailable
from halloween.gui.shared.event_dispatcher import showAnomaliesWindow as showAnomaliesWindow
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import DifficultyWindowState as DifficultyWindowState, DIFFICULTY_SCREEN as DIFFICULTY_SCREEN
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class DifficultyWindowView(BaseView):
    __slots__: tuple
    itemsCache: Any
    layoutID: Any
    _difficultyLevel: Any
    def __init__(self, layoutID=None, difficultyLevel=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self):
        ...
    def _getEvents(self):
        ...
    @property
    def _hasNewRecipes(self):
        ...
    @staticmethod
    def _onToAnomaliesClick():
        ...

class DifficultyWindow(HWLobbyNotificationWindow):
    _args: Any
    def __init__(self, layoutID, difficultyLevel, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
