# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/multiple_icons_set_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel as IconViewModel

class IconPositionLogicEnum(Enum):
    BOTTOMALIGNMENT = 'bottomAlignment'
    CENTREDANDTHROUGHCONTENT = 'centredAndThroughContent'
    MOVECONTENTBELOW = 'moveContentBelow'

class MultipleIconsSetViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getBackgrounds(self):
        ...
    def setBackgrounds(self, value):
        ...
    @staticmethod
    def getBackgroundsType():
        ...
    def getOverlays(self):
        ...
    def setOverlays(self, value):
        ...
    @staticmethod
    def getOverlaysType():
        ...
    def getIcons(self):
        ...
    def setIcons(self, value):
        ...
    @staticmethod
    def getIconsType():
        ...
    def getIconPositionLogic(self):
        ...
    def setIconPositionLogic(self, value):
        ...
    def _initialize(self):
        ...
