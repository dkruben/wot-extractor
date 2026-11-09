# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/config_schemas/umg_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/config_schemas/umg_config.py
from __future__ import absolute_import
import typing
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models, schemas

class ConfigModel(models.Model):
    __slots__ = ('enableAllDaily', 'enableAllWeekly', 'enableDailyWeeklyUI', 'enablePM3Banner',
                 'slides')

    def __init__(self, enableAllDaily, enableAllWeekly, enableDailyWeeklyUI, enablePM3Banner, slides):
        super(ConfigModel, self).__init__()
        self.enableAllDaily = enableAllDaily
        self.enableAllWeekly = enableAllWeekly
        self.enableDailyWeeklyUI = enableDailyWeeklyUI
        self.enablePM3Banner = enablePM3Banner
        self.slides = list(slides)

    def _reprArgs(self):
        return 'enableAllDaily=%s, enableAllWeekly=%s, enableDailyWeeklyUI=%s, enablePM3Banner=%s, slides=%s' % (
         self.enableAllDaily, self.enableAllWeekly, self.enableDailyWeeklyUI, self.enablePM3Banner, self.slides)


class SlideModel(models.Model):
    __slots__ = ('name', 'priority', 'enabled')

    def __init__(self, name, priority, enabled):
        super(SlideModel, self).__init__()
        self.name = name
        self.priority = priority
        self.enabled = enabled

    def _reprArgs(self):
        return 'name=%s, priority=%s, enabled=%s' % (self.name, self.priority, self.enabled)


slideSchema = schemas.Schema(modelClass=SlideModel, fields={'name': (fields.String(required=True)), 
   'priority': (fields.Integer(required=True)), 
   'enabled': (fields.Boolean(required=True))})
umgConfigSchema = GameParamsSchema[ConfigModel](gameParamsKey='umgConfig', modelClass=ConfigModel, fields={'enableAllDaily': (fields.Integer(required=True)), 
   'enableAllWeekly': (fields.Integer(required=True)), 
   'enableDailyWeeklyUI': (fields.Integer(required=True)), 
   'enablePM3Banner': (fields.Integer(required=True)), 
   'slides': (fields.UniCapList(fieldOrSchema=slideSchema, required=True))})
