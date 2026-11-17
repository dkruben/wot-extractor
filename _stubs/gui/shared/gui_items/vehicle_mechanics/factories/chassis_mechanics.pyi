# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/chassis_mechanics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory as BaseMechanicFactory
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import CHASSIS_MECHANIC_DETECTORS as CHASSIS_MECHANIC_DETECTORS
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
_CHASSIS_MECHANICS: Any

class ChassisMechanicFactory(BaseMechanicFactory):
    @classmethod
    def _getMechanicsChecks(cls, guiItem, _):
        ...
