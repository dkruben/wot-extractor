# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/tooltips/battle_royale_completed_quest_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/tooltips/battle_royale_completed_quest_tooltip.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.tooltips import TOOLTIP_TYPE, formatters
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController
from gui.server_events import IEventsCache
from battle_royale.gui.Scaleform.daapi.view.lobby.tooltips.battle_royale_tooltip_quest_helper import getQuestTooltipBlock

class BattleRoyaleQuestsTooltip(BlocksTooltipData):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __eventsCache = dependency.descriptor(IEventsCache)
    __slots__ = ()

    def __init__(self, context):
        super(BattleRoyaleQuestsTooltip, self).__init__(context, TOOLTIP_TYPE.EPIC_QUESTS)
        self._setContentMargin(top=0, left=0, bottom=0, right=0)
        self._setMargins(afterBlock=0)
        self._setWidth(320)

    def _packBlocks(self, *args, **kwargs):
        allQuests = self.__eventsCache.getAllQuests()
        quests = [allQuests.get(qId) for qId in args[1]]
        if quests:
            return [
             self._packHeader()] + [getQuestTooltipBlock(q) for q in quests]
        return super(BattleRoyaleQuestsTooltip, self)._packBlocks()

    def _packHeader(self):
        if self.__battleRoyaleController.isStPatrick():
            bgImage = R.images.battle_royale.gui.maps.st_patrick.icons.quests_tooltip_bg()
        else:
            bgImage = R.images.battle_royale.gui.maps.icons.quests_tooltip_bg()
        return formatters.packImageTextBlockData(title=text_styles.highTitle(backport.text(R.strings.epic_battle.questsTooltip.epicBattle.steelhunter.header())), img=backport.image(bgImage), txtPadding=formatters.packPadding(top=18, bottom=-12), txtOffset=20)
