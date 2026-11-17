# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/client_arena_component_assembler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
from arena_component_system.client_arena_component_system import ClientArenaComponentSystem as ClientArenaComponentSystem
from arena_components.player_type_specific_components import getDefaultComponents as getDefaultComponents
from debug_utils import LOG_WARNING as LOG_WARNING

class ClientArenaComponentAssembler(object):
    @staticmethod
    def assembleComponents(componentSystem):
        ...
    @staticmethod
    def disassembleComponents(componentSystem):
        ...
    @staticmethod
    def _assembleBonusCapsComponents(componentSystem):
        ...
    @staticmethod
    def _addArenaComponents(componentSystem, componentsList):
        ...
    @staticmethod
    def _addArenaComponent(componentSystem, name, componentClass):
        ...

def createComponentSystem(arena, bonusType, arenaType):
    ...
def destroyComponentSystem(componentSystem):
    ...
