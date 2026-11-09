# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tank_setup/ammunition_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.lobby.tank_setup.ammunition_panel.hangar_view import HangarAmmunitionPanelView as HangarAmmunitionPanelView
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7AmmunitionPanelView(HangarAmmunitionPanelView):
    __comp7Controller: Any
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateViewModel(self):
        ...
    def __updateRoleSkillSlot(self):
        ...
    def __getVehicle(self):
        ...
    def __getCurrentVehicleRoleSkill(self):
        ...
    def __getCurrentVehicleRoleEquipmentKey(self):
        ...
    def __getCurrentVehicleRoleSkillLevel(self):
        ...
