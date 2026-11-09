# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/br_season_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/br_season_provider.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController
from constants import GameSeasonType
from gui.shared.system_factory import registerSeasonProviderHandler

def registerBRSeasonProviderHandler():
    registerSeasonProviderHandler(GameSeasonType.BATTLE_ROYALE, (lambda *args, **kwargs: dependency.instance(IBattleRoyaleController)))
