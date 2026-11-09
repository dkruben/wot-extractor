# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/gsw_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/widgets/gsw_view.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.lobby.gsw_cards.key_card_presenter import KeyCardPresenter
from halloween.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestsCardPresenter
from halloween.gui.impl.lobby.gsw_cards.reward_path_presenter import RewardPathCardPresenter
from halloween.gui.impl.lobby.gsw_cards.shop_card_presenter import ShopCardPresenter
from halloween.uilogging.logging_constants import HWLogKeys

class GswPresenter(ViewComponent):

    def _getChildComponents(self):
        halloween = R.aliases.halloween.shared
        return {(halloween.Shop()): ShopCardPresenter, 
           (halloween.Keys()): (lambda : KeyCardPresenter(HWLogKeys.HW_HANGAR_UMG_WIDGET.value)), 
           (halloween.RewardPath()): RewardPathCardPresenter, 
           (halloween.Quests()): (lambda : QuestsCardPresenter(isGSW=True))}
