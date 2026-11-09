# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/components/component_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from GenericComponents import COMPOSITION_ROOT_SLOT_NAME as COMPOSITION_ROOT_SLOT_NAME
from constants import DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot

# decorador original: @ReprInjector.simple(...)
class IVehicleSlotComponent(object):
    def getVehicleSlotName(self):
        ...

class IVehicleGunSlotComponent(IVehicleSlotComponent):
    def getGunInstallationIndex(self):
        ...
    def getVehicleSlotName(self):
        ...
