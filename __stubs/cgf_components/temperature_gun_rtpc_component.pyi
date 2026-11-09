# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/temperature_gun_rtpc_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import SoundGroups as SoundGroups
import typing as typing
from constants import IS_CLIENT as IS_CLIENT
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

class TemperatureGunController(object):
    ...

# decorador original: @registerComponent
class TemperatureGunRTPCComponent(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Temperature Gun RTPC'
    domain = CGF.Domain.Client
    RTPCName: Any
    temperatureGunControllerGO: Any
    progress: Any
    def __init__(self):
        ...

class TemperatureGunMechanicSystem(CGF.System):
    TemperatureGunActivated: Any
    TemperatureGunDeactivated: Any
    TemperatureGunIterate: Any
    TemperatureControllerAccess: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __resolveController(self, rtpc, go, controllerAccess):
        ...
    @classmethod
    def __getTemperatureGunProgress(cls, controller):
        ...
    @classmethod
    def __setGunTemperature(cls, rtpc, controller):
        ...
