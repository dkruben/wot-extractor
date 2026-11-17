# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/tooltips/epic_battle_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel as ConsumablesPanel
from gui.app_loader import sf_battle as sf_battle
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from constants import PLAYER_RANK as PLAYER_RANK
from gui.battle_control.controllers.epic_missions_ctrl import RANK_TO_TRANSLATION as RANK_TO_TRANSLATION
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class EpicRankUnlockTooltipData(BlocksTooltipData):
    _RANK_LEVEL_AVAILABLE_TOOLTIP: tuple
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class _FLRandomReserveContext(ConsumablesPanel):
    __sessionProvider: Any
    _EQUIPMENT_ARG = 0
    # decorador original: @sf_battle
    def app(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getComponent(self):
        ...
