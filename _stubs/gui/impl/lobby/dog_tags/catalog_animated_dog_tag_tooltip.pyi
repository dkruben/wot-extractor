# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/catalog_animated_dog_tag_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings
from advanced_achievements_client.items import SteppedAchievement as SteppedAchievement
from dog_tags_common.components_config import componentConfigAdapter as componentConfig
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.catalog_animated_dog_tag_tooltip_model import CatalogAnimatedDogTagTooltipModel as CatalogAnimatedDogTagTooltipModel
from gui.impl.lobby.dog_tags.dog_tag_composer import DogTagComposerLobby as DogTagComposerLobby
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from uilogging.dog_tags.logging_constants import DogTagKeys as DogTagKeys, DogTagsViewKeys as DogTagsViewKeys
from uilogging.dog_tags.logger import DogTagsTooltipLogger as DogTagsTooltipLogger
from account_helpers.dog_tags import DogTags as DogTagsAccountHelper
from advanced_achievements_client.items import _BaseGuiAchievement as _BaseGuiAchievement, _Progress as _Progress

class CatalogAnimatedDogTagTooltip(ViewImpl):
    __slots__: tuple
    __achievementsController: Any
    __dogTagsHelper: Any
    __composer: Any
    __uiLogger: Any
    __backgroundId: Any
    __engravingId: Any
    def __init__(self, params, layoutID=..., uiParent=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, backgroundId, engravingId):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def getLogInfo(self):
        ...
    def _finalize(self):
        ...
    def __getRequiredAchievement(self, backgroundId):
        ...
