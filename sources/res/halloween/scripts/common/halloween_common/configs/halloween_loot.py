# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/common/halloween_common/configs/halloween_loot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/common/halloween_common/configs/halloween_loot.py
from __future__ import absolute_import
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, schemas
from halloween_common.halloween_constants import HALLOWEEN_LOOT_PARAMS_KEY

class LootModel(models.Model):
    __slots__ = ('lootId', 'bonus')

    def __init__(self, lootId, bonus):
        super(LootModel, self).__init__()
        self.lootId = lootId
        self.bonus = bonus


class LootConfigModel(models.Model):
    __slots__ = ('loot', )

    def __init__(self, loot):
        super(LootConfigModel, self).__init__()
        self.loot = loot

    def getBonus(self, lootId):
        for lootItem in self.loot:
            if lootItem.lootId == lootId:
                return lootItem.bonus

        return {}

    def getBonusItemsAmount(self, lootId):
        return sum([1 if isinstance(bonus, int) else len(bonus) for bonus in self.getBonus(lootId).values()])


def _getBonusReaders(*args, **kwargs):
    import bonus_readers
    return bonus_readers.readBonusSection(bonus_readers.getSupportedBonuses(), *args, **kwargs)


lootSchema = schemas.Schema(fields={'lootId': (fields.String(required=True)), 
   'bonus': (fields.Field(required=True))}, modelClass=LootModel, checkUnknown=True)
lootConfigSchema = GameParamsSchema[LootConfigModel](gameParamsKey=HALLOWEEN_LOOT_PARAMS_KEY, fields={'loot': (fields.List(fieldOrSchema=lootSchema, required=True))}, modelClass=LootConfigModel, checkUnknown=True, usedInReplay=True, readers={'bonus': _getBonusReaders})
