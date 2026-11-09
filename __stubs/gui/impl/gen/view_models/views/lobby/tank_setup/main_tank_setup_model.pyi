# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/main_tank_setup_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_boosters_setup_model import BattleBoostersSetupModel as BattleBoostersSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.consumables_setup_model import ConsumablesSetupModel as ConsumablesSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_devices_setup_model import OptDevicesSetupModel as OptDevicesSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shells_setup_model import ShellsSetupModel as ShellsSetupModel

class MainTankSetupModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def consumablesSetup(self):
        ...
    @staticmethod
    def getConsumablesSetupType():
        ...
    @property
    def shellsSetup(self):
        ...
    @staticmethod
    def getShellsSetupType():
        ...
    @property
    def battleBoostersSetup(self):
        ...
    @staticmethod
    def getBattleBoostersSetupType():
        ...
    @property
    def optDevicesSetup(self):
        ...
    @staticmethod
    def getOptDevicesSetupType():
        ...
    def getSelectedSetup(self):
        ...
    def setSelectedSetup(self, value):
        ...
    def _initialize(self):
        ...
