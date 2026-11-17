# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/trigger_vse_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Event as Event
from GenericComponents import VSEComponent as VSEComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class TriggerVSEComponent(object):
    editorTitle = 'Trigger VSE'
    domain = CGF.Domain.ClientEditor
    eventName: Any
    triggerEvent: Any
    def __init__(self):
        ...

class TriggerVisualScriptComponentsSystem(CGF.System):
    TriggerActivated: Any
    TriggerDeactivated: Any
    Reactions: Any
    def update(self):
        ...
