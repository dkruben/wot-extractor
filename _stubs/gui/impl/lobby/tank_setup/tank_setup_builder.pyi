# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/tank_setup_builder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel as MainTankSetupModel
from gui.impl.lobby.tank_setup.interactors.consumable import ConsumableInteractor as ConsumableInteractor
from gui.impl.lobby.tank_setup.interactors.battle_booster import BattleBoosterInteractor as BattleBoosterInteractor
from gui.impl.lobby.tank_setup.interactors.opt_device import OptDeviceInteractor as OptDeviceInteractor
from gui.impl.lobby.tank_setup.interactors.shell import ShellInteractor as ShellInteractor
from gui.impl.lobby.tank_setup.sub_views.consumable_setup import ConsumableSetupSubView as ConsumableSetupSubView
from gui.impl.lobby.tank_setup.sub_views.battle_booster_setup import BattleBoosterSetupSubView as BattleBoosterSetupSubView
from gui.impl.lobby.tank_setup.sub_views.opt_device_setup import OptDeviceSetupSubView as OptDeviceSetupSubView
from gui.impl.lobby.tank_setup.sub_views.shell_setup import ShellSetupSubView as ShellSetupSubView
TankSetupComponent: Any

class TankSetupBuilder(object):
    __slots__: tuple
    __viewModelClazz: Any
    _vehItem: Any
    def __init__(self, viewModelClazz, vehItem):
        ...
    @staticmethod
    def build(components):
        ...
    def configureBuild(self, viewModel):
        ...
    def configureComponents(self, viewModel):
        ...
    def getViewModel(self):
        ...
    def clear(self):
        ...
    @staticmethod
    def addComponent(components, subModel, subView, interactor):
        ...

class HangarTankSetupBuilder(TankSetupBuilder):
    __slots__: tuple
    def __init__(self, vehItem):
        ...
    def configureComponents(self, viewModel):
        ...
