# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/armor_flashlight_common/server_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/armor_flashlight_common/server_config.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import models, fields

class ServerConfigModel(models.Model):
    __slots__ = ('enabled', )

    def __init__(self, enabled):
        super(ServerConfigModel, self).__init__()
        self.enabled = enabled

    def _reprArgs(self):
        return ('enabled={}').format(self.enabled)


serverConfigSchema = GameParamsSchema[ServerConfigModel](gameParamsKey='armor_flashlight_config', fields={'enabled': (fields.Boolean(required=True))}, modelClass=ServerConfigModel)
