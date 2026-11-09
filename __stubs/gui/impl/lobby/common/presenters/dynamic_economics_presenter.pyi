# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/presenters/dynamic_economics_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from BonusCaps import BonusCapsConst as BonusCapsConst
from constants import Configs as Configs
from gui.impl.gen.view_models.views.lobby.common.dynamic_economics_model import DynamicEconomicsModel as DynamicEconomicsModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

# base nao representavel no stub: ViewComponent[...]
class DynamicEconomicsPresenter(IGlobalListener):
    __hangarGuiCtrl: Any
    __lobbyContext: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateModel(self, *_):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
