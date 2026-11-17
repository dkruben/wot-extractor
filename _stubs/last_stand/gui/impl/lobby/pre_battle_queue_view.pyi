# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/pre_battle_queue_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prestige.prestige_helpers import hasVehiclePrestige as hasVehiclePrestige, fillPrestigeEmblemModel as fillPrestigeEmblemModel, getVehiclePrestige as getVehiclePrestige
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.app_loader import sf_lobby as sf_lobby
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView
from last_stand.gui.impl.lobby.tooltips.difficulty_tooltip import DifficultyTooltipView as DifficultyTooltipView
from last_stand.gui.game_control.ls_difficulty_missions_controller import getFormattedMissionsList as getFormattedMissionsList
from last_stand.gui.ls_gui_constants import QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from last_stand.gui.prb_control.entities.squad.entity import LastStandSquadEntity as LastStandSquadEntity
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import PRE_QUEUE_EXIT as PRE_QUEUE_EXIT, PRE_QUEUE_ENTER as PRE_QUEUE_ENTER
from last_stand_common.last_stand_constants import CURRENT_QUEUE_TYPE_KEY as CURRENT_QUEUE_TYPE_KEY, DEFAULT_DIFFICULTY_MODIFIER as DEFAULT_DIFFICULTY_MODIFIER
from helpers import dependency as dependency
from helpers.time_utils import MS_IN_SECOND as MS_IN_SECOND
from gui.impl.gen import R as R
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from last_stand.gui.impl.gen.view_models.views.lobby.pre_battle_queue_view_model import PreBattleQueueViewModel as PreBattleQueueViewModel, VehicleInfoBlockModel as VehicleInfoBlockModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel as DifficultyItemModel, StateEnum as StateEnum
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items import Vehicle as Vehicle
_BACKGROUND_ALPHA = 0.0

class PreBattleQueueView(BaseView):
    _difficultyLevelCtrl: Any
    _appLoader: Any
    _lsMissionsCtrl: Any
    _itemsCache: Any
    __startTime: Any
    def __init__(self, layoutID=..., startTime=None):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _loadModel(self):
        ...
    def __fillCommonInfo(self, model):
        ...
    def __fillSelectedVehicle(self, model):
        ...
    def __fillSelectedDifficulty(self, model):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onExitBattleButtonClick(self):
        ...
    # decorador original: @sf_lobby
    def __app(self):
        ...
    def __onEscape(self):
        ...
    @staticmethod
    def __onMoveSpace(moveTypeArgs=None):
        ...
    def __onDifficultyLevelChanged(self, *args, **kwargs):
        ...
    def __getSelectedDifficultyLevel(self):
        ...
