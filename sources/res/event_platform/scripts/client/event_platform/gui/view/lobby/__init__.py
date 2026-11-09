# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/event_platform/gui/view/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/event_platform/gui/view/lobby/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ViewSettings
from event_platform.gui.impl.event_hangar import EventHangar
from event_platform.gui.impl.lobby_cm import EPVehicleContextMenuHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE

def getContextMenuHandlers():
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.VEHICLE, EPVehicleContextMenuHandler),)


def getViewSettings():
    return (
     ViewSettings(VIEW_ALIAS.LOBBY_HANGAR, EventHangar, 'hangar.swf', WindowLayer.SUB_VIEW, VIEW_ALIAS.LOBBY_HANGAR, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getBusinessHandlers():
    return ()
