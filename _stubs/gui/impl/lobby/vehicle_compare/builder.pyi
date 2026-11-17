# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/builder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel as MainTankSetupModel
from gui.impl.lobby.vehicle_compare.battle_booster import CompareBattleBoosterSetupSubView as CompareBattleBoosterSetupSubView
from gui.impl.lobby.vehicle_compare.consumable import CompareConsumableSetupSubView as CompareConsumableSetupSubView
from gui.impl.lobby.vehicle_compare.interactors import CompareConsumableInteractor as CompareConsumableInteractor, CompareOptDeviceInteractor as CompareOptDeviceInteractor, CompareBattleBoosterInteractor as CompareBattleBoosterInteractor
from gui.impl.lobby.vehicle_compare.opt_device import CompareOptDeviceSetupSubView as CompareOptDeviceSetupSubView
from gui.impl.lobby.tank_setup.tank_setup_builder import TankSetupBuilder as TankSetupBuilder

class CompareTankSetupBuilder(TankSetupBuilder):
    __slots__: tuple
    def __init__(self, vehItem):
        ...
    def configureComponents(self, viewModel):
        ...
