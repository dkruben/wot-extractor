# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/tooltips/comp7_light_selector_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7_light.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.tooltips.battle_selector import SeasonalBattleSelectorTooltip as SeasonalBattleSelectorTooltip
_R_COMP7_LIGHT_SELECTOR_TOOLTIP = R.strings.comp7_light.selectorTooltip
_TOOLTIP_MIN_WIDTH = 280

class Comp7LightSelectorTooltip(SeasonalBattleSelectorTooltip):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_LIGHT_SELECTOR_INFO
    _TOOLTIP_WIDTH = _TOOLTIP_MIN_WIDTH
    @staticmethod
    def _getTitle():
        ...
    @staticmethod
    def _getDescription():
        ...
