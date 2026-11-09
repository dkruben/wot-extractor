# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rally/action_button_state_vo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.PLATOON import PLATOON as PLATOON
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.shared.formatters import text_styles as text_styles, icons as icons
from helpers import i18n as i18n
from shared_utils import BoundMethodWeakref as BoundMethodWeakref
_EXT_INVALID_UNIT_MESSAGE_GETTERS: list

class ActionButtonStateVO(dict):
    __NOT_CRITICAL_STATES: tuple
    _playerInfo: Any
    __unitIsValid: Any
    __restrictionType: Any
    __validationCtx: Any
    __isEnabled: Any
    __stats: Any
    __flags: Any
    __settings: Any
    __canTakeSlot: Any
    __INVALID_UNIT_MESSAGES: Any
    __WARNING_UNIT_MESSAGES: Any
    __NEUTRAL_UNIT_MESSAGES: Any
    def __init__(self, unitEntity):
        ...
    def getSimpleState(self):
        ...
    def isReadinessTooltip(self):
        ...
    def __getNotAvailableIcon(self):
        ...
    def _getReadyValidInSlotStateStr(self):
        ...
    def _getIdleStateStr(self):
        ...
    def _getArenaStateStr(self):
        ...
    def _isEnabled(self, isValid, restriction):
        ...
    def _getLabel(self):
        ...
    def _rotationGroupBlockMessage(self):
        ...
    def _notInSlotMessage(self):
        ...
    def _getUnitReadyMessage(self):
        ...
    def _getVehiclesGroupIsFullMessage(self):
        ...
    def __getState(self):
        ...
    @property
    def __toolTipData(self):
        ...
    def _clanMembersNotEnoughMessage(self):
        ...
    def __stateTextStyleFormatter(self, state):
        ...
    @staticmethod
    def getInvalidVehicleLevelsMessage(ctx):
        ...
