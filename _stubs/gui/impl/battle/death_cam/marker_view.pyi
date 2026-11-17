# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/death_cam/marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import GUI as GUI
import BigWorld as BigWorld
import typing as typing
from constants import IMPACT_TYPES as IMPACT_TYPES, BATTLE_LOG_MECHANIC_SHOT as BATTLE_LOG_MECHANIC_SHOT
import Math as Math
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType as KillCamInfoMarkerType, ImpactMarkerData as ImpactMarkerData, GunMarkerData as GunMarkerData, DistanceMarkerData as DistanceMarkerData
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsEnum as MechanicsEnum
from gui.impl.gen.view_models.views.battle.death_cam.death_cam_hud_view_model import DeathCamHudViewModel as DeathCamHudViewModel, ShellType as ShellType, Phase as Phase, DeathReason as DeathReason, ImpactMode as ImpactMode, CaliberRule as CaliberRule
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from math_common import round_py2_style as round_py2_style, round_py2_style_int as round_py2_style_int
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items import vehicles as vehicles
from typing import Optional as Optional, Dict as Dict
_logger: Any
_MODE_SHELL_ICON: dict

class DeathCamMarkerView(SubModelPresenter, IGlobalListener):
    __guiSessionProvider: Any
    _HIDE_MARKERS_DURING_PAUSE = False
    shellIconMap: dict
    __DEATH_REASONS: dict
    __IMPACT_MODES: dict
    __gunPosConfig: Any
    __markerMatrix: Any
    __callbackDelayer: Any
    __positionController: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    @staticmethod
    def __getMechanicShotModeIcon(attackerMechanicInfo):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onKillCamStateChanged(self, killCamState, _):
        ...
    def __onMarkerDisplayChanged(self, markerType, ctx):
        ...
    def __showDistanceMarker(self, distanceMarkerData):
        ...
    def __showImpactMarker(self, impactMarkerData):
        ...
    def __showGunMarker(self, gunMarkerData):
        ...
    def __updateGunMarkerModel(self, phaseDuration, projectileData, shellType, attackerMechanicInfo):
        ...
    def __updateImpactMarkerModel(self, phaseDuration, projectileData, relativeArmor, shellKind, causeOfDeath):
        ...
    def __updateDistanceMarkerModel(self, distanceMarkerData):
        ...
    def __updateGunMarkerParameters(self, projectileData, shellType, attackerMechanicInfo):
        ...
    def __updateDistanceMarkerParameters(self, projectileData, shellType, isAttackerSpotted, attackerMechanicInfo):
        ...
    def __updateImpactMarkerParameters(self, projectileData, relativeArmor, shellKind, causeOfDeath):
        ...
    def __updateViewModelSettings(self, phase, phaseTimePassed, phaseDuration, isVisible):
        ...
    def __initializeModel(self):
        ...
    def __updateMarkerPosition(self):
        ...
    def __getCaliberMarkerPositions(self, markerData):
        ...
    def __showMarker(self):
        ...
    def __hideMarker(self):
        ...
    def __isSimplifiedView(self):
        ...

def hasShellPenetrationDistanceLoss(shellType):
    ...
