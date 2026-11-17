# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.box_compensation_tooltip_model import BoxCompensationTooltipModel as BoxCompensationTooltipModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.box_tooltip_model import BoxTooltipModel as BoxTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController

class BoxTooltipBase(ViewImpl):
    __slots__: tuple
    __lootBoxes: Any
    __boxCategory: Any
    __eventName: Any
    def __init__(self, boxCategory, eventName, layoutID, model):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...

class BoxTooltip(BoxTooltipBase):
    def __init__(self, boxCategory, eventName):
        ...

class BoxCompensationTooltip(BoxTooltipBase):
    def __init__(self, boxCategory, eventName):
        ...
