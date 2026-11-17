# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/bonus_list_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.auxiliary.rewards_helper import getRewardRendererModelPresenter as getRewardRendererModelPresenter
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS

class BonusListManager(object):
    __slots__: tuple
    __tooltipsData: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def setBonuses(self, bonuses, model, lastCongratsIndex=-1):
        ...
    def createToolTip(self, event, parentWindow):
        ...
    def __getBackportTooltipData(self, event):
        ...
