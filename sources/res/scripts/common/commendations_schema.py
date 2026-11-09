# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/commendations_schema.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/commendations_schema.py
from __future__ import absolute_import
from game_params_common.base_manager import GameParamsSchema
from constants import Configs
from dict2model import models, fields as d2mfields

class CommendationsConfigModel(models.Model):
    __slots__ = ('isLiveTagsEnabled', 'isCommendationsEnabled')

    def __init__(self, isLiveTagsEnabled, isCommendationsEnabled):
        super(CommendationsConfigModel, self).__init__()
        self.isCommendationsEnabled = isCommendationsEnabled
        self.isLiveTagsEnabled = isLiveTagsEnabled


commendationsConfigSchema = GameParamsSchema[CommendationsConfigModel](gameParamsKey=Configs.COMMENDATIONS_CONFIG.value, fields={'isLiveTagsEnabled': (d2mfields.Boolean()), 
   'isCommendationsEnabled': (d2mfields.Boolean())}, modelClass=CommendationsConfigModel, checkUnknown=True, usedInReplay=True)
