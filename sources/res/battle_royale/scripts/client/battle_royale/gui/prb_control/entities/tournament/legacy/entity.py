# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/legacy/entity.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/legacy/entity.py
from __future__ import absolute_import
from helpers import dependency
from gui.prb_control import prb_getters
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.prb_control.entities.base.legacy.entity import LegacyEntryPoint
from skeletons.gui.game_control import IBattleRoyaleTournamentController
from gui.prb_control.items import prb_seqs

class BattleRoyaleTournamentEntryPoint(LegacyEntryPoint):
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController)

    def __init__(self):
        super(BattleRoyaleTournamentEntryPoint, self).__init__(FUNCTIONAL_FLAG.BATTLE_ROYALE)

    def join(self, ctx, callback=None):
        prbID = int(ctx.getID())
        item = prb_seqs.AutoInviteItem(prbID, **prb_getters.getPrebattleAutoInvites().get(prbID, {}))
        self.__battleRoyaleTournamentController.join(item.addInfo)
