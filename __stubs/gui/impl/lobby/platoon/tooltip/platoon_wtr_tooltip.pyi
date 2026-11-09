# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/tooltip/platoon_wtr_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.platoon.common_player_data_model import CommonPlayerDataModel as CommonPlayerDataModel
from gui.impl.pub import ViewImpl as ViewImpl

class WTRTooltip(ViewImpl):
    __name: Any
    __clanTag: Any
    __badgeID: Any
    __rating: Any
    def __init__(self, name, clanTag, badgeID, rating):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
