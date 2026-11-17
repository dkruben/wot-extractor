# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tank_setup/backports/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.lobby.tank_setup.backports.tooltips import ConsumableToolitpBuilder as ConsumableToolitpBuilder
from gui.impl.backport import createTooltipData as createTooltipData
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants as HWTankSetupConstants
HW_CONSUMABLE_EMPTY_TOOLTIP = '#halloween.tooltips.extend:hangar/ammo_panel/hw_equipment/empty'

class HWConsumableTooltipBuilder(ConsumableToolitpBuilder):
    @classmethod
    def getEmptyTooltip(cls, *args):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
