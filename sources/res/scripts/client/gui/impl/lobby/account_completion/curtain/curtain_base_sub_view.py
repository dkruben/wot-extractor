# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_completion/curtain/curtain_base_sub_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/curtain/curtain_base_sub_view.py
import typing
from typing import Type
from Event import Event
from frameworks.wulf import ViewModel, ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
if typing.TYPE_CHECKING:
    from frameworks.wulf import PyResAccessor

class CurtainBaseSubView(ViewImpl):
    __slots__ = ('_isActive', '_isHidden', 'onWaitingChanged', '_isWaitingVisible',
                 '_waitingMsgResID')
    _LAYOUT_DYN_ACCESSOR = R.invalid
    _VIEW_MODEL_CLASS = ViewModel

    def __init__(self):
        settings = ViewSettings(self._LAYOUT_DYN_ACCESSOR())
        settings.model = self._VIEW_MODEL_CLASS()
        super(CurtainBaseSubView, self).__init__(settings)
        self._isActive = False
        self._isHidden = False
        self.onWaitingChanged = Event()
        self._isWaitingVisible = False
        self._waitingMsgResID = R.invalid()

    @property
    def isActive(self):
        return self._isActive

    @property
    def isWaitingVisible(self):
        return self._isWaitingVisible

    @property
    def waitingMsgResID(self):
        return self._waitingMsgResID

    @property
    def isHidden(self):
        return self._isHidden

    def activate(self, *args, **kwargs):
        self._isActive = True

    def deactivate(self):
        self._isActive = False

    def hide(self):
        self._isHidden = True

    def reveal(self):
        self._isHidden = False

    def _finalize(self):
        if self._isActive:
            self.deactivate()
        self._doFinalize()
        super(CurtainBaseSubView, self)._finalize()

    def _doFinalize(self):
        pass

    def _setWaiting(self, isVisible, msgResID=R.invalid()):
        self._isWaitingVisible = isVisible
        self._waitingMsgResID = msgResID
        self.onWaitingChanged(isVisible, msgResID)
