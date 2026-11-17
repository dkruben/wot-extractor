# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/sub_views/battle_booster_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.configurations.battle_booster import BattleBoostersTabsController as BattleBoostersTabsController, BattleBoosterTabs as BattleBoosterTabs
from gui.impl.lobby.tank_setup.sub_views.base_equipment_setup import BaseEquipmentSetupSubView as BaseEquipmentSetupSubView

class BattleBoosterSetupSubView(BaseEquipmentSetupSubView):
    __slots__: tuple
    def updateSlots(self, slotID, fullUpdate=True, updateData=True):
        ...
    def revertItem(self, slotID):
        ...
    def _createTabsController(self):
        ...
    def _addListeners(self):
        ...
    def __onAdd(self, args):
        ...
