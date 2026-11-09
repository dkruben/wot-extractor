# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/visual_script_client/contexts/vehicle_context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/contexts/vehicle_context.py
from __future__ import absolute_import
import weakref
from visual_script.context import VScriptContext, vse_get_property
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE

class VehicleContextClient(VScriptContext):

    def __init__(self, vehicle):
        super(VehicleContextClient, self).__init__(ASPECT.CLIENT)
        self._vehicle = vehicle

    def destroy(self):
        super(VehicleContextClient, self).destroy()
        self._vehicle = None
        return

    @vse_get_property(SLOT_TYPE.VEHICLE, display_name='Self', description='Return instance of current vehicle', aspects=[
     ASPECT.CLIENT])
    def getSelf(self):
        return weakref.proxy(self._vehicle)
