# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/sub_modes/sub_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/sub_modes/sub_mode.py
from __future__ import absolute_import
from typing import Dict, TYPE_CHECKING
from dict2model import fields, models, schemas
from fun_random.gui.feature.configs.common.gamemode import gameModeConfigurationSchema
from fun_random.gui.feature.configs.sub_modes.custom_abilities import funSubModeCustomAbilitiesSchema, FunSubModeCustomAbilitiesConfigModel
from fun_random.gui.feature.configs.sub_modes.custom_shells import funSubModeCustomShellsSchema, FunSubModeCustomShellsConfigModel
if TYPE_CHECKING:
    from fun_random.gui.feature.configs.common.gamemode import GameModeConfigurationModel

class FunSubModeConfigurationModel(models.Model):
    __slots__ = ('isExclusiveHelpPages', 'hasBattleQueueWarning', 'assetsPointer',
                 'pbsEfficiency', 'customShells', 'customAbilities', 'showInfoPageOnFirstVisit')

    def __init__(self, isExclusiveHelpPages, hasBattleQueueWarning, assetsPointer, pbsEfficiency, customShells, customAbilities, showInfoPageOnFirstVisit):
        super(FunSubModeConfigurationModel, self).__init__()
        self.isExclusiveHelpPages = isExclusiveHelpPages
        self.hasBattleQueueWarning = hasBattleQueueWarning
        self.assetsPointer = assetsPointer
        self.pbsEfficiency = pbsEfficiency
        self.customShells = customShells
        self.customAbilities = customAbilities
        self.showInfoPageOnFirstVisit = showInfoPageOnFirstVisit


class FunSubModeCompositeConfigurationModel(models.Model):
    __slots__ = ('common', 'subMode')

    def __init__(self, common, subMode):
        super(FunSubModeCompositeConfigurationModel, self).__init__()
        self.common = common
        self.subMode = subMode


funSubModeConfigurationSchema = schemas.Schema[FunSubModeConfigurationModel](fields={'isExclusiveHelpPages': (fields.Boolean(required=False, default=False)), 
   'hasBattleQueueWarning': (fields.Boolean(required=False, default=False)), 
   'assetsPointer': (fields.String(required=True)), 
   'pbsEfficiency': (fields.Dict(keyFieldOrSchema=fields.String(required=True), valueFieldOrSchema=fields.List(fields.String(required=True), required=True), required=True)), 
   'customShells': (fields.Nested(schema=funSubModeCustomShellsSchema, required=False, default=FunSubModeCustomShellsConfigModel)), 
   'customAbilities': (fields.Nested(schema=funSubModeCustomAbilitiesSchema, required=False, default=FunSubModeCustomAbilitiesConfigModel)), 
   'showInfoPageOnFirstVisit': (fields.Boolean(required=False, default=False))}, modelClass=FunSubModeConfigurationModel)
funSubModeCompositeConfigurationSchema = schemas.Schema[FunSubModeCompositeConfigurationModel](fields={'common': (fields.Nested(schema=gameModeConfigurationSchema, required=True)), 
   'subMode': (fields.Nested(schema=funSubModeConfigurationSchema, required=True))}, modelClass=FunSubModeCompositeConfigurationModel)
