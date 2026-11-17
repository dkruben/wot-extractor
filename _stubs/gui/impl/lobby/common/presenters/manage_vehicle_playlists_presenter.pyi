# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/presenters/manage_vehicle_playlists_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.impl.gen.view_models.views.lobby.hangar.manageable_vehicle_playlists_model import ManageableVehiclePlaylistsModel as ManageableVehiclePlaylistsModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import HangarVehicleEvent as HangarVehicleEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehiclePlaylistsController as IVehiclePlaylistsController

# base nao representavel no stub: ViewComponent[...]
class ManageableVehiclePlaylistsPresenter(EventSystemEntity):
    __vehiclePlaylistsCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __handleContextMenuClicked(self, event=None):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onSelectVehicle(self, id):
        ...
    def __updateModel(self, intCD):
        ...
