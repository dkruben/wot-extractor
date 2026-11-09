# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/managers/TutorialManager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/managers/TutorialManager.py
from __future__ import absolute_import
from Event import Event, EventManager
from gui.Scaleform.framework.entities.abstract.TutorialManagerMeta import TutorialManagerMeta

class ScaleformTutorialManager(TutorialManagerMeta):

    def __init__(self):
        super(ScaleformTutorialManager, self).__init__()
        self.__eventMgr = EventManager()
        self.onComponentFoundEvent = Event(self.__eventMgr)
        self.onComponentDisposedEvent = Event(self.__eventMgr)
        self.onTriggerActivatedEvent = Event(self.__eventMgr)
        self.onEffectCompletedEvent = Event(self.__eventMgr)

    def _dispose(self):
        self.__eventMgr.clear()
        super(ScaleformTutorialManager, self)._dispose()

    def onComponentFound(self, componentId, viewTutorialId):
        self.onComponentFoundEvent(componentId, viewTutorialId)

    def onTriggerActivated(self, componentId, triggerId, state):
        self.onTriggerActivatedEvent(componentId, triggerId, state)

    def onComponentDisposed(self, componentId):
        self.onComponentDisposedEvent(componentId)

    def onEffectCompleted(self, componentId, effectType):
        self.onEffectCompletedEvent(componentId, effectType)
