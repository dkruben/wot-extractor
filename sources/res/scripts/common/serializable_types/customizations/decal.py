# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/serializable_types/customizations/decal.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/decal.py
from __future__ import absolute_import
from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from py2to3.patched_future import with_metaclass
from typing import Dict
from serialization.field import intField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = ('DecalComponent', )

class DecalComponent(with_metaclass(ReflectionMetaclass, SerializableComponent)):
    customType = C11nSerializationTypes.DECAL
    fields = OrderedDict((
     (
      'id', intField()),
     (
      'appliedTo', applyAreaEnumField(ApplyArea.NONE)),
     (
      'progressionLevel', intField(0))))
    __slots__ = ('id', 'appliedTo', 'progressionLevel')

    def __init__(self, id=0, appliedTo=ApplyArea.NONE, progressionLevel=0):
        self.id = id
        self.appliedTo = appliedTo
        self.progressionLevel = progressionLevel
        super(DecalComponent, self).__init__()

    def toDict(self):
        at = self.appliedTo
        p = self.id
        return {i: p for i in ApplyArea.RANGE if i & at}
