# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/hints/battle/manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/hints/battle/manager.py
from __future__ import absolute_import
import typing
from hints_common.battle import manager
from hints.battle.schemas.base import clientHintSchema
if typing.TYPE_CHECKING:
    from hints.battle.schemas.base import CHMType
SCHEMA_TAG = 'clientSchema'

def init():
    manager.init(schemaTag=SCHEMA_TAG, defaultSchema=clientHintSchema)


def get():
    return manager.get()
