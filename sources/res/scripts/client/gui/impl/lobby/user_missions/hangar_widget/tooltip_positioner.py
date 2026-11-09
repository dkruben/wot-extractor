# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/tooltip_positioner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/tooltip_positioner.py
VIEW_OVERLAPPED = 'viewOverlapped'

class TooltipPositionerMixin(object):

    def __onWindowPositionChanged(self, uniqueID, *_):
        window = self.gui.windowsManager.getWindow(uniqueID)
        if window:
            window.onPositionChanged -= self.__onWindowPositionChanged
            if self.__positionX and self.__positionY:
                width, __ = window.size
                window.move(int(self.__positionX) - int(width), int(self.__positionY))

    def createToolTip(self, event):
        if self.hasDeferModelUpdate:
            return VIEW_OVERLAPPED
        window = super(TooltipPositionerMixin, self).createToolTip(event)
        if window:
            self.__positionX = event.getArgument('positionX')
            self.__positionY = event.getArgument('positionY')
            window.onPositionChanged += self.__onWindowPositionChanged
        return window
