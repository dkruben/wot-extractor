# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/user_missions_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/presenters/user_missions_presenter.py
from __future__ import absolute_import
from frontline.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import FLOverlapCtrlMixin
from frontline.gui.impl.lobby.views.frontline_event_widget import FrontlineEventWidget
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter

class _BattlePassPresenter(BattlePassPresenter, FLOverlapCtrlMixin):
    pass


class FrontlineUserMissionsPresenter(UserMissionsPresenter):
    _CHILDREN = {(R.aliases.user_missions.hangarWidget.BattlePass()): _BattlePassPresenter, 
       (R.aliases.user_missions.hangarWidget.Events()): FrontlineEventWidget}
