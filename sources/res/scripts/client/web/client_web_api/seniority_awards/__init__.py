# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/client_web_api/seniority_awards/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/seniority_awards/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController
from web.client_web_api.api import C2WHandler, c2w

class SeniorityAwardsEventHandler(C2WHandler):
    __seniorityAwardsCtrl = dependency.descriptor(ISeniorityAwardsController)

    def init(self):
        super(SeniorityAwardsEventHandler, self).init()
        self.__seniorityAwardsCtrl.onVehicleSelectionChanged += self.__seniorityAwardsVehicleSelectionUpdated

    def fini(self):
        self.__seniorityAwardsCtrl.onVehicleSelectionChanged -= self.__seniorityAwardsVehicleSelectionUpdated
        super(SeniorityAwardsEventHandler, self).fini()

    @c2w(name='seniority_awards_vehicle_selection_changed')
    def __seniorityAwardsVehicleSelectionUpdated(self, *args):
        return {'isVehicleSelectionAvailable': (self.__seniorityAwardsCtrl.isVehicleSelectionAvailable)}
