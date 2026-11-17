# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/serial_number_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from functools import partial as partial
from GenericComponents import DecalComponent as DecalComponent
from EntitySync import EntityGOSync as EntityGOSync
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import List as List

# decorador original: @registerComponent
class SerialNumberSwitcher(object):
    editorTitle = 'Serial Number Switcher'
    domain = CGF.Domain.Client
    lamp3digits: Any
    lamp4digits: Any
    lamp5digits: Any
    def getPrefabPath(self, counterValue):
        ...

# decorador original: @registerComponent
class SerialNumberComponent(object):
    editorTitle = 'Serial Number'
    domain = CGF.Domain.Client
    counterValue: Any
    splitNumber: Any
    decalComponent: Any
    decalCount: Any

class SerialNumberComponentSystem(CGF.System):
    DEFAULT_NUMBER = '00000'
    SwitcherActivated: Any
    NumberActivated: Any
    DecalAccess: Any
    EntityGOSyncAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __onLoaded(self, counterValue, root, _, queue):
        ...
    def __getVehicle(self, gameObject):
        ...
    def __getSerialNumberValue(self, vehicle):
        ...
