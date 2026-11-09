# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ArenaType as ArenaType
import BigWorld as BigWorld
import Math as Math
from AvatarInputHandler.cameras import getViewProjectionMatrix as getViewProjectionMatrix
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from Event import Event as Event
from frameworks_common.state_machine import StateIdsObserver as StateIdsObserver
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_group_model import MapsTrainingGroupModel as MapsTrainingGroupModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_map_model import MapsTrainingMapModel as MapsTrainingMapModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_scenario_model import MapsTrainingScenarioModel as MapsTrainingScenarioModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_view_model import MapsTrainingViewModel as MapsTrainingViewModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_minimap_point import MapsTrainingMinimapPoint as MapsTrainingMinimapPoint
from gui.impl.lobby.maps_training.maps_training_tactical_maps_config import TacticalMapsConfigReader as TacticalMapsConfigReader, Scenario as Scenario, Team as Team, Point as Point
from gui.impl.lobby.maps_training.scenario_tooltip import ScenarioTooltip as ScenarioTooltip
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.impl.lobby.hangar.presenters.utils import fillMenuSharedItems as fillMenuSharedItems, navigateTo as navigateTo
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from maps_training_common.maps_training_constants import VEHICLE_TYPE as VEHICLE_TYPE, VEHICLE_CLASSES_ORDER as VEHICLE_CLASSES_ORDER, SCENARIO_INDEXES as SCENARIO_INDEXES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.impl.lobby.maps_training.maps_training_base_view import MapsTrainingBaseView as MapsTrainingBaseView
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames
from gui.impl.lobby.maps_training.sound_constants import MAPS_TRAINING_SOUND_SPACE as MAPS_TRAINING_SOUND_SPACE

class _MapsTrainingStatesObserver(StateIdsObserver):
    __mapsTrainingCtrl: Any
    onNavigationChanged: Any
    def __init__(self):
        ...
    def onEnterState(self, state, event):
        ...

class MapsTrainingView(MapsTrainingBaseView, IGlobalListener):
    __slots__: tuple
    _TACTICAL_MAPS_CONFIG_PATH = 'scripts/maps_training_tactical_maps.xml'
    _SCENARIO_COUNT: Any
    _UPDATE_TICK_RATE = 0.1
    _MEDIUM_TANK_OFFSET = 1.26959
    _MAX_MAP_DIFFICULTY = 3
    _DEFAULT_MAP_DIFFICULTY = 3
    _DISABLED_MAP_GROUP_ID = 2
    _COMMON_SOUND_SPACE = MAPS_TRAINING_SOUND_SPACE
    lobbyContext: Any
    itemsCache: Any
    mapsTrainingController: Any
    hangarSpace: Any
    __selectedMap: Any
    __selectedScenario: Any
    __ctxVehicleType: Any
    __ctxSide: Any
    __ctxShowAnimation: Any
    __tooltipData: Any
    __account: Any
    __mapsConfig: Any
    __isDataLoaded: Any
    __blur: Any
    __blurRectId: Any
    __packer: Any
    __tickCallback: Any
    __preferences: Any
    __markerPosOffset: Any
    __finalizationInProgress: Any
    __lsmObserver: Any
    def __init__(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __initFromCtx(self, ctx):
        ...
    def _removeListeners(self):
        ...
    def __onNavigationChanged(self, selectedMap):
        ...
    def __onClose(self):
        ...
    def __onBack(self):
        ...
    def __onSelect(self, args):
        ...
    def __onScenarioSelect(self, args):
        ...
    def __updateSelectedMap(self, model):
        ...
    def __getRewards(self, geometryID, stage):
        ...
    def __fillBonusArray(self, bonusArray, bonusesData):
        ...
    def __updateSelectedScenario(self, model):
        ...
    @staticmethod
    def __createPointModel(pointId, textKeys, isLeft, tooltipImage, position, pointType):
        ...
    def __getVehicleForScenario(self, scenario):
        ...
    def __getTargets(self, scenario):
        ...
    def __getScenarioConfig(self, vehType, team):
        ...
    def __filterChangeHandler(self, kwargs):
        ...
    def __clickInfoHandler(self):
        ...
    def __fillData(self):
        ...
    def __updateAllSelections(self, model):
        ...
    def __selectScenario(self):
        ...
    def __onBlurRectUpdated(self, args):
        ...
    def __onPreviewVehicleChangeStarted(self):
        ...
    def __onPreviewVehicleChanged(self):
        ...
    def __updateMarkerPosition(self):
        ...
    def worldToScreenPos(self, worldPos):
        ...
    def __tick(self):
        ...
    def __checkCamera(self):
        ...
    def __switchCamera(self):
        ...
    def __updateMenuItems(self):
        ...
