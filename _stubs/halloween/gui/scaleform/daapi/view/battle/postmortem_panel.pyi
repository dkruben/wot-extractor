# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.battle_control import avatar_getter as avatar_getter
from halloween.gui.scaleform.daapi.view.meta.PostmortemPanelMeta import PostmortemPanelMeta as PostmortemPanelMeta
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.hw_vehicle_role_helper import getVehicleRole as getVehicleRole
_ATTACK_REASON_MSG_TO_EVENT: dict

class HWPostmortemPanel(PostmortemPanelMeta):
    PHASE_DEATH_REASON = 'DEATH_FROM_PHASE_TIMER_SELF_SUICIDE'
    PHASE_DEATH_REASON_LATE = 'DEATH_FROM_PHASE_TIMER_SELF_SUICIDE_LATE'
    PHASE_DEATH_REASON_FINAL = 'DEATH_FROM_PHASE_TIMER_SELF_SUICIDE_FINAL'
    TICK_RATE = 1
    __slots__: tuple
    __collectorIsFull: Any
    _callbacks: Any
    def __init__(self):
        ...
    @property
    def _isRespawnEnabledOnServer(self):
        ...
    @property
    def _isLastPhase(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _showOwnDeathInfo(self):
        ...
    def _showPlayerInfo(self):
        ...
    def _updateDeathInfo(self):
        ...
    def _prepareMessage(self, code, killerVehID, device=None):
        ...
    def _makeKillerVO(self, vInfoVO):
        ...
    def _setDeadReasonInfo(self, vInfoVO, reason, showVehicle, vehLvl, vehImg, vehClass, vehName, killerUserVO):
        ...
    def __canRespawn(self):
        ...
    def __hasAliveTeammate(self):
        ...
    def __onSoulCollectorProgress(self, collected, capacity, isFull, isCampActivated):
        ...
