# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tank_setup/interactor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.lobby.tank_setup.interactors.consumable import ConsumableInteractor as ConsumableInteractor
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from adisp import adisp_process as adisp_process
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants as HWTankSetupConstants
BUY_AND_INSTALL_HW_CONSUMABLES_ACTION = 'buyAndInstallHWConsumables'

class HalloweenInteractor(ConsumableInteractor):
    def getName(self):
        ...
    # decorador original: @adisp_process
    def confirm(self, callback, skipDialog=False):
        ...
