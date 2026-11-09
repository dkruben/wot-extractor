# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/serializable_types/customizations/insignia.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/insignia.py
from __future__ import absolute_import
from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from py2to3.patched_future import with_metaclass
from serialization.field import xmlOnlyIntField, xmlOnlyApplyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = ('InsigniaComponent', )

class InsigniaComponent(with_metaclass(ReflectionMetaclass, SerializableComponent)):
    customType = C11nSerializationTypes.INSIGNIA
    fields = OrderedDict((
     (
      'id', xmlOnlyIntField()),
     (
      'appliedTo', xmlOnlyApplyAreaEnumField(ApplyArea.NONE))))
    __slots__ = ('id', 'appliedTo')

    def __init__(self, id=0, appliedTo=ApplyArea.NONE):
        self.id = id
        self.appliedTo = appliedTo
        super(InsigniaComponent, self).__init__()

    def isGunInsignia(self):
        return self.appliedTo == ApplyArea.GUN
