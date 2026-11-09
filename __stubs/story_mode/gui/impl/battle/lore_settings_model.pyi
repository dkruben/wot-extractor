# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/battle/lore_settings_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
import section2dict as section2dict
import typing as typing
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags
from story_mode_common.configs.sounds_schema import soundSchema as soundSchema
from story_mode_common.configs.sounds_schema import SoundModel as SoundModel
_LORE_SETTINGS_PATH = 'story_mode/gui/lore.xml'
missionLoreSchema: Any
epilogueLoreSchema: Any
loreSchema: Any
__loreSchema = None

class MissionLoreModel(models.Model):
    __slots__: tuple
    id: Any
    music: Any
    vo: Any
    battleMusic: Any
    def __init__(self, id, music, vo, battleMusic):
        ...

class EpilogueLoreModel(models.Model):
    __slots__: tuple
    music: Any
    vo: Any
    def __init__(self, music, vo):
        ...

class LoreSettingsModel(models.Model):
    __slots__: tuple
    mission: Any
    epilogue: Any
    def __init__(self, mission, epilogue):
        ...

def getLoreSettings():
    ...
