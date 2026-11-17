# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSVehicleDissolveComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from vehicle_systems.tankStructure import VehiclePartsTuple as VehiclePartsTuple
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
_DISSOLVE_TIME_TICK = 0.05
_DISSOLVE_FACTOR_STEP = 0.015
_DISSOLVE_FULL_FACTOR = 1.0
_DISSOLVE_INSTANT_FACTOR = 0.95
_INSTANT_DISSOLVE_TIME_PASSED = 2.0

class LSVehicleDissolveComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    __callbackDelayer: Any
    __dissolveHandler: Any
    __dissolveFashions: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def __onAppearanceReady(self):
        ...
    def __onModelChanged(self):
        ...
    def __dissolve(self, factor):
        ...
    def __hideModel(self):
        ...
