# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/config_schemas/oit_availability.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/config_schemas/oit_availability.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models

class OitAvailabilityModel(models.Model):
    __slots__ = ('min', 'low', 'medium', 'high', 'ultra')

    def __init__(self, min, low, medium, high, ultra):
        super(OitAvailabilityModel, self).__init__()
        self.min = min
        self.low = low
        self.medium = medium
        self.high = high
        self.ultra = ultra


oitAvailabilitySchema = GameParamsSchema[OitAvailabilityModel](gameParamsKey='oit_availability_config', modelClass=OitAvailabilityModel, fields={'min': (fields.Boolean(required=False, default=False)), 
   'low': (fields.Boolean(required=False, default=False)), 
   'medium': (fields.Boolean(required=False, default=False)), 
   'high': (fields.Boolean(required=False, default=False)), 
   'ultra': (fields.Boolean(required=False, default=False))})
