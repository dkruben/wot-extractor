# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/ResourceWellAccountComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/ResourceWellAccountComponent.py
from __future__ import absolute_import
import json, typing
from resource_well_common.resource_well_account_commands import CMD_RESOURCE_WELL_PUT, CMD_RESOURCE_WELL_TAKE
import AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
if typing.TYPE_CHECKING:
    from typing import Callable, Optional, List, Tuple

def _getAccountRepository():
    import Account
    return Account.g_accountRepository


class ResourceWellAccountComponent(BaseAccountExtensionComponent):

    def putResources(self, resources, reward, callback):
        repository = _getAccountRepository()
        if repository is None:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 'NON_PLAYER', None)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext)
        else:
            proxy = None
        resourcesStr = json.dumps(resources)
        repository.commandProxy.perform(CMD_RESOURCE_WELL_PUT, [reward, resourcesStr], proxy)
        return

    def takeBack(self, callback):
        repository = _getAccountRepository()
        if repository is None:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        proxy = (lambda requestID, resultID, errorStr, ext={}: callback(resultID)) if callback is not None else None
        repository.commandProxy.perform(CMD_RESOURCE_WELL_TAKE, 0, proxy)
        return
