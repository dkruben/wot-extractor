# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/FLStealthRadarComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from frontline import invalidateVehicleMarkerState as invalidateVehicleMarkerState, isAvatarReady as isAvatarReady
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak

class FLStealthRadarComponent(BigWorld.DynamicScriptComponent):
    _CALLBACK_DELAY = 0.5
    def __init__(self):
        ...
    def set_stealthRadar(self, _=None):
        ...
    def onLeaveWorld(self):
        ...
    def __onAvatarReady(self):
        ...
    def __invalidateStealthRadarState(self):
        ...
