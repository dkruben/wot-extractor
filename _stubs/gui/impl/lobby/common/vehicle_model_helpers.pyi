# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/vehicle_model_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel as VehicleMechanicModel, MechanicsRank as MechanicsRank, MechanicsEnum as MechanicsEnum
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel
from gui.impl.lobby.platoon.platoon_helpers import removeNationFromTechName as removeNationFromTechName
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from frameworks.wulf import Array as Array
from typing import Optional as Optional, Iterable as Iterable, List as List
from gui.shared.gui_items.vehicle_mechanics.vehicle_mechanic_item import VehicleMechanicItem as VehicleMechanicItem

def fillVehicleModel(model, vehicleItem, tags=None):
    ...
def fillVehicleMechanicModel(mechanicModel, mechanicItem):
    ...
def clearVehicleMechanicModel(mechanicModel):
    ...
def fillVehicleMechanicsArray(mechanicsArray, vehicleItem):
    ...
