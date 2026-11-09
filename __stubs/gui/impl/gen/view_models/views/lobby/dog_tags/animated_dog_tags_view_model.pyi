# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/animated_dog_tags_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tag_component import AnimatedDogTagComponent as AnimatedDogTagComponent

class AnimatedDogTagsViewModel(ViewModel):
    __slots__: tuple
    onEquip: Any
    onGoToAchievement: Any
    onInfoButtonClick: Any
    onPlayVideo: Any
    onOnboardingCloseClick: Any
    onHideNewBubble: Any
    onClose: Any
    def __init__(self, properties=3, commands=7):
        ...
    def getDogTags(self):
        ...
    def setDogTags(self, value):
        ...
    @staticmethod
    def getDogTagsType():
        ...
    def getOnboardingEnabled(self):
        ...
    def setOnboardingEnabled(self, value):
        ...
    def getInitialIndex(self):
        ...
    def setInitialIndex(self, value):
        ...
    def _initialize(self):
        ...
