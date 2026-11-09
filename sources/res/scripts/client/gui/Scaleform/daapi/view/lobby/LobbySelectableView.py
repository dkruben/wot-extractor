# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/LobbySelectableView.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/LobbySelectableView.py
from __future__ import absolute_import
from gui.Scaleform.daapi import LobbySubView
from hangar_selectable_objects import ISelectableLogicCallback, HangarSelectableLogic

class LobbySelectableView(LobbySubView, ISelectableLogicCallback):

    def __init__(self, ctx=None):
        super(LobbySelectableView, self).__init__(ctx)
        self.__selectableLogic = None
        return

    def onHighlight3DEntity(self, entity):
        self._highlight3DEntityAndShowTT(entity)

    def onFade3DEntity(self, entity):
        self._fade3DEntityAndHideTT(entity)

    def _populate(self):
        super(LobbySelectableView, self)._populate()
        self._activateSelectableLogic()

    def _dispose(self):
        self._deactivateSelectableLogic()
        super(LobbySelectableView, self)._dispose()

    def _highlight3DEntityAndShowTT(self, entity):
        pass

    def _fade3DEntityAndHideTT(self, entity):
        pass

    def _activateSelectableLogic(self):
        if self.__selectableLogic is not None:
            return
        else:
            self.__selectableLogic = self._createSelectableLogic()
            self.__selectableLogic.init(self)
            return

    def _deactivateSelectableLogic(self):
        if self.__selectableLogic is not None:
            self.__selectableLogic.fini()
            self.__selectableLogic = None
        return

    def _createSelectableLogic(self):
        return HangarSelectableLogic()
