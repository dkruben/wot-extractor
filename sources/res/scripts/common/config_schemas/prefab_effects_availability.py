# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/config_schemas/prefab_effects_availability.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/config_schemas/prefab_effects_availability.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models

class PrefabEffectsAvailabilityModel(models.Model):
    __slots__ = ('enabled', 'switchEnabled')

    def __init__(self, enabled, switchEnabled):
        super(PrefabEffectsAvailabilityModel, self).__init__()
        self.enabled = enabled
        self.switchEnabled = switchEnabled


prefabEffectsAvailabilitySchema = GameParamsSchema[PrefabEffectsAvailabilityModel](gameParamsKey='prefab_effects_availability_config', modelClass=PrefabEffectsAvailabilityModel, fields={'enabled': (fields.Boolean(required=False, default=True)), 
   'switchEnabled': (fields.Boolean(required=False, default=False))}, usedInReplay=True)
