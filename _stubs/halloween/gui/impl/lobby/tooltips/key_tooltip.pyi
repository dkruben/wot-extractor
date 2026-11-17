# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/key_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.key_tooltip_view_model import KeyTooltipViewModel as KeyTooltipViewModel
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from helpers import dependency as dependency

class KeyTooltipView(ViewImpl):
    __slots__: tuple
    _hwArtifactsCtrl: Any
    _hwController: Any
    __isPostBattle: Any
    __ctx: Any
    def __init__(self, isPostBattle, ctx=None, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
