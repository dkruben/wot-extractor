# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/poi_notification_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from Event import EventsSubscriber as EventsSubscriber
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.constants import POI_TYPE_UI_MAPPING as POI_TYPE_UI_MAPPING, POI_STATUS_UI_MAPPING as POI_STATUS_UI_MAPPING
from gui.Scaleform.daapi.view.meta.PointsOfInterestNotificationPanelMeta import PointsOfInterestNotificationPanelMeta as PointsOfInterestNotificationPanelMeta
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from points_of_interest.components import PoiStateUpdateMask as PoiStateUpdateMask
from points_of_interest.mixins import PointsOfInterestListener as PointsOfInterestListener
from points_of_interest_shared import ENEMY_VEHICLE_ID as ENEMY_VEHICLE_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from points_of_interest.components import PoiStateComponent as PoiStateComponent
from points_of_interest_shared import PoiType as PoiType
_logger: Any
_R_NOTIFICATION_PANEL = R.strings.points_of_interest.notificationPanel

class PointsOfInterestPanel(PointsOfInterestNotificationPanelMeta, PointsOfInterestListener):
    __sessionProvider: Any
    __es: Any
    def __init__(self):
        ...
    @property
    def __isAvatarReady(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onPoiAdded(self, poiState):
        ...
    def onProcessPoi(self, poiState):
        ...
    def __updateStatus(self, poiState):
        ...
    def __updateProgress(self, poiState):
        ...
    def __onPoiCaptured(self, poiID, vehicleID):
        ...
    @classmethod
    def __getPoiCapturedMessage(cls, poiType, isAlly, vehicleID):
        ...
    @staticmethod
    def __isAlly(poiState):
        ...
    def __onBattleSessionStop(self):
        ...
