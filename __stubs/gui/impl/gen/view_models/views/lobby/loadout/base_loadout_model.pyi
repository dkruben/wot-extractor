# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/base_loadout_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel

class BaseLoadoutModel(ViewModel):
    __slots__: tuple
    onSlotAction: Any
    def __init__(self, properties=1, commands=1):
        ...
    @property
    def dealPanel(self):
        ...
    @staticmethod
    def getDealPanelType():
        ...
    def _initialize(self):
        ...
