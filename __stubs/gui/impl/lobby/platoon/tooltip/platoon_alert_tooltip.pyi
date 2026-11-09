# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/tooltip/platoon_alert_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl import backport as backport
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.platoon.alert_tooltip_model import AlertTooltipModel as AlertTooltipModel

class AlertTooltip(ViewImpl):
    __header: Any
    __body: Any
    def __init__(self, header, body):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
