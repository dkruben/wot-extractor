# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/mechanic_components/cyclic_rocket/accelerator_status_tracker.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from StagedJetBoostersController import StagedJetBoostersController as StagedJetBoostersController
from constants import AcceleratorStatus as AcceleratorStatus
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class AcceleratorStatusTrackerComponent(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Accelerator Status Tracker'
    domain = CGF.Domain.Client
    target: Any
    type: Any
    status: Any
    ctrl: Any
    def __init__(self):
        ...

class AcceleratorStatusTrackerComponentSystem(CGF.System):
    Activated: Any
    Deactivated: Any
    Iterate: Any
    BoosterAccess: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def onAdded(self, go, tracker, boosterAccess):
        ...
    def onRemoved(self, tracker, queue):
        ...
    def onProcess(self, tracker, boosterAccess, queue):
        ...
    def __update(self, tracker, status, flag, queue):
        ...
