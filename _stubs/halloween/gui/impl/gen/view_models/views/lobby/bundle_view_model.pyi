# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/bundle_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.bundle_model import BundleModel as BundleModel

class WindowType(Enum):
    KEYWIDGET = 'keyWidget'
    DECRYPT = 'decrypt'
    SKIP = 'skip'

class TitleStates(Enum):
    DEFAULT = 'default'
    ONLYSHOPBUNDLE = 'onlyShopBundle'
    ONLYKEYSBUNDLE = 'onlyKeysBundle'

class BundleViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onPurchase: Any
    def __init__(self, properties=6, commands=2):
        ...
    def getLackOfKeys(self):
        ...
    def setLackOfKeys(self, value):
        ...
    def getSlide(self):
        ...
    def setSlide(self, value):
        ...
    def getWindowType(self):
        ...
    def setWindowType(self, value):
        ...
    def getTitleState(self):
        ...
    def setTitleState(self, value):
        ...
    def getBundles(self):
        ...
    def setBundles(self, value):
        ...
    @staticmethod
    def getBundlesType():
        ...
    def getGoldCount(self):
        ...
    def setGoldCount(self, value):
        ...
    def _initialize(self):
        ...
