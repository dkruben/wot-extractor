# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/serialization/component_xml_deserializer.pyc (uncompyle6 3.9.3 / Python 3.14.3) - nao e o codigo original
# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
# Embedded file name: scripts/common/serialization/component_xml_deserializer.py
from __future__ import absolute_import
from typing import Tuple, Any
from future.utils import iteritems
import ResMgr
from constants import IS_EDITOR
from items import decodeEnum
from items.components.c11n_constants import ApplyArea, Options
from items.utils import getEditorOnlySection
from serialization.definitions import FieldFlags, FieldTypes
from serialization.exceptions import SerializationException
from serialization.serializable_component import SerializableComponent
__all__ = ('ComponentXmlDeserializer', )

class ComponentXmlDeserializer(object):
    __slots__ = ('customTypes', )

    def __init__(self, customTypes):
        self.customTypes = customTypes
        super(ComponentXmlDeserializer, self).__init__()
        return

    def decode(self, itemType, xmlCtx, section):
        obj = self.__decodeCustomType(itemType, xmlCtx, section)
        return obj

    def __decodeCustomTypeParse error at or near `LOAD_FAST' instruction at offset 0

    def __decodeArray(self, itemType, ctx, section):
        result = []
        for iname, isection in section.items():
            if itemType == FieldTypes.VARINT:
                result.append(isection.asInt)
            elif itemType == FieldTypes.FLOAT:
                result.append(isection.asFloat)
            elif itemType >= FieldTypes.CUSTOM_TYPE_OFFSET:
                customType = itemType // FieldTypes.CUSTOM_TYPE_OFFSET
                ictx = (ctx, ('{0} {1}').format(iname, isection))
                result.append(self.__decodeCustomType(customType, ictx, isection))
            else:
                raise SerializationException('Unsupported item type')

        return result

    def __decodeEnum(self, value, enum):
        return decodeEnum(value, enum)[0]


return
# wot-extractor: AVISO - descompilacao partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 31)
