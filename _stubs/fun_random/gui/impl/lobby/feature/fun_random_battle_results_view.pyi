# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_battle_results_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from fun_random.gui.feature.fun_sounds import FUN_BATTLE_RESULTS_SOUND_SPACE as FUN_BATTLE_RESULTS_SOUND_SPACE
from fun_random.gui.sounds.ambients import FunRandomBattleResultsEnv as FunRandomBattleResultsEnv
from fun_random.gui.shared.fun_system_factory import collectBattleResultsSoundEnv as collectBattleResultsSoundEnv
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_battle_results_view_model import FunBattleResultsViewModel as FunBattleResultsViewModel

class FunRandomBattleResultsView(ViewImpl):
    _COMMON_SOUND_SPACE = FUN_BATTLE_RESULTS_SOUND_SPACE
    __sound_env__ = FunRandomBattleResultsEnv
    __battleResults: Any
    __connectionMgr: Any
    __arenaUniqueID: Any
    __subPresenter: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def viewModel(self):
        ...
    def createContextMenu(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def getDynamicSoundEnv(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...

class FunPostBattleResultsWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
