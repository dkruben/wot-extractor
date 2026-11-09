# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/on_death_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class ChangeModelOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Change Model On Death'
    domain = CGF.Domain.ClientEditor
    modelPath: Any
    delay: Any
    initialModel: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class SoundOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Sound On Death'
    domain = CGF.Domain.ClientEditor
    soundPath: Any
    delay: Any
    attachToGO: Any

# decorador original: @registerComponent
class EffectOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Effect On Death'
    domain = CGF.Domain.ClientEditor
    effectPath: Any
    delay: Any
    attachToGO: Any
