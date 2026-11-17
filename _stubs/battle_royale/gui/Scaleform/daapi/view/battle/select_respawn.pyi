# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/select_respawn.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import weakref as weakref
from battle_royale.gui.battle_control.controllers.spawn_ctrl import ISpawnListener as ISpawnListener
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.doc_loaders.battle_royale_settings_loader import getBattleRoyaleSettings as getBattleRoyaleSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle_royale.respawn_point_view_model import RespawnPointViewModel as RespawnPointViewModel
from gui.impl.gen.view_models.views.battle_royale.select_respawn_view_model import SelectRespawnViewModel as SelectRespawnViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from math_common import round_py2_style as round_py2_style
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class SelectRespawnComponent(InjectComponentAdaptor, ISpawnListener):
    __view: Any
    def __init__(self):
        ...
    def _makeInjectView(self):
        ...
    def _dispose(self):
        ...
    def setSpawnPoints(self, points):
        ...
    def updateCloseTime(self, timeLeft, state):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def onSelectPoint(self, pointId):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...

class BRPrebattleTimer(IAbstractPeriodView):
    __timeLeft: Any
    _parentView: Any
    __endingTime: Any
    def __init__(self, parentView):
        ...
    def updateCloseTime(self, timeLeft, state):
        ...
    def __updateTimer(self):
        ...
    @staticmethod
    def __getWaitMessage():
        ...

class SelectRespawnView(ViewImpl):
    __sessionProvider: Any
    __mapTexture: Any
    __background: Any
    __mapSize: Any
    __offset: Any
    __closeTime: Any
    __points: Any
    __pointsById: Any
    __isActive: Any
    __timer: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def updateCloseTime(self, timeLeft, state):
        ...
    def dispose(self):
        ...
    def setPoints(self, points):
        ...
    def updateSelectedPoint(self, pointId):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def setKeyHandlerState(self, isActive=True):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __getBgByGeometryName(self, geometry):
        ...
    def __onSelectPoint(self):
        ...
    def __onCompleteBtnClick(self):
        ...
