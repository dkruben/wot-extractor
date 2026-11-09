# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/notification/decorators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/notification/decorators.py
from __future__ import absolute_import
from gui.shared.notifications import NotificationGuiSettings, NotificationPriorityLevel
from helpers import dependency
from messenger import g_settings
from notification.decorators import MessageDecorator
from notification.settings import NOTIFICATION_TYPE, NOTIFICATION_BUTTON_STATE
from skeletons.gui.resource_well import IResourceWellController

class ResourceWellLockButtonDecorator(MessageDecorator):
    __resourceWell = dependency.descriptor(IResourceWellController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(ResourceWellLockButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.__resourceWell.onEventUpdated += self.__update
        self.__resourceWell.onSettingsChanged += self.__update

    def clear(self):
        self.__resourceWell.onEventUpdated -= self.__update
        self.__resourceWell.onSettingsChanged -= self.__update

    def _make(self, entity=None, settings=None):
        self.__updateEntityButtons()
        super(ResourceWellLockButtonDecorator, self)._make(entity, settings)

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            if self.__resourceWell.isActive():
                state = NOTIFICATION_BUTTON_STATE.DEFAULT
            else:
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
            self._entity['buttonsStates'] = {'submit': state}
            return

    def __update(self, *_):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class ResourceWellStartDecorator(ResourceWellLockButtonDecorator):

    def __init__(self, entityID, message, model):
        super(ResourceWellStartDecorator, self).__init__(entityID, self.__makeEntity(message), self.__makeSettings(), model)

    def getType(self):
        return NOTIFICATION_TYPE.RESOURCE_WELL_START

    def __makeEntity(self, message):
        return g_settings.msgTemplates.format('ResourceWellStartSysMessage', ctx=message)

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.HIGH)
