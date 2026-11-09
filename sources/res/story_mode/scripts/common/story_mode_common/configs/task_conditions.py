# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/common/story_mode_common/configs/task_conditions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/common/story_mode_common/configs/task_conditions.py
from __future__ import absolute_import
import enum
from dict2model import fields
from visual_script.slot_types import SLOT_TYPE

@enum.unique
class TaskConditionType(str, enum.Enum):
    INT = 'int'
    FLOAT = 'float'

    def getSchemaFieldType(self):
        return _VALUE_FIELD_BY_TYPE[self]

    def getVseSlotType(self):
        return _VSE_SLOT_BY_TYPE[self]


_VALUE_FIELD_BY_TYPE = {(TaskConditionType.INT): (fields.Integer(required=True)), 
   (TaskConditionType.FLOAT): (fields.Float(required=True))}
_VSE_SLOT_BY_TYPE = {(TaskConditionType.INT): (SLOT_TYPE.INT), 
   (TaskConditionType.FLOAT): (SLOT_TYPE.FLOAT)}
