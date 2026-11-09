# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/OpenBundleAccountComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/OpenBundleAccountComponent.py
from __future__ import absolute_import
import typing, AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from open_bundle_common.open_bundle_account_commands import CMD_OPEN_BUNDLE_PROCESS_NEXT_STEP
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

def _getAccountRepository():
    import Account
    return Account.g_accountRepository


class OpenBundleAccountComponent(BaseAccountExtensionComponent):

    def processNextStep(self, bundleID, stepNumber, callback):
        repository = _getAccountRepository()
        if repository is None:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 'NON_PLAYER', None)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext)
        else:
            proxy = None
        repository.commandProxy.perform(CMD_OPEN_BUNDLE_PROCESS_NEXT_STEP, bundleID, stepNumber, proxy)
        return
