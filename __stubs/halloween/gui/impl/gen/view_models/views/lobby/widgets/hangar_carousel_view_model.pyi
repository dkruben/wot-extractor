# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/hangar_carousel_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import HangarCarouselVehicleViewModel as HangarCarouselVehicleViewModel

class HangarCarouselViewModel(ViewModel):
    __slots__: tuple
    onChangeVehicle: Any
    onVehiclePreview: Any
    onChangeSize: Any
    def __init__(self, properties=2, commands=3):
        ...
    def getSelectedVehicle(self):
        ...
    def setSelectedVehicle(self, value):
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def _initialize(self):
        ...
