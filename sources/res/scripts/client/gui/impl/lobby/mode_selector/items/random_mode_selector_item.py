# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/random_mode_selector_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/random_mode_selector_item.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_random_battle_model import ModeSelectorRandomBattleModel
from gui.impl.lobby.mode_selector.items import setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID

class RandomModeSelectorItem(ModeSelectorLegacyItem):
    __slots__ = ()
    _VIEW_MODEL = ModeSelectorRandomBattleModel
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.RANDOM

    @property
    def viewModel(self):
        return super(RandomModeSelectorItem, self).viewModel

    def _onInitializing(self):
        super(RandomModeSelectorItem, self)._onInitializing()
        self._addReward(ModeSelectorRewardID.CREDITS)
        self._addReward(ModeSelectorRewardID.EXPERIENCE)
        setBattlePassState(self.viewModel)
