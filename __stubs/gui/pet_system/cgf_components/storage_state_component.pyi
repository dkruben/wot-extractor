# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/cgf_components/storage_state_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from gui.pet_system.constants import StorageStateKey as StorageStateKey

# decorador original: @registerComponent
class StorageStateComponent(object):
    group = 'Pet system'
    editorTitle = 'Pet Storage State Component'
    domain = CGF.Domain.Client
    names: dict
    storageObjectKey: Any
