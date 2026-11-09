# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/tooltips/collection_item_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.collection.collections_helpers import getItemResKey as getItemResKey, getCollectionRes as getCollectionRes, getItemName as getItemName, getImagePath as getImagePath
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.tooltips.collection_item_tooltip_view_model import CollectionItemTooltipViewModel as CollectionItemTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController

class CollectionItemTooltipView(ViewImpl):
    __slots__: tuple
    __collectionsSystem: Any
    __collectionId: Any
    __item: Any
    __isDetailed: Any
    def __init__(self, itemId, collectionId, isDetailed, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __getDescription(self):
        ...
    def __getImage(self):
        ...
