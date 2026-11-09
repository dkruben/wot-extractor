# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/difficulty_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from last_stand_common.last_stand_constants import DEFAULT_DIFFICULTY_MODIFIER as DEFAULT_DIFFICULTY_MODIFIER
from last_stand.gui.impl.gen.view_models.views.lobby.difficulty_window_view_model import DifficultyWindowViewModel as DifficultyWindowViewModel
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView, EventLobbyNotificationWindow as EventLobbyNotificationWindow
from last_stand.gui.impl.lobby.ls_helpers import fillRewards as fillRewards
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import DifficultyWindowState as DifficultyWindowState, DIFFICULTY_SCREEN as DIFFICULTY_SCREEN
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
_R_BACKPORT_TOOLTIP: Any

class DifficultyWindowView(BaseView):
    layoutID: Any
    lsMissionsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 3
    _difficultyLevel: Any
    __idGen: Any
    __bonusCache: Any
    def __init__(self, layoutID=None, difficultyLevel=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
    def _getEvents(self):
        ...

class DifficultyWindow(EventLobbyNotificationWindow):
    _args: Any
    def __init__(self, layoutID, difficultyLevel, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
