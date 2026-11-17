# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/rank_rewards_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_rewards_item_model import RankRewardsItemModel as RankRewardsItemModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.progression_base_model import ProgressionBaseModel as ProgressionBaseModel
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel as QualificationModel

class RankRewardsModel(ProgressionBaseModel):
    __slots__: tuple
    DEFAULT_ITEM_INDEX = -1
    onPreviewOpen: Any
    def __init__(self, properties=5, commands=1):
        ...
    @property
    def qualificationModel(self):
        ...
    @staticmethod
    def getQualificationModelType():
        ...
    def getItems(self):
        ...
    def setItems(self, value):
        ...
    @staticmethod
    def getItemsType():
        ...
    def getInitialItemIndex(self):
        ...
    def setInitialItemIndex(self, value):
        ...
    def _initialize(self):
        ...
