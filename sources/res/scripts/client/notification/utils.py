# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/notification/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/notification/utils.py
from __future__ import absolute_import
import typing
from frameworks.wulf import WindowLayer
from gui.impl.lobby.gf_notifications import GFNotificationInject
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent
    from typing import Dict, Any

def dynamicNotificationRegister(owner, component, alias, gfViewName, isPopUp, linkageData, onDone):
    idx = WindowLayer.UNDEFINED
    guiLoader = dependency.instance(IGuiLoader)
    componentPy = guiLoader.entitiesFactory.initialize(GFNotificationInject(gfViewName, isPopUp, linkageData), component, idx)
    owner.components[alias] = componentPy
    componentPy.setEnvironment(owner.app)
    componentPy.create()
    g_eventBus.handleEvent(events.ComponentEvent(events.ComponentEvent.COMPONENT_REGISTERED, owner, componentPy, alias), EVENT_BUS_SCOPE.GLOBAL)
    onDone(componentPy, alias)
