# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_vehicle_appearance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import weakref as weakref
import math as math
from collections import namedtuple as namedtuple
from typing import TYPE_CHECKING as TYPE_CHECKING, List as List
from functools import partial as partial
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Event as Event
import Math as Math
import VehicleStickers as VehicleStickers
import Vehicular as Vehicular
import math_utils as math_utils
from cgf_client_common.prefab_loader import PrefabLoader as PrefabLoader
from dossiers2.ui.achievements import MARK_ON_GUN_RECORD as MARK_ON_GUN_RECORD
from items.components.c11n_constants import EASING_TRANSITION_DURATION as EASING_TRANSITION_DURATION
from gui import g_tankActiveCamouflage as g_tankActiveCamouflage
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.simple_turret_rotator import SimpleTurretRotator as SimpleTurretRotator
from shared_utils import nextTick as nextTick
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from vehicle_outfit.outfit import Area as Area, ANCHOR_TYPE_TO_SLOT_TYPE_MAP as ANCHOR_TYPE_TO_SLOT_TYPE_MAP, SLOT_TYPES as SLOT_TYPES, SLOT_TYPE_TO_ANCHOR_TYPE_MAP as SLOT_TYPE_TO_ANCHOR_TYPE_MAP
from gui.shared.gui_items.customization.slots import SLOT_ASPECT_RATIO as SLOT_ASPECT_RATIO, BaseCustomizationSlot as BaseCustomizationSlot, EmblemSlot as EmblemSlot, getProgectionDecalAspect as getProgectionDecalAspect
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from items.components.c11n_constants import ApplyArea as ApplyArea, AttachmentType as AttachmentType
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles as ITurretAndGunAngles
from objects_hierarchy import PrefabsMapItem as PrefabsMapItem
from vehicle_systems import camouflages as camouflages
from vehicle_systems.vehicle_composition import getExtraSlotMap as getExtraSlotMap, getObjectSlots as getObjectSlots, createVehicleComposition as createVehicleComposition, removeComposition as removeComposition, ATTACHMENT_TYPE_TO_SLOT as ATTACHMENT_TYPE_TO_SLOT
from vehicle_systems.components.vehicle_shadow_manager import VehicleShadowManager as VehicleShadowManager
from vehicle_systems.tankStructure import ModelsSetParams as ModelsSetParams, TankPartNames as TankPartNames, ColliderTypes as ColliderTypes, TankPartIndexes as TankPartIndexes
from vehicle_systems.tankStructure import VehiclePartsTuple as VehiclePartsTuple, TankNodeNames as TankNodeNames
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.ClientHangarSpace import hangarCFG as hangarCFG
from gui.battle_control.vehicle_getter import hasTurretRotator as hasTurretRotator
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
import GenericComponents as GenericComponents
import CGF as CGF
from vehicle_outfit.outfit import Outfit as TOutfit
from items.vehicles import VehicleDescrType as VehicleDescrType
_SHOULD_CHECK_DECAL_UNDER_GUN = True
_PROJECTION_DECAL_OVERLAPPING_FACTOR = 0.7
_HANGAR_TURRET_SHIFT: Any
_CAMERA_CAPSULE_GUN_SCALE: Any
_CAMERA_CAPSULE_SCALE: Any
_CAMERA_MIN_DIST_FACTOR = 0.8
AnchorLocation: Any
AnchorId: Any
AnchorHelper: Any
AnchorParams: Any
_logger: Any
ActivateContext: Any

class _LoadStateNotifier(object):
    __em: Any
    _onLoaded: Any
    _onUnloaded: Any
    __loaded: Any
    def __init__(self, loaded=False):
        ...
    def destroy(self):
        ...
    @property
    def isLoaded(self):
        ...
    def subscribe(self, onLoadCallback, onUnloadCallback):
        ...
    def unsubscribe(self, onLoadCallback, onUnloadCallback):
        ...
    def load(self):
        ...
    def unload(self):
        ...

class HangarVehicleAppearance(PrefabLoader):
    __ROOT_NODE_NAME = 'V'
    itemsCache: Any
    itemsFactory: Any
    settingsCore: Any
    turretAndGunAngles: Any
    customizationService: Any
    collisions: Any
    fashion: Any
    fashions: Any
    attachments: Any
    typeDescriptor: Any
    vehicleStickers: Any
    vehicleState: Any
    modelsSetParams: Any
    isDestroyed: Any
    isCompositionReady: Any
    __loadState: Any
    __curBuildInd: Any
    __vDesc: Any
    __vState: Any
    __resourceLoadID: Any
    __fashions: Any
    __repaintHandlers: Any
    __camoHandlers: Any
    __projectionDecalsHandlers: Any
    __projectionDecalsUpdater: Any
    __vEntity: Any
    __onLoadedCallback: Any
    __onLoadedAfterRefreshCallback: Any
    __vehicleStickers: Any
    __isVehicleDestroyed: Any
    __outfit: Any
    __staticTurretYaw: Any
    __staticGunPitch: Any
    __anchorsHelpers: Any
    __anchorsParams: Any
    __attachments: Any
    __modelAnimators: Any
    _modelCollisions: Any
    _crashedModelCollisions: Any
    turretRotator: Any
    __currentEmblemsAlpha: Any
    __showMarksOnGun: Any
    customizationGameObjects: Any
    onDecalsUpdated: Any
    onAttachmentsUpdated: Any
    __isCompositionReady: Any
    __collisions: Any
    __shadowManager: Any
    __c11nComponent: Any
    __tracks: Any
    __resources: Any
    @property
    def compoundModel(self):
        ...
    def isReady(self):
        ...
    @property
    def id(self):
        ...
    @property
    def filter(self):
        ...
    def __init__(self, spaceId, vEntity):
        ...
    def _recreateLinks(self):
        ...
    def onActivate(self, ctx):
        ...
    def recreate(self, vDesc, vState=None, callback=None, outfit=None):
        ...
    def remove(self):
        ...
    def refresh(self, outfit=None, callback=None):
        ...
    def destroy(self):
        ...
    def _reset(self, queue=None):
        ...
    @property
    def loadState(self):
        ...
    @property
    def fakeShadowDefinedInHullTexture(self):
        ...
    @property
    def slotPrefabs(self):
        ...
    def isLoaded(self):
        ...
    def recreateRequired(self, newOutfit):
        ...
    def computeVehicleHeight(self, collisions):
        ...
    def computeVehicleLength(self, collisions):
        ...
    def computeFullVehicleLength(self):
        ...
    def setCompositionReady(self, ready):
        ...
    def _initDirtComponent(self, dirtComponent, collisions):
        ...
    def _getTurretYaw(self):
        ...
    def _getGunPitch(self):
        ...
    def __reload(self, vDesc, vState, outfit):
        ...
    def __startBuild(self, vDesc, vState):
        ...
    def __onResourcesLoaded(self, buildInd, resourceRefs):
        ...
    def __fireResourcesLoadedEvent(self):
        ...
    def __onAnimatorsLoaded(self, buildInd, outfit, resourceRefs):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def _getActiveOutfit(self, vDesc):
        ...
    def __assembleModel(self, queue):
        ...
    def __onItemsCacheSyncCompleted(self, updateReason, _):
        ...
    def _getThisVehicleDossierInsigniaRank(self):
        ...
    def _requestClanDBIDForStickers(self, callback):
        ...
    def __onClanDBIDRetrieved(self, _, clanID):
        ...
    def __setupModel(self, buildIdx, queue):
        ...
    def _connectCollider(self, collisions):
        ...
    def _getColliderType(self):
        ...
    def __handleEntityUpdated(self, event):
        ...
    def _reloadColliderType(self, state, collisions):
        ...
    def __reloadShadowManagerTarget(self, state):
        ...
    def __doFinalSetup(self):
        ...
    def __applyAttachmentsVisibility(self):
        ...
    def __handleAttachmentsUpdated(self):
        ...
    def getAnchorParams(self, slotId, areaId, regionIdx):
        ...
    def updateAnchorsParams(self, tankPartsToUpdate=...):
        ...
    def getCentralPointForArea(self, areaIdx):
        ...
    def __applyCustomization(self, outfit, callback):
        ...
    def updateCustomization(self, outfit=None, callback=None):
        ...
    def rotateTurretForAnchor(self, anchorId, duration=...):
        ...
    def rotateGunToDefault(self):
        ...
    def rotateGunForAngle(self, gunPitchAngle):
        ...
    def getGunPitch(self):
        ...
    def getVehicleCentralPoint(self):
        ...
    def __getHullCentralPoint(self):
        ...
    def __getAnchorHelperById(self, anchorId):
        ...
    def __updateAnchorHelperWithId(self, anchorId, newAnchorHelper):
        ...
    def __getTurretYawForAnchor(self, anchorId, defaultYaw):
        ...
    def __updatePaint(self, outfit):
        ...
    def __updateCamouflage(self, outfit):
        ...
    def __updateDecals(self, outfit):
        ...
    def __updateProjectionDecals(self, outfit):
        ...
    def __updateCustomLogicComponents(self, outfit):
        ...
    def updateAttachments(self, prevAttachments):
        ...
    def __onAttachmentLoaded(self, attachment, objects, queue):
        ...
    def __updateStyleProgression(self, outfit):
        ...
    def __clearCustomLogicComponents(self, queue):
        ...
    def __onVehicleChanged(self):
        ...
    def __initAnchorsParams(self):
        ...
    def __updateAnchorsParams(self, tankPartsToUpdate):
        ...
    def __initAnchorsHelpers(self):
        ...
    def __getEmblemAnchorHelper(self, anchor):
        ...
    def __getAnchorHelper(self, anchor):
        ...
    def __getAttachedPartIdx(self, position, normal, tankPartIdx):
        ...
    def __correctTurretYaw(self, anchorHelper, defaultYaw):
        ...
    def __getDecalCorners(self, position, direction, up, slotDescriptor):
        ...
    def __applyToAnchorLocation(self, anchorLocation, transform):
        ...
    def __getGunNode(self):
        ...
    def __setGunMatrix(self, gunMatrix):
        ...
    @property
    def outfit(self):
        ...
    def __getStyleProgressionOutfitData(self, outfit):
        ...
    @property
    def _cameraPartsIdx(self):
        ...
