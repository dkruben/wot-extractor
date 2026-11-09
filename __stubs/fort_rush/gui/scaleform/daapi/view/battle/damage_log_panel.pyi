# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/damage_log_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.avatar_getter import getPlayerVehicleID as getPlayerVehicleID
from gui.impl import backport as backport
from fort_rush.gui.scaleform.daapi.view.meta.FortRushDamageLogPanelMeta import FortRushDamageLogPanelMeta as FortRushDamageLogPanelMeta
from fort_rush_common.component_helpers import getScoreComponent as getScoreComponent

class FortRushDamagePanel(FortRushDamageLogPanelMeta):
    _scoreComponent: Any
    _totalScore: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleFortRushPersonalScoreUpdateEvent(self, scores):
        ...
