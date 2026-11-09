# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffInfinitePeriodicHealComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from dyn_components_groups import groupComponent as groupComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from xml_config_specs import StrParam as StrParam
from HWBuffSequencesComponent import HWBuffSequencesComponent as HWBuffSequencesComponent
from shared_utils import nextTick as nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak

# decorador original: @groupComponent(...)
class HWBuffInfinitePeriodicHealComponent(HWBuffSequencesComponent):
    guiSessionProvider: Any
    _buffKey: Any
    def __init__(self):
        ...
    def set_isActive(self, prev):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _activateEffects(self):
        ...
    def _onChangeBuffState(self):
        ...
    def _onVehicleHealthChanged(self, vehicleID, attackerID, damage):
        ...
    def _playEffect(self):
        ...
