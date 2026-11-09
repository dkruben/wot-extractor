# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/WaitingView.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/WaitingView.py
from __future__ import absolute_import
import Keys
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui import InputHandler
from gui.Scaleform.daapi.view.meta.WaitingViewMeta import WaitingViewMeta
from gui.impl import backport
from skeletons.gui.app_loader import IWaitingWidget

class WaitingView(WaitingViewMeta, IWaitingWidget):

    def __init__(self, **kwargs):
        super(WaitingView, self).__init__()
        InputHandler.g_instance.onKeyUp += self.handleKeyUpEvent
        self.__callback = None
        return

    def handleKeyUpEvent(self, event):
        if event.key == Keys.KEY_ESCAPE:
            if self.__callback:
                self.__callback()

    def destroy(self):
        self.__callback = None
        InputHandler.g_instance.onKeyUp -= self.handleKeyUpEvent
        super(WaitingView, self).destroy()
        return

    def setCallback(self, callback=None):
        self.__callback = callback

    def cancelCallback(self):
        self.__callback = None
        return

    def showWaiting(self, messageID, softStart=False, showBg=True):
        self.as_showWaitingS(backport.text(messageID), softStart, showBg)

    def hideWaiting(self):
        self.__callback = None
        try:
            self.as_hideWaitingS()
        except Exception:
            LOG_ERROR('There is error while trying to close waiting')
            LOG_CURRENT_EXCEPTION()

        return

    def setBackgroundImage(self, image):
        if image:
            self.as_showBackgroundImgS(image)
