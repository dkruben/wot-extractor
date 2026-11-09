# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/sound/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
import WWISE as WWISE
import SoundGroups as SoundGroups
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from web.web_client_api import w2c as w2c, w2capi as w2capi, W2CSchema as W2CSchema, Field as Field

class _SoundSchema(W2CSchema):
    sound_id: Any

class _SoundStateSchema(W2CSchema):
    state_name: Any
    state_value: Any

class _HangarSoundSchema(W2CSchema):
    mute: Any

# decorador original: @w2capi(...)
class SoundWebApi(object):
    _ENTER_EXIT_SOUND_MAPPING: dict
    __exitSounds: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def sound(self, cmd):
        ...
    def _soundFini(self):
        ...

# decorador original: @w2capi(...)
class SoundStateWebApi(object):
    _ON_EXIT_STATES: dict
    __setStates: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def setSoundState(self, cmd):
        ...
    def _soundStateFini(self):
        ...

# decorador original: @w2capi(...)
class HangarSoundWebApi(object):
    # decorador original: @w2c(...)
    def hangarSound(self, cmd):
        ...
    def _hangarSoundFini(self):
        ...
