# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/battle_control/controllers/equipment_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
import ResMgr as ResMgr
from gui.battle_control.controllers.consumables.equipment_ctrl import _ReplayItem as _ReplayItem, _InspireItem as _InspireItem, _RegenerationKitItem as _RegenerationKitItem, _ActivationError as _ActivationError, _StealthRadarItem as _StealthRadarItem
from gui.shared.system_factory import registerEquipmentItem as registerEquipmentItem
_EQUIPMENT_CONFIG_PATH = 'frontline/scripts/item_defs/vehicles/common/equipments/epic_equipments.xml'

class _FLStealthRadarItem(_StealthRadarItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _FLInspireItem(_InspireItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _FLRegenerationKit(_RegenerationKitItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

def getEquipmentWorkingResult(item, result, error):
    ...
def registerFLEquipmentsItems():
    ...
