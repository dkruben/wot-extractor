# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/shared/utils/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/shared/utils/__init__.py
from __future__ import absolute_import
from future.utils import viewvalues
import BigWorld
from LSAccountEquipmentController import getLSConsumables
import wg_async as future_async
from adisp import adisp_async
from last_stand.gui.shared.event_dispatcher import showAbilitiesIncompleteConfirm

def findMarkerEntity():
    return [e for e in BigWorld.entities.valuesOfType('EmptyEntity') if any(c.__class__.__name__ == 'EntityMarkerComponent' for c in viewvalues(e.dynamicComponents))]


@adisp_async
@future_async.wg_async
def checkAbilities(vehicle, callback):
    if vehicle:
        if any(not item for item in getLSConsumables(vehicle).installed):
            result = yield future_async.wg_await(showAbilitiesIncompleteConfirm())
            if result.busy or not result.result:
                callback(False)
                return
            toBattle, _ = result.result
            callback(toBattle)
        else:
            callback(True)
