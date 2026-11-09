# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/winback.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/winback.py
from __future__ import absolute_import
import typing, AccountCommands
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

class Winback(object):

    def __init__(self, commandsProxy):
        self.__commandsProxy = commandsProxy

    def turnOffBattles(self, reason, callback):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)
        else:
            proxy = None
        self.__commandsProxy.perform(AccountCommands.CMD_TURNOFF_WINBACK_BATTLES, reason, proxy)
        return
