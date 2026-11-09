# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/controllers/fun_random_overlap_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/controllers/fun_random_overlap_controller.py
from __future__ import absolute_import
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin
from fun_random.gui.impl.lobby.hangar.states import DefaultFunRandomHangarState

class FunRandomOverlapCtrlMixin(OverlapCtrlMixin):

    def _onVisibleRouteChanged(self, routeInfo):
        defaultState = self._lobbyStateMachine.getStateByCls(DefaultFunRandomHangarState)
        self._isInHangar = routeInfo.state == defaultState
        self._updateViewModelIfNeeded()
