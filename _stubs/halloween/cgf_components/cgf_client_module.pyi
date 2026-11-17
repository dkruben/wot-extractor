# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/cgf_components/cgf_client_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from cgf_script.registration import registerModule as registerModule
from cgf_components.client_worlds_helpers import clientWorldsPredicate as clientWorldsPredicate, ClientWorld as ClientWorld
from halloween.cgf_components.hexapod_component import HWIsHexapod as HWIsHexapod, HWHexapodSystem as HWHexapodSystem
from halloween.cgf_components.soul_collector_components import SoulCollectorProgressComponent as SoulCollectorProgressComponent, SoulCollectorComponent as SoulCollectorComponent

# decorador original: @registerModule
class HalloweenClientBattleModule(object):
    name = 'Halloween Battle Client Module'
    group = 'Halloween'
    systems: list
    components: list
