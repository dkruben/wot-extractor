# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/weekly_quests_common/weekly_quests_schema.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/weekly_quests_common/weekly_quests_schema.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from constants import Configs
from dict2model import fields, models, validate

class WeeklyQuestsConfigModel(models.Model):
    __slots__ = ('enabled', 'rerollTimeout')

    def __init__(self, enabled, rerollTimeout):
        super(WeeklyQuestsConfigModel, self).__init__()
        self.enabled = enabled
        self.rerollTimeout = rerollTimeout

    def _reprArgs(self):
        return ('enabled={}, rerollTimeout={}').format(self.enabled, self.rerollTimeout)


weeklyQuestsSchema = GameParamsSchema[WeeklyQuestsConfigModel](gameParamsKey=Configs.WEEKLY_QUESTS_CONFIG.value, fields={'enabled': (fields.Boolean(required=True)), 
   'rerollTimeout': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1)))}, modelClass=WeeklyQuestsConfigModel, checkUnknown=True)
