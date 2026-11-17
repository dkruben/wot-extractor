# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_prime_time.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import time_utils as time_utils
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData, TOOLTIP_TYPE as TOOLTIP_TYPE
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedServerPrimeTime(ToolTipBaseData):
    __rankedController: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, peripheryID):
        ...
