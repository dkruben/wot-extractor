# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWLootVisualComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from HWBuffSequencesComponent import HWBuffSequencesComponent as HWBuffSequencesComponent
from dyn_components_groups import groupComponent as groupComponent
from xml_config_specs import StrParam as StrParam

# decorador original: @groupComponent(...)
class HWLootVisualComponent(HWBuffSequencesComponent):
    _stateParam: Any
    def __init__(self, stateParam='state'):
        ...
    def set_lootState(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def _onChangeLootState(self):
        ...
