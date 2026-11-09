# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/pop_over_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/pop_over_window.py
from __future__ import absolute_import
import typing
from frameworks.wulf import WindowFlags, ViewFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.windows.pop_over_window_model import PopOverWindowModel
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView

class PopOverWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, event, content, parent, layer=WindowLayer.UNDEFINED, direction=None):
        super(PopOverWindow, self).__init__(wndFlags=WindowFlags.POP_OVER, decorator=WindowView(layoutID=event.decoratorID, flags=ViewFlags.POP_OVER_DECORATOR, viewModelClazz=PopOverWindowModel), content=content, parent=parent, areaID=R.areas.pop_over(), layer=layer)
        with self.popOverModel.transaction() as tx:
            tx.setBoundX(event.bbox.positionX)
            tx.setBoundY(event.bbox.positionY)
            tx.setBoundWidth(event.bbox.width)
            tx.setBoundHeight(event.bbox.height)
            tx.setDirectionType(direction or event.direction)
            tx.setIsCloseBtnVisible(content.isCloseBtnVisible)

    @property
    def popOverModel(self):
        return super(PopOverWindow, self)._getDecoratorViewModel()
