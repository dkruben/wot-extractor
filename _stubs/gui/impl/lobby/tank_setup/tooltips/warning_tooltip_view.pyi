# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/tooltips/warning_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningTooltipViewModel as WarningTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningDescription as WarningDescription

class WarningTooltipView(ViewImpl):
    def __init__(self, reason, isCritical):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, reason, isCritical, *args, **kwargs):
        ...
