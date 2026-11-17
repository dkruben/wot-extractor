# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/prestige/prestige_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.prestige.views.prestige_reward_view_model import PrestigeRewardViewModel as PrestigeRewardViewModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.prestige.prestige_helpers import fillPrestigeEmblemModel as fillPrestigeEmblemModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class PrestigeRewardView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, vehIntCD, level):
        ...

class PrestigeRewardViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, vehIntCD, level, parent=None):
        ...
