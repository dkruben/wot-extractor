# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/shared/utils/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/shared/utils/__init__.py
from __future__ import absolute_import
import BigWorld, wg_async as future_async
from adisp import adisp_async
from halloween.gui.shared.event_dispatcher import showAbilitiesIncompleteConfirm

def findMarkerEntity():
    return [e for e in BigWorld.entities.valuesOfType('EmptyEntity') if any(c.__class__.__name__ == 'EntityMarkerComponent' for c in e.dynamicComponents.values())]


@adisp_async
@future_async.wg_async
def checkAbilities(vehicle, callback):
    if vehicle:
        if any(not item for item in vehicle.consumables.installed):
            result = yield future_async.wg_await(showAbilitiesIncompleteConfirm())
            if result.busy or not result.result:
                callback(False)
                return
            toBattle, _ = result.result
            callback(toBattle)
        else:
            callback(True)
