# wot-extractor: STUB (.pyi) gerado a partir de sources/res/event_platform/scripts/client/event_platform/respawns/respawns_client_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from cgf_script.registration import registerModule as registerModule
from event_platform.respawns.respawns import RespawnPolicySystem as RespawnPolicySystem
from DisconnectRespawnValidatorComponent import DisconnectRespawnValidatorComponent as DisconnectRespawnValidatorComponent
from IndividualRespawnTimerComponent import IndividualRespawnTimerComponent as IndividualRespawnTimerComponent
from RespawnPolicyVehicleLinkComponent import RespawnPolicyVehicleLinkComponent as RespawnPolicyVehicleLinkComponent

# decorador original: @registerModule
class ClientRespawnsModule(object):
    name = 'ClientRespawnsModule'
    group = 'Battle'
    systems: list
    components: list
