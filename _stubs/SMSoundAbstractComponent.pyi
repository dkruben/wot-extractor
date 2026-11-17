# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/SMSoundAbstractComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
import BigWorld as BigWorld
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import StrParam as StrParam, EnumParam as EnumParam, ListParam as ListParam, ObjParam as ObjParam

# decorador original: @enum.unique
class SMSoundComponentPlayMode(str, enum.Enum):
    NONE = 'none'
    SELF = 'self'
    OTHERS = 'others'
    ALL = 'all'

# decorador original: @groupComponent(...)
class SMSoundAbstractComponent(DynamicScriptComponent):
    _activationIsPlayed: Any
    def __init__(self, *_, **__):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _isPlayerVehicle(self):
        ...
    def _needToPlay(self, param):
        ...
    def _playSound(self, playTo, soundName):
        ...
    def _play(self, soundName):
        ...
