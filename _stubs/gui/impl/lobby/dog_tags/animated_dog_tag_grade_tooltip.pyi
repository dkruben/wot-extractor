# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/animated_dog_tag_grade_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from advanced_achievements_client.items import SteppedAchievement as SteppedAchievement
from dog_tags_common.components_config import componentConfigAdapter as componentConfig
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tag_grade_tooltip_model import AnimatedDogTagGradeTooltipModel as AnimatedDogTagGradeTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IAchievementsController as IAchievementsController

class AnimatedDogTagGradeTooltip(ViewImpl):
    __slots__: tuple
    __achievementsController: Any
    def __init__(self, params, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, backgroundId, engravingId):
        ...
    def __getRequiredAchievement(self, backgroundId):
        ...
