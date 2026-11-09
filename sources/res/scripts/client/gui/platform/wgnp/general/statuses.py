# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/wgnp/general/statuses.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/general/statuses.py
import typing
from gui.platform.base.response import Codes
from gui.platform.base.statuses.constants import StatusTypes
from gui.platform.base.statuses.status import Status
if typing.TYPE_CHECKING:
    from gui.platform.wgnp.general.request import AccountCountryParams

class GeneralAccountCountryStatus(Status):
    __slots__ = ()

    @property
    def country(self):
        return self.data.get('country', '')


def createAccountCountryStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        data = response.getData()
        if data:
            statusType = StatusTypes.ADDED
    else:
        data = {'error': (Codes(response.code))}
    return GeneralAccountCountryStatus(statusType=statusType, data=data)
