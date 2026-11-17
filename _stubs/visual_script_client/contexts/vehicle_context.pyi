# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/contexts/vehicle_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from visual_script.context import VScriptContext as VScriptContext, vse_get_property as vse_get_property
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class VehicleContextClient(VScriptContext):
    _vehicle: Any
    def __init__(self, vehicle):
        ...
    def destroy(self):
        ...
    # decorador original: @vse_get_property(...)
    def getSelf(self):
        ...
