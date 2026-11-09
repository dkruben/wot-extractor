# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/telecom_rentals/web_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/telecom_rentals/web_handlers.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import showHangar, showTelecomRentalPage
from web.web_client_api import Schema2Command, webApiCollection
from web.web_client_api.ui import OpenTabWebApi

class _OpenTabWebApi(OpenTabWebApi):

    def _getVehiclePreviewReturnAlias(self, cmd):
        return VIEW_ALIAS.RENTAL_VEHICLE_PREVIEW

    def _getVehiclePreviewReturnCallback(self, cmd):
        return self.__getReturnCallback(cmd)

    def _getVehicleStylePreviewCallback(self, cmd):
        return self.__getReturnCallback(cmd)

    def __getReturnCallback(self, cmd):

        def _returnToVehicleRental():
            showHangar()
            showTelecomRentalPage()

        return _returnToVehicleRental


_NAME_TO_API_MAP = {'open_tab': _OpenTabWebApi}

def replaceHandlers(handlers):
    handlersToReplace = [e for e in handlers if e.name in _NAME_TO_API_MAP.keys()]
    for element in handlersToReplace:
        handlers.remove(element)

    newHandlers = webApiCollection(*_NAME_TO_API_MAP.values())
    handlers.extend(newHandlers)
