# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/hints_common/prebattle/manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/hints_common/prebattle/manager.py
from __future__ import absolute_import
import logging, typing
from future.utils import viewitems
from dict2model import exceptions
from hints_common.common.manager import BaseHintsModelsManager
from hints_common.prebattle.schemas import hintSchema, BaseHintSchema
if typing.TYPE_CHECKING:
    from hints_common.prebattle.schemas import BaseHintModel
_logger = logging.getLogger(__name__)
_g_manager = None
_HINTS_XML = 'scripts/item_defs/hints/prebattle_hints.xml'

class PrebattleHintsModelsManager(BaseHintsModelsManager):

    def __init__(self):
        self._hints = []
        super(PrebattleHintsModelsManager, self).__init__(_HINTS_XML, hintSchema)

    def iterHints(self):
        return iter(self._hints)

    def _checkSchemaType(self, schema):
        if not isinstance(schema, BaseHintSchema):
            raise exceptions.ValidationError(('Schema type must be {} or inherited.').format(BaseHintSchema))

    def _addToStorage(self, schema, model):
        self._hints.append(model)

    def _validateRegistered(self):
        errors = None
        for path, schema in viewitems(self._importedSchemas):
            try:
                schema.validateRegistered(list(self._hints))
            except exceptions.ValidationError as ve:
                error = exceptions.ValidationErrorMessage(ve.error.data, title=('{}').format(path))
                errors = errors + error if errors else error

        if errors:
            raise exceptions.ValidationError(errors)
        return


def init():
    global _g_manager
    if _g_manager is None:
        _g_manager = PrebattleHintsModelsManager()
        _logger.info('PrebattleHintsModelsManager created from: %s.', _HINTS_XML)
    return


def getInstance():
    if _g_manager is None:
        _logger.error('PrebattleHintsModelsManager not initialized.')
    return _g_manager
