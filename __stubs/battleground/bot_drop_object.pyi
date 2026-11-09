# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/bot_drop_object.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
import BattleReplay as BattleReplay
from constants import AirdropType as AirdropType
from helpers import dependency as dependency
from ReplayEvents import g_replayEvents as g_replayEvents
from battleground.components import SequenceComponent as SequenceComponent
from battleground.iself_assembler import ISelfAssembler as ISelfAssembler
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_logger: Any

class BotAirdrop(CallbackDelayer, ISelfAssembler):
    __dynamicObjectsCache: Any
    __sessionProvider: Any
    ALTITUDE_CORRECTING = 0.5
    END_ANIMATION_TIME_CORRECTING = 0.18
    __slots__: tuple
    TYPE_TO_EQUIPMENT: dict
    __spaceID: Any
    __deliveryTime: Any
    __deliveryPosition: Any
    __markerArea: Any
    __deliveryEffect: Any
    __teamID: Any
    __yawAxis: Any
    __plannedAnimDuration: Any
    __airdropType: Any
    def __init__(self, dropID, deliveryPosition, teamID, yawAxis, deliveryTime, airdropType):
        ...
    def start(self, *args, **kwargs):
        ...
    def destroy(self):
        ...
    def __onReplayTimeWarpStart(self):
        ...
    def __getEffect(self, effects):
        ...
    def __createMarkerArea(self, config, equipmentDescr):
        ...
    def __on3dEffectLoaded(self, equipmentDescr, effectP, position, resourceRefs):
        ...
    def __createDeliveryEffect(self, config):
        ...
    def __onDeliverEffectLoaded(self, effectP, position, resourceRefs):
        ...
    def __removeMarkerArea(self):
        ...
    def __removeDeliveryEffect(self):
        ...
    def __getEquipmentDescr(self):
        ...
