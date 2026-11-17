# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/veh_skill_tree/tooltips/base_perk_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.kpi_model import KpiModel as KpiModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import NodeModel as NodeModel

class BasePerkTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    @property
    def node(self):
        ...
    @staticmethod
    def getNodeType():
        ...
    def getKpis(self):
        ...
    def setKpis(self, value):
        ...
    @staticmethod
    def getKpisType():
        ...
    def _initialize(self):
        ...
