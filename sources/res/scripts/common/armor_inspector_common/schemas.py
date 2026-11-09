# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/armor_inspector_common/schemas.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/armor_inspector_common/schemas.py
from __future__ import absolute_import
from armor_inspector_common.models import ArmorInspectorConfigModel
from game_params_common.schema import GameParamsSchema
from dict2model import fields
armorInspectorConfigSchema = GameParamsSchema[ArmorInspectorConfigModel](gameParamsKey='armor_inspector_config', fields={'enabled': (fields.Boolean(required=True)), 
   'linkButtonURL': (fields.String(required=False, default=None)), 
   'disabledVehicle': (fields.UniCapList(fieldOrSchema=fields.String(required=True), required=False, default=list))}, modelClass=ArmorInspectorConfigModel)
