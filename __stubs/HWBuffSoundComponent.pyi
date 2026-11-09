# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffSoundComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import enum as enum
import SoundGroups as SoundGroups
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import StrParam as StrParam, ListParam as ListParam, ObjParam as ObjParam, BoolParam as BoolParam
_INTERNAL_OBJ_NAME_PATTER = 'HWBuffSoundComponent:{}'

class HWBuffSoundComponentPlayMode(enum.IntEnum):
    NONE = 0
    SELF = 1
    OTHERS = 2
    ALL = 3

# decorador original: @groupComponent(...)
class HWBuffSoundComponent(DynamicScriptComponent):
    _activationIsPlayed: Any
    _soundObjectInternal: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onAvatarReady(self):
        ...
    def _playActivation(self):
        ...
    def onDestroy(self):
        ...
    @property
    def soundObject(self):
        ...
    def _isVehicleObservedByAvatar(self):
        ...
    def _needToPlay(self, param):
        ...
