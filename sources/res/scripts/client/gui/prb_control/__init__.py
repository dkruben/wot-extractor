# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/__init__.py
import typing
if typing.TYPE_CHECKING:
    from typing import Any, Optional
    from gui.prb_control.dispatcher import _PreBattleDispatcher
    from gui.prb_control.entities.base.entity import BasePrbEntity

class prbDispatcherProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getDispatcher()


class prbEntityProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        dispatcher = g_prbLoader.getDispatcher()
        entity = None
        if dispatcher is not None:
            entity = dispatcher.getEntity()
        return entity


class prbPeripheriesHandlerProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getPeripheriesHandler()


class prbInvitesProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getInvitesManager()


class prbAutoInvitesProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getAutoInvitesNotifier()
