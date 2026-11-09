# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/base_menu_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.shared.utils.HangarSpace import HangarVideoCameraController as HangarVideoCameraController
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class EntryStateWithReason(object):
    state: Any
    reason: Any
    params: Any
    def __init__(self, state, reason, params=None):
        ...

class BaseMenuEntrySubPresenter(SubModelPresenter):
    __hangarSpace: Any
    _entryId: Any
    def __init__(self, entryId, viewModel, parentView):
        ...
    @property
    def _cameraController(self):
        ...
    def packEntry(self):
        ...
    def onNavigate(self):
        ...
    def _getState(self):
        ...
    def _getMenuEntryState(self):
        ...
