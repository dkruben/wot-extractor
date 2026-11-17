# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/model/video_settings_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
import section2dict as section2dict
import typing as typing
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate
from story_mode_common.configs.sounds_schema import SoundModel as SoundModel, SoundSchema as SoundSchema
INTRO_VIDEO_SETTINGS_PATH = 'story_mode/gui/intro_video.xml'
OUTRO_VIDEO_SETTINGS_PATH = 'story_mode/gui/outro_video.xml'
soundEventsSchema: Any
videoSchema: Any
introVideoSchema: Any
__introVideoSchema = None
__outroVideoSchema = None

class SoundEventsModel(SoundModel):
    __slots__: tuple
    pause: Any
    resume: Any
    def __init__(self, start, pause, resume, stop, group, state):
        ...

# base nao representavel no stub: SoundSchema[...]
class SoundEventsSchema:
    def __init__(self):
        ...

class VideoModel(models.Model):
    __slots__: tuple
    id: Any
    videoPath: Any
    music: Any
    playSoundOnClose: Any
    vo: Any
    def __init__(self, id, videoPath, music, playSoundOnClose, vo):
        ...

class VideoSettingsModel(models.Model):
    __slots__: tuple
    missions: Any
    def __init__(self, missions):
        ...

def getIntroVideoSettings():
    ...
def getOutroVideoSettings():
    ...
