# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/serialization/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/serialization/utils.py
from __future__ import absolute_import
from typing import Dict, Type
from .component_bin_deserializer import ComponentBinDeserializer
from .component_bin_serializer import ComponentBinSerializer
from .serializable_component import SerializableComponent, SerializableComponentChildType
__all__ = ('makeCompDescr', 'parseCompDescr')

def makeCompDescr(customizationItem):
    return ComponentBinSerializer().serialize(customizationItem)


def parseCompDescr(CUSTOMIZATION_CLASSES, customizationElementCompDescr):
    return ComponentBinDeserializer(CUSTOMIZATION_CLASSES).decode(customizationElementCompDescr)
