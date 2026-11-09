# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/params_schemas/veh_playlists_schema.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/params_schemas/veh_playlists_schema.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from constants import Configs
from dict2model import models, fields as d2mfields

class VehPlaylistsConfigModel(models.Model):
    __slots__ = ('isVehPlaylistsEnabled', )

    def __init__(self, isVehPlaylistsEnabled):
        super(VehPlaylistsConfigModel, self).__init__()
        self.isVehPlaylistsEnabled = isVehPlaylistsEnabled


vehPlaylistsConfigSchema = GameParamsSchema[VehPlaylistsConfigModel](gameParamsKey=Configs.VEH_PLAYLISTS_CONFIG.value, fields={'isVehPlaylistsEnabled': (d2mfields.Boolean())}, modelClass=VehPlaylistsConfigModel, checkUnknown=True)
