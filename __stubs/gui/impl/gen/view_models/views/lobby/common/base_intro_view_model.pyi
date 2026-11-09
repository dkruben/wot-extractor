# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/base_intro_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel as IntroSlideModel

class BaseIntroViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onVideo: Any
    onViewLoaded: Any
    def __init__(self, properties=4, commands=3):
        ...
    def getTitle(self):
        ...
    def setTitle(self, value):
        ...
    def getAbout(self):
        ...
    def setAbout(self, value):
        ...
    def getButtonLabel(self):
        ...
    def setButtonLabel(self, value):
        ...
    def getSlides(self):
        ...
    def setSlides(self, value):
        ...
    @staticmethod
    def getSlidesType():
        ...
    def _initialize(self):
        ...
