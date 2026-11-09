# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/pre_battle_queue_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.app_loader import sf_lobby as sf_lobby
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.halloween_gui_constants import QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from halloween.gui.prb_control.entities.squad.entity import HalloweenSquadEntity as HalloweenSquadEntity
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import PRE_QUEUE_EXIT as PRE_QUEUE_EXIT, PRE_QUEUE_ENTER as PRE_QUEUE_ENTER
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween_common.halloween_constants import CURRENT_QUEUE_TYPE_KEY as CURRENT_QUEUE_TYPE_KEY
from helpers import dependency as dependency
from gui.impl.gen import R as R
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from halloween.gui.impl.gen.view_models.views.lobby.pre_battle_queue_view_model import PreBattleQueueViewModel as PreBattleQueueViewModel
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_BACKGROUND_ALPHA = 0.0

class PreBattleQueueView(BaseView):
    _difficultyLevelCtrl: Any
    _appLoader: Any
    _halloweenCtrl: Any
    __startTime: Any
    __callbackDelayer: Any
    def __init__(self, layoutID=..., startTime=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _loadModel(self):
        ...
    def _getEvents(self):
        ...
    def _initTipDelayer(self):
        ...
    def _getTipDelay(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalizeTipDelayer(self):
        ...
    def _finalize(self):
        ...
    def __updateTip(self):
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
    def __getSelectedDifficultyLevel(self):
        ...
