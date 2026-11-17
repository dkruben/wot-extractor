# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VehicleStickers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import imghdr as imghdr
import logging as logging
import weakref as weakref
import typing as typing
import math as math
from collections import namedtuple as namedtuple
from itertools import chain as chain
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import cgf_network as cgf_network
import GpuDecals as GpuDecals
import math_utils as math_utils
import items as items
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from constants import IS_EDITOR as IS_EDITOR, VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT
from helpers import dependency as dependency
from helpers.prefab_effects import resolvePrefabStickerID as resolvePrefabStickerID, resolveDamageStickerPrefab as resolveDamageStickerPrefab
import Math as Math
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr
from items.components.c11n_constants import CustomizationType as CustomizationType, DecalType as DecalType, SLOT_DEFAULT_ALLOWED_MODEL as SLOT_DEFAULT_ALLOWED_MODEL
from items.components.component_constants import INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from vehicle_systems import stricted_loading as stricted_loading
from vehicle_systems import vehicle_composition as vehicle_composition
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes, TankPartNames as TankPartNames, TankNodeNames as TankNodeNames
from vehicle_systems.tankStructure import DetachedTurretPartIndexes as DetachedTurretPartIndexes, DetachedTurretPartNames as DetachedTurretPartNames
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from vehicle_outfit.outfit import Outfit as Outfit
import wrapped_options as wrapped_options
from emission_params import getEmissionParams as getEmissionParams
from GenericComponents import SlotMarkerComponent as SlotMarkerComponent
from cgf_modules import game_events as game_events
import BattleReplay as BattleReplay
_logger: Any
DEBUG_STICKER_TEXTURE = 'gui/maps/vehicles/decals/player_stickers/cool/sticker_15.dds'
_TextureParams: Any
_CounterParams: Any
_StickerSlotPair: Any
_PersonalNumberTexParams: Any
_INSIGNIA_LETTER = '*'
DamageStickerData: Any

class StickerAttributes(object):
    IS_INSCRIPTION = 1
    DOUBLESIDED = 2
    IS_MIRRORED = 4
    IS_UV_PROPORTIONAL = 8
    APPLY_TO_FABRIC = 16

class SlotTypes(object):
    CLAN = 'clan'
    PLAYER = 'player'
    INSCRIPTION = 'inscription'
    INSIGNIA_ON_GUN = 'insigniaOnGun'
    INSIGNIA = 'insignia'
    FIXED_EMBLEM = 'fixedEmblem'
    FIXED_INSCRIPTION = 'fixedInscription'
    ALL: tuple

class Insignia(object):
    class NodeNames(object):
        SINGLE = 'G'
        DUAL_LEFT = 'G_L'
        DUAL_RIGHT = 'G_R'
        ALL: tuple
    class Types(object):
        SINGLE = 'gunInsignia'
        DUAL_LEFT = 'gunInsigniaL'
        DUAL_RIGHT = 'gunInsigniaR'
        ALL: tuple
    class Indexes(object):
        SINGLE = -1
        DUAL_LEFT = -2
        DUAL_RIGHT = -3
        ALL: tuple

class ModelStickers(object):
    __componentIdx: Any
    __stickerPacks: Any
    __model: Any
    __partIdx: Any
    __toPartRootMatrix: Any
    __parentNode: Any
    __isDamaged: Any
    __modelComponentLink: Any
    __partIdxOverriden: Any
    __stickerModel: Any
    __isLoadingClanEmblems: Any
    def __init__(self, spaceID, componentIdx, stickerPacks, vDesc, emblemSlots):
        ...
    def __destroy__(self):
        ...
    @property
    def partIdx(self):
        ...
    @property
    def partIdxOverriden(self):
        ...
    def attachStickers(self, model, partIdx, parentNode, isDamaged, toPartRootMatrix=None):
        ...
    def attachInsigniaSticker(self, modelLink, partIdx, offsetToRootMatrix):
        ...
    def detachStickers(self):
        ...
    def bindReceiver(self, receiverId):
        ...
    def unbindReceiver(self):
        ...
    def addDamageSticker(self, stickerID, data):
        ...
    def delDamageSticker(self, handle):
        ...
    def updateClanSticker(self):
        ...
    def updateInsigniaSticker(self):
        ...
    def setAlpha(self, stickersAlpha):
        ...

class ComponentStickers(object):
    stickers: Any
    damageStickers: Any
    alpha: Any
    def __init__(self, stickers, damageStickers, alpha):
        ...

class DamageSticker(object):
    stickerID: Any
    handle: Any
    data: Any
    def __init__(self, stickerID, handle, data):
        ...

class StickerPack(object):
    _ALLOWED_PART_IDX: tuple
    _outfit: Any
    _data: Any
    _handles: Any
    def __init__(self, vDesc, outfit):
        ...
    def getData(self, componentIdx):
        ...
    def bind(self, componentIdx, componentSlot):
        ...
    def attach(self, componentIdx, stickerModel, isDamaged, offsetToRootMatrix=None):
        ...
    def detach(self, componentIdx, stickerModel):
        ...
    def _isValidComponentIdx(self, componentIdx):
        ...
    def _useTexture(self):
        ...
    def _getStickerSize(self, slot):
        ...
    def _getStickerAttributes(self, slot, sticker):
        ...

class FixedEmblemStickerPack(StickerPack):
    _ALLOWED_PART_IDX: tuple
    def bind(self, componentIdx, componentSlot):
        ...
    def _getDefaultParams(self, stickerID):
        ...

class EmblemStickerPack(StickerPack):
    _ALLOWED_PART_IDX: tuple
    def bind(self, componentIdx, componentSlot):
        ...
    def __convertToParams(self, item):
        ...

class FixedInscriptionStickerPack(FixedEmblemStickerPack):
    _ALLOWED_PART_IDX: tuple
    def _getStickerSize(self, slot):
        ...
    def _getStickerAttributes(self, slot, sticker):
        ...

class InscriptionStickerPack(StickerPack):
    _ALLOWED_PART_IDX: tuple
    def bind(self, componentIdx, componentSlot):
        ...
    def _convertToParams(self, item):
        ...
    def _getStickerSize(self, slot):
        ...
    def _getStickerAttributes(self, slot, sticker):
        ...

class PersonalNumStickerPack(StickerPack):
    _ALLOWED_PART_IDX: tuple
    def bind(self, componentIdx, componentSlot):
        ...
    def _convertToParams(self, item, component):
        ...
    def _getStickerSize(self, slot):
        ...
    def attach(self, componentIdx, stickerModel, isDamaged, offsetToRootMatrix=None):
        ...

class ClanStickerPack(StickerPack):
    _ALLOWED_PART_IDX: tuple
    _NO_CLAN_ID = 0
    lobbyContext: Any
    _clanId: Any
    def __init__(self, vDesc, clanId=...):
        ...
    def setClanId(self, clanId):
        ...
    def bind(self, componentIdx, componentSlot):
        ...
    def attach(self, componentIdx, stickerModel, isDamaged, offsetToRootMatrix=None):
        ...
    def _isValidComponentIdx(self, componentIdx):
        ...
    def _useTexture(self):
        ...
    def __onClanEmblemLoaded(self, _, data, componentIdx, stickerModel, isDamaged):
        ...

class InsigniaStickerPack(StickerPack):
    _ALLOWED_PART_IDX: Any
    _NO_INSIGNIA_RANK = 0
    _insigniaRank: Any
    _customizationNationID: Any
    _useCustomInsignia: Any
    _useOldInsignia: Any
    def __init__(self, vDesc, outfit, insigniaRank):
        ...
    def setInsigniaRank(self, insigniaRank):
        ...
    def bind(self, componentIdx, componentSlot):
        ...
    def attach(self, componentIdx, stickerModel, isDamaged, offsetToRootMatrix=None):
        ...
    def update(self, componentIdx):
        ...
    def _isValidComponentIdx(self, componentIdx):
        ...
    def _getDefaultParams(self):
        ...
    def _getStickerAttributes(self, slot, sticker):
        ...
    def _convertToInsignia(self, item):
        ...
    def _convertToCounter(self, item):
        ...

class DebugStickerPack(StickerPack):
    _ALLOWED_PART_IDX: Any
    def bind(self, componentIdx, componentSlot):
        ...
    def setClanId(self, clanId):
        ...
    def setInsigniaRank(self, insigniaRank):
        ...
    def _getStickerSize(self, slot):
        ...
    def _getStickerAttributes(self, slot, sticker):
        ...

class VehicleStickers(object):
    alpha: Any
    show: Any
    __currentInsigniaRank: Any
    __show: Any
    __defaultAlpha: Any
    __animateGunInsignia: Any
    __go: Any
    __vDesc: Any
    __componentNames: Any
    __childPartDamageStickers: Any
    __parametrizedDamageStickers: Any
    __pendingParametrizedDamageStickers: Any
    __stickers: Any
    __stickerPacks: Any
    def setClanID(self, clanID):
        ...
    def setInsigniaRank(self, insigniaRank):
        ...
    def __setAlpha(self, alpha):
        ...
    def __setShow(self, show):
        ...
    def __init__(self, spaceID, go, vehicleDesc, insigniaRank=0, outfit=None, currentModelsSet=None):
        ...
    def getCurrentInsigniaRank(self):
        ...
    def getStickerPack(self, packType):
        ...
    def attach(self, compoundModel, isDamaged, showDamageStickers, isDetachedTurret=False, attachChildPart=False, collisionComponent=None):
        ...
    def detach(self):
        ...
    def attachInsigniaReceiverStickers(self, vehiclePart, modelLink, offsetToRootMatrix, componentID):
        ...
    def bindReceiver(self, partIdx, receiverId):
        ...
    def unbindReceiver(self, partIdx):
        ...
    def addDamageSticker(self, code, stickerID, prefabEffIndex, data, collisionComponent, isCompositionReady, isActive):
        ...
    def delDamageSticker(self, code):
        ...
    @classmethod
    def _createComponentSlots(cls, vehicleDesc, showEmblemsOnGun, modelsSet):
        ...
    @classmethod
    def _hasModelsSetClanSlots(cls, vehicleDesc, modelsSet):
        ...
    @classmethod
    def _filterClanEmblems(cls, emblemSlots, modelsSet, skipDefault=False):
        ...
    @classmethod
    def _createGunSlots(cls, vehicleDesc, modelsSet):
        ...
    def _createStickerPacks(self, vehicleDesc, outfit, insigniaRank):
        ...
    def _createDebugStickerPacks(self, vehicleDesc, outfit, insigniaRank):
        ...
    def __getInsigniaAttachNode(self, insigniaType, isDamaged, compoundModel):
        ...
    def __addChildPartDamageSticker(self, code, stickerID, data, spaceID):
        ...
    @staticmethod
    def __addDamageStickerGO(code, stickerID, data, spaceID):
        ...
    @staticmethod
    def __getDamageStickerGoByNetworkId(code, spaceID):
        ...
    def __getSlotGoByComponentIdx(self, componentIdx):
        ...
    def __addParametrizedDamageSticker(self, code, prefabEffIndex, hitType, data, collisionComponent, isCompositionReady, isActive=False):
        ...
    def __delParametrizedDamageSticker(self, uid):
        ...
    def processPendingDamageStickers(self, collisionComponent, isCompositionReady):
        ...

class VehicleStickersSystem(CGF.System):
    StickerActivated: Any
    StickerDeactivated: Any
    ReceiverAccess: Any
    Reactions: Any
    def update(self):
        ...
    def getReceiverId(self, gameObject, partIdx):
        ...

def _getAccountRepository():
    ...
def isUseDebugStickers():
    ...
def resizeSegment(segStart, segEnd, segLength):
    ...
