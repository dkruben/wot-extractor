# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/hangar_selectable_objects/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/hangar_selectable_objects/interfaces.py


class ISelectableObject(object):

    def __init__(self):
        super(ISelectableObject, self).__init__()
        if not hasattr(self, 'selectionId'):
            self.selectionId = ''
        if not hasattr(self, 'mouseOverSoundName'):
            self.mouseOverSoundName = ''

    @property
    def enabled(self):
        raise NotImplementedError

    def setEnable(self, enabled):
        raise NotImplementedError

    def setHighlight(self, show):
        raise NotImplementedError

    def onMouseDown(self):
        pass

    def onMouseUp(self):
        pass

    def onMouseClick(self):
        pass


class ISelectableLogic(object):
    __slots__ = ()

    def init(self, callback=None):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def _onMouseEnter(self, entity):
        raise NotImplementedError

    def _onMouseExit(self, entity):
        raise NotImplementedError

    def _onMouseDown(self):
        raise NotImplementedError

    def _onMouseUp(self):
        raise NotImplementedError

    def _onNotifyCursorOver3dScene(self, isCursorOver3dScene):
        raise NotImplementedError

    def _filterEntity(self, entity):
        raise NotImplementedError


class ISelectableLogicCallback(object):

    def onHighlight3DEntity(self, entity):
        raise NotImplementedError

    def onFade3DEntity(self, entity):
        raise NotImplementedError
