# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/formatters/vehicle_filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from builtins import range as range
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from nations import INDICES as INDICES
from gui import GUI_NATIONS as GUI_NATIONS, GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform import getVehicleTypeAssetPath as getVehicleTypeAssetPath, getNationsFilterAssetPath as getNationsFilterAssetPath, getLevelsAssetPath as getLevelsAssetPath
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES

def packIntVehicleTypesFilter(defaultVehType=-1):
    ...
def packVehicleTypesFilter(defaultVehType, types=...):
    ...
def packNationsFilter(nations=...):
    ...
def packVehicleLevelsFilter(levelRange=...):
    ...
