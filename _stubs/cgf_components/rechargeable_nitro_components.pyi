# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/rechargeable_nitro_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import SoundGroups as SoundGroups
from cgf_script.registration import registerComponent as registerComponent, ComponentProperty as ComponentProperty
from constants import IS_CLIENT as IS_CLIENT

class RechargeableNitroController(object):
    ...

# decorador original: @registerComponent
class RechargeableNitroRTPCComponent(object):
    category = 'Sound'
    editorTitle = 'Rechargeable Nitro RTPC'
    domain = CGF.Domain.Client
    RTPCName: Any
    rechargeableNitroControllerGO: Any
    progress: Any
    def __init__(self):
        ...

class RechargeableNitroMechanicSystem(CGF.System):
    NitroActivated: Any
    NitroDeactivated: Any
    NitroIterate: Any
    NitroControllerAccess: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __setRechargeableNitroRTPC(self, rechargeableNitroRTPCComponent):
        ...
    def __getRechargeableNitroActiveProgress(self, rechargeableNitroControllerGO):
        ...
