# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cfg_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel as PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_purchase_model import PostProgressionPurchaseModel as PostProgressionPurchaseModel

class PostProgressionCfgViewModel(PostProgressionBaseViewModel):
    __slots__: tuple
    onGoBackAction: Any
    onResearchAction: Any
    def __init__(self, properties=6, commands=3):
        ...
    @property
    def purchasePreview(self):
        ...
    @staticmethod
    def getPurchasePreviewType():
        ...
    def _initialize(self):
        ...
