# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/status_notifications/sn_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications.sn_items import TimerSN as TimerSN, HalfOverturnedSN as HalfOverturnedSN, StaticDeathZoneSN as StaticDeathZoneSN, _DestroyTimerSN as _DestroyTimerSN
from last_stand.gui.battle_control.ls_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand.gui.scaleform.genConsts.LS_BATTLE_NOTIFICATIONS_TIMER_TYPES import LS_BATTLE_NOTIFICATIONS_TIMER_TYPES as _LSTYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
import typing as typing

class _LSLocalizationProvider(sn_items.LocalizationProvider):
    @property
    def _stringResource(self):
        ...

class LSHalfOverturnedSN(_LSLocalizationProvider, HalfOverturnedSN):
    def _getDescription(self, value=None):
        ...

class LSStaticDeathZoneSN(StaticDeathZoneSN):
    def getViewTypeID(self):
        ...

class LSPersonalDeathZoneSN(_LSLocalizationProvider, TimerSN):
    __callbackDelayer: Any
    _isVisible: Any
    def __init__(self, updateCallback):
        ...
    def destroy(self):
        ...
    def getItemID(self):
        ...
    def getViewTypeID(self):
        ...
    def _getDescription(self, value):
        ...
    def _update(self, value):
        ...
    def __hideTimer(self):
        ...

class _BaseBuffSN(_LSLocalizationProvider, _DestroyTimerSN):
    _BUFF_KEY = None
    __callbackDelayer: Any
    _isVisible: Any
    def __init__(self, updateCallback):
        ...
    def start(self):
        ...
    def destroy(self):
        ...
    def getItemID(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def _update(self, value):
        ...
    def _updateLogic(self, value):
        ...
    def _showWithTimer(self, duration, finishTime=0):
        ...
    def _hideTimer(self):
        ...
    def _canActivate(self, value):
        ...
    def _onBuffUpdate(self, isActvie, data):
        ...

class ShieldBuffSN(_BaseBuffSN):
    _BUFF_KEY = 'obeliskShield'
    def getViewTypeID(self):
        ...
    def _getTitle(self, value):
        ...
