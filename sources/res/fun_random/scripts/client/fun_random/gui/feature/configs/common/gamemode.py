# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/common/gamemode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/common/gamemode.py
from __future__ import absolute_import
from dict2model import fields, models, schemas

class GameModeConfigurationModel(models.Model):
    __slots__ = ('regularDevices', 'regularBoosters', 'regularShells', 'regularConsumables')

    def __init__(self, regularDevices, regularBoosters, regularShells, regularConsumables):
        super(GameModeConfigurationModel, self).__init__()
        self.regularDevices = regularDevices
        self.regularBoosters = regularBoosters
        self.regularShells = regularShells
        self.regularConsumables = regularConsumables


gameModeConfigurationSchema = schemas.Schema[GameModeConfigurationModel](fields={'regularDevices': (fields.Boolean(required=True)), 
   'regularBoosters': (fields.Boolean(required=True)), 
   'regularShells': (fields.Boolean(required=True)), 
   'regularConsumables': (fields.Boolean(required=True))}, modelClass=GameModeConfigurationModel)
