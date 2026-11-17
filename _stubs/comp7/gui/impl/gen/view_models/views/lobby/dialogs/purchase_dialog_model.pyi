# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/dialogs/purchase_dialog_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel as BaseProductModel

class PageState(IntEnum):
    CONFIRMATION = 0
    FLYBY = 1
    CONGRATULATION = 2
    ERROR = 3

class PurchaseDialogModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onConfirm: Any
    onMouseOver3dScene: Any
    onMoveSpace: Any
    def __init__(self, properties=4, commands=4):
        ...
    def getPageState(self):
        ...
    def setPageState(self, value):
        ...
    def getProduct(self):
        ...
    def setProduct(self, value):
        ...
    @staticmethod
    def getProductType():
        ...
    def getHasSuitableVehicle(self):
        ...
    def setHasSuitableVehicle(self, value):
        ...
    def getIsPurchaseProcessing(self):
        ...
    def setIsPurchaseProcessing(self, value):
        ...
    def _initialize(self):
        ...
