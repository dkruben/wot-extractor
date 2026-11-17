# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/groups_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.lobby.tank_setup.ammunition_panel.blocks_controller import HangarAmmunitionBlocksController as HangarAmmunitionBlocksController
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController, RANDOM_GROUPS as RANDOM_GROUPS

class HangarAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__: tuple
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def _getGroups(self):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...
