# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSWaveProgressComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class LSWaveProgressComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    @property
    def lsBattleGuiCtrl(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_enemiesInfo(self, prev):
        ...
    def set_healthBreakpoints(self, prev):
        ...
    def set_enemiesStatus(self, prev):
        ...
    def set_convoyStatus(self, prev):
        ...
    def set_convoyDistanceIndicator(self, prev):
        ...
    def set_convoyHealth(self, prev):
        ...
