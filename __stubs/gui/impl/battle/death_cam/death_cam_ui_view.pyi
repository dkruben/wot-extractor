# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/death_cam/death_cam_ui_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from AvatarInputHandler.DynamicCameras.kill_cam_camera import CallbackPauseManager as CallbackPauseManager
from constants import IMPACT_TYPES as IMPACT_TYPES
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType as KillCamInfoMarkerType, ImpactMarkerData as ImpactMarkerData
from gui.impl.gen.view_models.views.battle.death_cam.death_cam_hud_view_model import DeathCamHudViewModel as DeathCamHudViewModel, ImpactMode as ImpactMode
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class DeathCamUIView(SubModelPresenter):
    __slots__: tuple
    __guiSessionProvider: Any
    _DISPLAY_DELAY = 0.75
    _UPDATE_TIMER_TICK = 0.1
    __isSceneRunning: Any
    __timerSeconds: Any
    __callbackDelayer: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def resetDisplay(self):
        ...
    def startDisplayTimer(self, seconds):
        ...
    def updateTimerCallback(self):
        ...
    def updatePauseText(self, seconds=None):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onKillCamStateChanged(self, killCamState, totalSceneDuration):
        ...
    def __onMarkerDisplayChanged(self, markerType, ctx):
        ...
    def __triggerFinalPhase(self):
        ...
    def __barsVisibility(self, show=True):
        ...
