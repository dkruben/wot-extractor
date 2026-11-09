# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/on_shot_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class EffectOnShotComponent(object):
    group = 'Shooting'
    editorTitle = 'Effect On Shot'
    domain = CGF.Domain.ClientEditor
    effectPath: Any

# decorador original: @registerComponent
class SoundOnShotComponent(object):
    group = 'Shooting'
    editorTitle = 'Sound On Shot'
    domain = CGF.Domain.ClientEditor
    soundPath: Any
