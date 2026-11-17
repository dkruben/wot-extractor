# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/sub_presenter_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items import Vehicle as Vehicle
from gui.impl.lobby.vehicle_hub.vehicle_hub_main_view import VehicleHubCtx as VehicleHubCtx

class SubPresenterBase(SubModelPresenter):
    __slots__: tuple
    _itemsCache: Any
    __vhCtx: Any
    def __init__(self, model, parentView):
        ...
    @property
    def vehicleHubCtx(self):
        ...
    @property
    def currentVehicle(self):
        ...
    def setVehicleHubCtx(self, vhCtx):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
