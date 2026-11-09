# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_upgrade_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import WWISE as WWISE
from ReservesEvents import randomReservesEvents as randomReservesEvents
from frontline.gui.Scaleform.daapi.view.meta.FrontlineBattleUpgradePanelMeta import FrontlineBattleUpgradePanelMeta as FrontlineBattleUpgradePanelMeta
from frontline.gui.frontline_helpers import getReserveIconPath as getReserveIconPath, getHotKeyInfoListByIndex as getHotKeyInfoListByIndex
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import UpgradeProhibitionReason as UpgradeProhibitionReason
from frontline.gui.sounds.sound_constants import FL_BATTLE_UPGRADE_PANEL_SOUND_EVENTS as FL_BATTLE_UPGRADE_PANEL_SOUND_EVENTS
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency, i18n as i18n, isPlayerAvatar as isPlayerAvatar
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
import BattleReplay as BattleReplay

class _AttentionEffectPlayer(object):
    __slots__: tuple
    __UPGRADE_ATTENTION_TIME = 10
    __viewRef: Any
    __callbackID: Any
    __delayTime: Any
    __isPlaying: Any
    def __init__(self, viewRef):
        ...
    def setVisible(self, visible):
        ...
    @staticmethod
    def playSound(eventName):
        ...
    def destroy(self):
        ...
    def __startTimer(self):
        ...
    def __disposeTimer(self):
        ...
    def __stopAnimation(self):
        ...
    def __stopEffect(self):
        ...
    def __onDelayFinished(self):
        ...

class FrontlineBattleUpgradePanel(FrontlineBattleUpgradePanelMeta, IArenaVehiclesController):
    __slots__: tuple
    __sessionProvider: Any
    __epicController: Any
    __FIRST_OFFER_INDEX = 0
    __SECOND_OFFER_INDEX = 1
    __TIME_WAITING_MESSAGE = 1
    __PROHIBITED_CAMERA_MODE: tuple
    __attentionEffect: Any
    __offer: Any
    __cooldownID: Any
    __showCooldownID: Any
    __canSelect: Any
    __canShowNextTime: Any
    __isInGameMessage: Any
    __lastStatus: Any
    __slotIdx: Any
    __prevCamera: Any
    def __init__(self):
        ...
    def onSelectItem(self, itemID):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onTimeWarpStart(self):
        ...
    def __stopPreviousShowTimer(self):
        ...
    def setVisible(self, status):
        ...
    def __onCameraChanged(self, cameraName, _=None):
        ...
    def __hidePanel(self, isInGameMessage=False):
        ...
    def __show(self):
        ...
    def __showPanel(self):
        ...
    def __disablePanel(self):
        ...
    def __enablePanel(self):
        ...
    def __stopPreviousTimer(self):
        ...
    def __isQueueEmpty(self):
        ...
    def __setCooldown(self, cooldownTime, reason):
        ...
    @staticmethod
    def __getR():
        ...
    @staticmethod
    def __getEquipmentByIntCD(intCD):
        ...
    def __getInstalledEquipments(self):
        ...
    def __getShortDescription(self, equipment):
        ...
    def __getReserveInfo(self, equipment, level, index):
        ...
    def __getDescription(self, firstEquipment, secondEquipment):
        ...
    def __getNumberName(self, number):
        ...
    def __hasOffer(self):
        ...
    def __selectedReserve(self, value, isIndex=True):
        ...
    def __onUpdateReservePanel(self, cooldownTime, reason):
        ...
    def __onShowReservePanel(self, offer, level, slotIdx):
        ...
    def __hasInstalledStackReserve(self):
        ...
    def __isReserveInstalled(self, equipment):
        ...
