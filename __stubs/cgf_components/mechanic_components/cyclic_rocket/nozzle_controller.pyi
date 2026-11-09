# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/mechanic_components/cyclic_rocket/nozzle_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from GenericComponents import CyclicActivatorComponent as CyclicActivatorComponent
from constants import IS_EDITOR as IS_EDITOR, PHASED_MECHANIC_STATE as PHASED_MECHANIC_STATE, AcceleratorStatus as AcceleratorStatus
from StagedJetBoostersController import StagedJetBoostersController as StagedJetBoostersController
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class NozzleController(object):
    editorTitle = 'Nozzle Controller'
    category = 'Vehicle Mechanics'
    domain = CGF.Domain.ClientEditor
    activeStateGameObject: Any
    endStateGameObject: Any
    failedStateGameObject: Any
    boosterType: Any
    wasActive: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class NozzleActivationSyncComponent(object):
    editorTitle = 'Nozzle Activation Sync'
    category = 'Vehicle Mechanics'
    domain = CGF.Domain.ClientEditor
    endOffset: Any
    endStateObjects: Any
    def __init__(self):
        ...

class NozzleControllerComponentSystem(CGF.System):
    Activated: Any
    Deactivated: Any
    NozzleActivated: Any
    NozzleDeactivated: Any
    BoosterAccess: Any
    NozzleControllerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onAddedSync(self, go, sync, activator, boosterAccess, nozzleAccess):
        ...
    def onRemovedSync(self, sync, queue):
        ...
    def onAddedNozzle(self, go, nozzle, queue, boosterAccess):
        ...
    def onRemovedNozzle(self, nozzle, queue):
        ...
