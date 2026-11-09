# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/base_child_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/base_child_presenter.py
from __future__ import absolute_import
from gui.impl.lobby.user_missions.hangar_widget.services import IUserMissionWidgetService
from helpers import dependency

class UserMissionChildPresenter(object):
    GROUP = ''
    _widgetService = dependency.descriptor(IUserMissionWidgetService)

    def isVisible(self):
        return True

    def _notifyVisibilityChanged(self):
        if not self.GROUP:
            return
        self._widgetService.setGroupVisibility(self.GROUP, self.isVisible())
