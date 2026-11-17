# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/battle_consumable.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.items_parameters import params_helper as params_helper, formatters as params_formatters
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from helpers import int2roman as int2roman
from helpers.i18n import makeString as _ms

class BattleConsumableTooltipData(BlocksTooltipData):
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class BattleConsumableTooltipBlockConstructor(object):
    item: Any
    configuration: Any
    leftPadding: Any
    rightPadding: Any
    def __init__(self, item, configuration, leftPadding=20, rightPadding=20):
        ...
    def construct(self):
        ...

class HeaderBlockConstructor(BattleConsumableTooltipBlockConstructor):
    def construct(self):
        ...

class CommonStatsBlockConstructor(BattleConsumableTooltipBlockConstructor):
    _valueWidth: Any
    def __init__(self, item, configuration, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...
    def __packParameterBloc(self, name, value, measureUnits):
        ...
