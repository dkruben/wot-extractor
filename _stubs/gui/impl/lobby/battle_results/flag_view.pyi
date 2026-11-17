# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/flag_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.impl.gen.view_models.views.lobby.battle_results.flag.flag_view_model import FlagViewModel as FlagViewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
_TEXTURE_PATH = 'particles/content_deferred/GFX_models/environment/hangar_v4/screen_flag.dds'

class FlagWindow(WindowImpl):
    def __init__(self):
        ...

class FlagView(ViewImpl, IRoutableView):
    _VIEW_SETTINGS_LAYOUT_ID: Any
    _VIEW_MODEL = FlagViewModel
    __router: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getLsmStateClass(self):
        ...
    def getRouterModel(self):
        ...
    @property
    def viewModel(self):
        ...
