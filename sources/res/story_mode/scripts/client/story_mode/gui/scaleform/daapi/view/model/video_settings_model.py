# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/model/video_settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/model/video_settings_model.py
from __future__ import absolute_import
import ResMgr, section2dict, typing
from dict2model import models, schemas, fields, validate
from story_mode_common.configs.sounds_schema import SoundModel, SoundSchema
INTRO_VIDEO_SETTINGS_PATH = 'story_mode/gui/intro_video.xml'
OUTRO_VIDEO_SETTINGS_PATH = 'story_mode/gui/outro_video.xml'

class SoundEventsModel(SoundModel):
    __slots__ = ('pause', 'resume')

    def __init__(self, start, pause, resume, stop, group, state):
        super(SoundEventsModel, self).__init__(start, stop, group, state)
        self.pause = pause
        self.resume = resume


class SoundEventsSchema(SoundSchema[SoundEventsModel]):

    def __init__(self):
        super(SoundEventsSchema, self).__init__(fields={'pause': (fields.String(required=True, default='')), 
           'resume': (fields.String(required=True, default=''))}, checkUnknown=True, modelClass=SoundEventsModel)


soundEventsSchema = SoundEventsSchema()

class VideoModel(models.Model):
    __slots__ = ('id', 'videoPath', 'music', 'playSoundOnClose', 'vo')

    def __init__(self, id, videoPath, music, playSoundOnClose, vo):
        super(VideoModel, self).__init__()
        self.id = id
        self.videoPath = videoPath
        self.music = music
        self.playSoundOnClose = playSoundOnClose
        self.vo = vo


class VideoSettingsModel(models.Model):
    __slots__ = ('missions', )

    def __init__(self, missions):
        super(VideoSettingsModel, self).__init__()
        self.missions = missions


videoSchema = schemas.Schema(fields={'id': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   'videoPath': (fields.String(required=True)), 
   'music': (fields.Nested(soundEventsSchema, required=True)), 
   'playSoundOnClose': (fields.String(required=False)), 
   'vo': (fields.String(required=True))}, modelClass=VideoModel, checkUnknown=True)
introVideoSchema = schemas.Schema(fields={'missions': (fields.UniCapList(fieldOrSchema=videoSchema, required=True, deserializedValidators=validate.Length(minValue=1)))}, modelClass=VideoSettingsModel, checkUnknown=True)
__introVideoSchema = None
__outroVideoSchema = None

def getIntroVideoSettings():
    global __introVideoSchema
    if __introVideoSchema:
        return __introVideoSchema
    root = ResMgr.openSection(INTRO_VIDEO_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __introVideoSchema = introVideoSchema.deserialize(rawData)
    return __introVideoSchema


def getOutroVideoSettings():
    global __outroVideoSchema
    if __outroVideoSchema:
        return __outroVideoSchema
    root = ResMgr.openSection(OUTRO_VIDEO_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __outroVideoSchema = introVideoSchema.deserialize(rawData)
    return __outroVideoSchema
