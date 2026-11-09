# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/gf_notifications/gf_notification_inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/gf_notifications/gf_notification_inject.py
import logging
from gui.shared.system_factory import collectGamefaceNotifications
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
_logger = logging.getLogger(__name__)

class GFNotificationInject(InjectComponentAdaptor):

    def __init__(self, gfViewName, isPopUp, linkageData, *args, **kwargs):
        self.__gfViewName = gfViewName
        self.__isPopUp = isPopUp
        self.__linkageData = linkageData
        super(GFNotificationInject, self).__init__()

    def _makeInjectView(self):
        resId, presenter = PresentersFactory.get(self.__gfViewName)
        return presenter(resId, self.__isPopUp, self.__linkageData)


class PresentersFactory(object):

    @staticmethod
    def get(gfTemplate):
        resId, clazz = collectGamefaceNotifications().get(gfTemplate, None)
        if clazz is not None:
            return (resId, clazz)
        else:
            _logger.error("can't fined presenter for %s", gfTemplate)
            return
