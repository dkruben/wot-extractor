# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/vehicle_appearance/component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import CGF as CGF
from cgf_script.registration import registerComponent as registerComponent
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
TAppearance: Any
_logger: Any

# decorador original: @registerComponent
class VehicleAppearanceComponent(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    appearance: Any
    def __init__(self, appearance):
        ...
