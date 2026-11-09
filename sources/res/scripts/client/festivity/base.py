# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/festivity/base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/base.py
from __future__ import absolute_import
import logging
from pprint import pformat
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
_logger = logging.getLogger(__name__)

def _defaultLogger(*args):
    msg = pformat(args)
    _logger.debug('[SERVER CMD RESPONSE]:%s', msg)


def _getProxy(callback):
    if callback is not None:
        return (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext))
    else:
        return


class BaseFestivityRequester(AbstractSyncDataRequester):
    dataKey = None

    def _requestCache(self, callback=None):
        BigWorld.player().festivities.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        festivityData = data.get(self.dataKey, {})
        return dict(festivityData)


class BaseFestivityProcessor(object):

    def __init__(self):
        super(BaseFestivityProcessor, self).__init__()
        self.__commandProxy = None
        return

    def setCommandProxy(self, account):
        self.__commandProxy = account

    def _perform(self, command, argsList, callback=None):
        if self.__commandProxy is not None:
            cmdArgs = argsList + (_getProxy(callback) if callback else _defaultLogger,)
            self.__commandProxy.perform(command, *cmdArgs)
        else:
            _logger.info('Festivity command can not be invoked due to proxy is not defined: cmd = %d, args = %r', command, argsList)
        return
