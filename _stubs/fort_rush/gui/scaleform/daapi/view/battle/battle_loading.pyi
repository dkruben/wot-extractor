# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/battle_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from account_helpers.settings_core.options import BattleLoadingTipSetting as BattleLoadingTipSetting
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading as BattleLoading
_FORT_RUSH_TIP_ICONS: Any
_FORT_RUSH_TIP_TEXT: tuple

class FortRushBattleLoading(BattleLoading):
    __tipIndex: Any
    __tipIcon: Any
    def __init__(self):
        ...
    def _setTipsInfo(self):
        ...
    def _makeVisualTipVO(self, arenaDP, tip=None):
        ...
