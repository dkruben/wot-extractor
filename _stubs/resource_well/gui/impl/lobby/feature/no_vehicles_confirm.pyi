# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_vehicles_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from resource_well.gui.impl.gen.view_models.views.lobby.no_vehicles_confirm_model import NoVehiclesConfirmModel as NoVehiclesConfirmModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class NoVehiclesConfirm(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def __showHangar(self):
        ...
    def __onEventStateUpdated(self):
        ...

class NoVehiclesConfirmWindow(LobbyWindow):
    def __init__(self, parent=None):
        ...
