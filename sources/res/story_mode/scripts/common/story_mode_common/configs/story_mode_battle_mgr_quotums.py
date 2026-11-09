# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/common/story_mode_common/configs/story_mode_battle_mgr_quotums.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/common/story_mode_common/configs/story_mode_battle_mgr_quotums.py
from __future__ import absolute_import
import typing
from game_params_common.schema import GameParamsSchema
from dict2model import models, fields, validate, schemas, exceptions
from story_mode_common.story_mode_constants import PRIORITY

class QuotumsModel(models.Model):
    __slots__ = ('quotums', )

    def __init__(self, quotums):
        super(QuotumsModel, self).__init__()
        self.quotums = quotums


class QuotumModel(models.Model):
    __slots__ = ('priority', 'quotum')

    def __init__(self, priority, quotum):
        super(QuotumModel, self).__init__()
        self.priority = priority
        self.quotum = quotum


def validatePriorityies(model):
    priorities, duplicates = set(), set()
    for q in model.quotums:
        if q.priority not in priorities:
            priorities.add(q.priority)
        else:
            duplicates.add(q.priority)

    if duplicates:
        raise exceptions.ValidationError(('Priority duplicates: {}').format(duplicates))


quotumSchema = schemas.Schema[QuotumModel](fields={'priority': (fields.IntEnum(PRIORITY, required=True, deserializedValidators=validate.Range(minValue=0))), 
   'quotum': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=0)))}, modelClass=QuotumModel, checkUnknown=True)
quotumsSchema = GameParamsSchema(gameParamsKey='story_mode_battle_mgr_quotums', fields={'quotums': (fields.UniCapList(fieldOrSchema=quotumSchema, required=True, deserializedValidators=validate.Length(minValue=3)))}, modelClass=QuotumsModel, checkUnknown=True, deserializedValidators=[
 validatePriorityies], usedInReplay=True)
