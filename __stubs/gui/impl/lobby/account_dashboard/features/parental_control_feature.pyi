# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/parental_control_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.premacc.dashboard.parent_control_info_popover import ParentControlInfoPopoverContent as ParentControlInfoPopoverContent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.shared import IItemsCache as IItemsCache

class ParentalControlFeature(FeatureItem):
    __gameSession: Any
    __itemsCache: Any
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def createPopOverContent(self, event):
        ...
    def _fillModel(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __update(self, model=None):
        ...
    def __onParentControlNotify(self):
        ...
