# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWVehicleOptionsRequesterComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from typing import Optional as Optional

class HWVehicleOptionsRequesterComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def set_upgradeOptions(self, _):
        ...
    def selectUpgrade(self, anomalyIDx):
        ...
    def _notifyUpgradeOptionChanged(self, options):
        ...
