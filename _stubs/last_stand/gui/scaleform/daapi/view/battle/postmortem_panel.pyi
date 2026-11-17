# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.battle_control import avatar_getter as avatar_getter
from last_stand.gui.scaleform.daapi.view.meta.PostmortemPanelMeta import PostmortemPanelMeta as PostmortemPanelMeta
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole as getVehicleRole
_ATTACK_REASON_MSG_TO_EVENT: dict

class LSPostmortemPanel(PostmortemPanelMeta):
    TICK_RATE = 1
    RESPAWN_TITLE: Any
    RESPAWN_INFO: Any
    __slots__: tuple
    _callbacks: Any
    def __init__(self):
        ...
    @property
    def _isRespawnEnabledOnServer(self):
        ...
    @property
    def _isLastPhase(self):
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
