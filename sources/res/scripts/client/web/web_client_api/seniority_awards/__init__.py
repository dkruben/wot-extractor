# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/seniority_awards/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/seniority_awards/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController
from gui.shared.event_dispatcher import showSeniorityRewardVehiclesWindow
from web.web_client_api import w2capi, w2c, W2CSchema

@w2capi(name='seniority_awards', key='action')
class SeniorityAwardsWebApi(object):
    __seniorityAwardsCtrl = dependency.descriptor(ISeniorityAwardsController)

    @w2c(W2CSchema, 'is_vehicle_selection_available')
    def isVehicleSelectionAvailable(self, _):
        return {'isVehicleSelectionAvailable': (self.__seniorityAwardsCtrl.isVehicleSelectionAvailable)}


class OpenSeniorityAwardsWebApi(object):

    @w2c(W2CSchema, 'seniority_vehicle_selection')
    def showSeniorityVehicleSelectionWindow(self, _):
        showSeniorityRewardVehiclesWindow()
