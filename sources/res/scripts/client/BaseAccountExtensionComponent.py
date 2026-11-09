# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/BaseAccountExtensionComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/BaseAccountExtensionComponent.py
from __future__ import absolute_import
import BigWorld
from helpers import isPlayerAccount

class BaseAccountExtensionComponent(BigWorld.StaticScriptComponent):

    @property
    def account(self):
        return self.entity

    @property
    def base(self):
        return self.account.base

    @classmethod
    def instance(cls):
        playerAccount = BigWorld.player()
        if isPlayerAccount() and cls.__name__ in playerAccount.components:
            return getattr(playerAccount, cls.__name__, None)
        else:
            return
