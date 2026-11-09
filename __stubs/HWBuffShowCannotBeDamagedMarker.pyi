# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffShowCannotBeDamagedMarker.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _FET
from halloween_common.halloween_constants import BOSS_ROLE_TAG as BOSS_ROLE_TAG

class HWBuffShowCannotBeDamagedMarker(DynamicScriptComponent):
    _guiSessionProvider: Any
    _alreadyShown: Any
    def __init__(self, *args, **kwargs):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _setVehicleState(self):
        ...

def isInvulnerableBoss(vehicleID):
    ...
