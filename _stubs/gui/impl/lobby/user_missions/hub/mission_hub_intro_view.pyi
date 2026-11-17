# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/mission_hub_intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.mission_hub_intro_view_model import MissionHubIntroViewModel as MissionHubIntroViewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur

class MissionHubIntroView(ViewImpl):
    __slots__: tuple
    __header: Any
    __description: Any
    __icon: Any
    __buttonText: Any
    def __init__(self, header, description, icon, buttonText=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...

class MissionHubIntroWindow(WindowImpl):
    __slots__: tuple
    __blur: Any
    def __init__(self, header, icon, description, buttonText=None):
        ...
    def _finalize(self):
        ...
