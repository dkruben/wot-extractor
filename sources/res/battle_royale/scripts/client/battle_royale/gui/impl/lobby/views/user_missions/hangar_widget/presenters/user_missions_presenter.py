# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/user_missions_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/user_missions_presenter.py
from __future__ import absolute_import
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.overlap_ctrl import BattleRoyaleOverlapCtrlMixin
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.event_shop_presenter import BattleRoyaleEventShopPresenter
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.progression_presenter import BattleRoyaleProgressionPresenter
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.quests_presenter import BattleRoayaleQuestsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter
from battle_royale.gui.impl.lobby.tooltips.battle_pass_in_progress_tooltip import BattleRoyaleBattlePassInProgressTooltipView
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter

class _BattlePassPresenter(BattlePassPresenter, BattleRoyaleOverlapCtrlMixin):

    def _createInProgressTooltipView(self):
        return BattleRoyaleBattlePassInProgressTooltipView()


class BattleRoyaleUserMissionsPresenter(UserMissionsPresenter):
    _WIDGET_ALIAS = R.aliases.user_missions.hangarWidget
    _BATTLE_ROYALE_WIDGET_ALIAS = R.aliases.battle_royale.hangarWidget
    _CHILDREN = {(_WIDGET_ALIAS.BattlePass()): _BattlePassPresenter, 
       (_WIDGET_ALIAS.Quests()): BattleRoayaleQuestsPresenter, 
       (_BATTLE_ROYALE_WIDGET_ALIAS.Progression()): BattleRoyaleProgressionPresenter, 
       (_BATTLE_ROYALE_WIDGET_ALIAS.EventShop()): BattleRoyaleEventShopPresenter}

    def _addChild(self, posId):
        uid = self._childrenUidByPosition.get(posId)
        if self._childrenByUid.get(uid):
            return
        super(BattleRoyaleUserMissionsPresenter, self)._addChild(posId)
