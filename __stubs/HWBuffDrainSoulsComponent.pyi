# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffDrainSoulsComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import GenericComponents as GenericComponents
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from HWBuffSequencesComponent import HWBuffSequencesComponent as HWBuffSequencesComponent
from dyn_components_groups import groupComponent as groupComponent
from xml_config_specs import StrParam as StrParam
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_ANIMATOR_STATUS_START = 1.0
_ANIMATOR_STATUS_END = 0.0
_START_ANIMATION_DELAY = 0.1

# decorador original: @groupComponent(...)
class HWBuffDrainSoulsComponent(HWBuffSequencesComponent):
    _guiSessionProvider: Any
    __callbackDelayer: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_isActive(self, prev):
        ...
    def set_isShownStatusIcon(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def _activateEffects(self):
        ...
    def _onAvatarVehicleChanged(self):
        ...
    def __updateVisualStatus(self, canStopAura):
        ...
    def __stopAura(self):
        ...
    def __startAura(self):
        ...
    def __startAuraDelayed(self):
        ...
    def __setAnimatorStatus(self, value):
        ...
    def __setSoulsIndication(self, value):
        ...
    def __isPlayerVehicle(self, vehicleID):
        ...
