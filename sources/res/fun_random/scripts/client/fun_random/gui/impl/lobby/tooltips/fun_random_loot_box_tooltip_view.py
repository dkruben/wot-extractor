# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_loot_box_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_loot_box_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_loot_box_tooltip_view_model import FunRandomLootBoxTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFunRandomBonusPacker
from fun_random.gui.impl.lobby.common.lootboxes import packLootboxRewards
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class FunRandomLootBoxTooltipView(ViewImpl, FunAssetPacksMixin):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.fun_random.mono.lobby.tooltips.loot_box_tooltip(), model=FunRandomLootBoxTooltipViewModel(), args=args, kwargs=kwargs)
        super(FunRandomLootBoxTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FunRandomLootBoxTooltipView, self).getViewModel()

    def _onLoading(self, lootboxTokenID, *args, **kwargs):
        super(FunRandomLootBoxTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            lb = self.__itemsCache.items.tokens.getLootBoxByTokenID(lootboxTokenID)
            lootBoxData = self.__lobbyContext.getServerSettings().getLootBoxesTooltipConfig().get(lb.getID())
            if lootBoxData and lb:
                model.setAssetsPointer(self.getModeAssetsPointer())
                model.setLabel(backport.text(R.strings.lootboxes.fepLootboxTitle(), lootboxName=backport.text(self.getModeLocalsResRoot().lootbox.dyn(lb.getType())())))
                model.setIconKey(lb.getType().split('_')[-1])
                packLootboxRewards(lootBoxData, model.getRewards(), getFunRandomBonusPacker())
