# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/damage_info_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from future.utils import viewitems as viewitems
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.daapi.view.meta.DamageInfoPanelMeta import DamageInfoPanelMeta as DamageInfoPanelMeta
from gui.Scaleform.genConsts.DAMAGE_INFO_PANEL_CONSTS import DAMAGE_INFO_PANEL_CONSTS as DAMAGE_INFO_PANEL_CONSTS
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import avatar_getter as avatar_getter
from AvatarInputHandler import AvatarInputHandler as AvatarInputHandler
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
_DEVICE_NAME_TO_ID: dict
_DEVICE_HIDE_METHODS: dict
_DEVICE_UPDATE_METHODS: dict

class DamageInfoPanel(DamageInfoPanelMeta):
    sessionProvider: Any
    __isShown: Any
    __vehicleID: Any
    __devicesSnap: Any
    __isInFire: Any
    __isTrackWithinTrack: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __show(self, vehicleID, fetcher):
        ...
    def __hide(self):
        ...
    def __setDevicesStates(self, fetcher):
        ...
    def __updateDevicesStates(self, vehicleID, fetcher):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onCameraChanged(self, mode, vehicleID=0):
        ...

def _deviceDataConverter(deviceName, state):
    ...
def _defaultIterator(fetcher):
    ...
def _yohIterator(fetcher):
    ...
def _getDevicesIterator(fetcher, isYoh):
    ...
def _getDevicesSnapshot(fetcher, isYoh):
    ...
