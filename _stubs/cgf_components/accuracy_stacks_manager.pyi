# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/accuracy_stacks_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import SoundGroups as SoundGroups
from cgf_components.vehicle_mechanics_components import AccuracyStacksRTPCComponent as AccuracyStacksRTPCComponent
from AccuracyStacksController import AccuracyStacksController as AccuracyStacksController

class AccuracyStacksMechanicSystem(CGF.System):
    AccuracyActivated: Any
    AccuracyDeactivated: Any
    AccuracyIterate: Any
    AccuracyControllerAccess: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def onAccuracyStacksRTPCProcess(self, accuracyStacksComponent, accuracyControllerAccess):
        ...
    def onAccuracyStacksRTPCRemoved(self, accuracyStacksComponent):
        ...
    def onAccuracyStacksRTPCAdded(self, gameObject, accuracyStacksComponent, accuracyControllerAccess):
        ...
    @classmethod
    def __setAccuracyStacksRTPC(cls, accuracyStacksComponent, accuracyStacksController):
        ...
    @classmethod
    def __getAccuracyStacksProgress(cls, controllerGO, accuracyStacksController):
        ...
