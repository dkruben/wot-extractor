# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared.utils.HangarSpace import HangarVideoCameraController as HangarVideoCameraController
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class VehicleMenuPresenter(IPrbListener):
    __hangarGuiCtrl: Any
    __hangarSpace: Any
    __menuEntries: Any
    __isVehicleChanging: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def cameraController(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __initMenuEntries(self):
        ...
    def __updateModel(self):
        ...
    def __onNavigate(self, args):
        ...
    def __onVehicleChanging(self):
        ...
    def __onVehicleChanged(self):
        ...
