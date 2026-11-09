# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/prb_control/entities/__init__.py
from __future__ import absolute_import
from adisp import adisp_process
from halloween.gui.shared import utils

def vehicleAbilitiesCheck(func):
    from CurrentVehicle import g_currentVehicle

    @adisp_process
    def wrapper(*args, **kwargs):
        res = yield utils.checkAbilities(g_currentVehicle.item)
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


@adisp_process
def checkVehicleAbilitiesFull(vehicle, callback=None):
    result = yield utils.checkAbilities(vehicle)
    callback(result)
