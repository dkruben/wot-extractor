# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/client_story_mode_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from cgf_script.registration import registerModule as registerModule
from story_mode.cgf_components.bunkers import BunkersSystem as BunkersSystem
from BunkerLogicComponent import BunkerLogicComponent as BunkerLogicComponent

# decorador original: @registerModule
class ClientStoryModeModule(object):
    name = 'Client Story Mode Module'
    desc = 'Client Story Mode Functionalities'
    group = 'Store Mode'
    systems: list
    components: list
