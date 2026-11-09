# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/game_params_common/schema.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/game_params_common/schema.py
from __future__ import absolute_import
import typing
from constants import IS_CLIENT, IS_BASEAPP, IS_CELLAPP
from dict2model.schemas import Schema, SchemaModelType
from dict2model.types import SchemaModelClassesType, ValidatorsType
if typing.TYPE_CHECKING:
    from dict2model.fields import Field
    from section2dict import TReaders

class GameParamsSchema(Schema[SchemaModelType]):
    __slots__ = ('readers', 'usedInReplay', '_gameParamsKey')

    def __init__(self, gameParamsKey, fields, modelClass=dict, checkUnknown=True, serializedValidators=None, deserializedValidators=None, readers=None, usedInReplay=False):
        super(GameParamsSchema, self).__init__(fields=fields, modelClass=modelClass, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self.readers = readers
        self.usedInReplay = usedInReplay
        self._gameParamsKey = gameParamsKey

    @property
    def gpKey(self):
        return self._gameParamsKey

    def getModel(self, **kwargs):
        if not IS_CLIENT and not IS_BASEAPP and not IS_CELLAPP:
            raise NotImplementedError
        from schema_manager import getSchemaManager
        return getSchemaManager().getModel(self, **kwargs)
