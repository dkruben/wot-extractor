# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/modules_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_display_model import ResearchItemDisplayModel as ResearchItemDisplayModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_model import ResearchItemModel as ResearchItemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.field_modification_model import FieldModificationModel as FieldModificationModel

class ModulesModel(ViewModel):
    __slots__: tuple
    onVehicleChange: Any
    onInstallItem: Any
    onUnlockItem: Any
    onBuyAndInstallItem: Any
    onSellItem: Any
    def __init__(self, properties=4, commands=5):
        ...
    @property
    def fieldModificationModel(self):
        ...
    @staticmethod
    def getFieldModificationModelType():
        ...
    def getPrevResearchItems(self):
        ...
    def setPrevResearchItems(self, value):
        ...
    @staticmethod
    def getPrevResearchItemsType():
        ...
    def getCurrentResearchItems(self):
        ...
    def setCurrentResearchItems(self, value):
        ...
    @staticmethod
    def getCurrentResearchItemsType():
        ...
    def getResearchItems(self):
        ...
    def setResearchItems(self, value):
        ...
    @staticmethod
    def getResearchItemsType():
        ...
    def _initialize(self):
        ...
