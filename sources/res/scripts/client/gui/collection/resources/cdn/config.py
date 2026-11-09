# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/collection/resources/cdn/config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/cdn/config.py
import typing
from dict2model import fields, schemas, validate
from gui.collection.resources.cdn.models import ConfigModel, Group, ImageModel, Sub
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
imageSchema = schemas.Schema(fields={'group': (fields.StrEnum(Group, required=True)), 
   'sub': (fields.StrEnum(Sub, required=True)), 
   'name': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   'url': (fields.Url(required=True, relative=False))}, modelClass=ImageModel, checkUnknown=True)
configSchema = schemas.Schema(fields={'images': (fields.List(fieldOrSchema=imageSchema, required=True))}, modelClass=ConfigModel, checkUnknown=True)

def createConfigModel(rawData):
    return configSchema.deserialize(rawData, silent=True)
