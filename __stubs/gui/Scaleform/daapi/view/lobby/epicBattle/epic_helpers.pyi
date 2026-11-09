# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/epic_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.ALERTMESSAGE_CONSTANTS import ALERTMESSAGE_CONSTANTS as ALERTMESSAGE_CONSTANTS
from gui.shared.formatters import time_formatters as time_formatters, text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.periodic_battles.models import AlertData as AlertData, PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils
from items import vehicles as vehicles
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from math_common import round_py2_style as round_py2_style, decimal_round as decimal_round
from shared_utils import first as first
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
_logger: Any
FRONTLINE_HIDDEN_TAG = 'fr_hidden'
_EPIC_GAME_PARAMS: dict
epicEquipmentParameterFormaters: dict

class AbilityParam(object):
    @classmethod
    def updateParams(cls, curEq, param):
        ...

class DisplayValuesMixin(object):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class DirectValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class NestedValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...
    @classmethod
    def _getEqParam(cls, eq, params):
        ...

class PercentValueMixin(DirectValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class AbsPercentValueMixin(DirectValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class NestedPercentValueMixin(NestedValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class NestedAbsPercentTupleValueMixin(NestedValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class DirectPercentValueMixin(DirectValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class NestedDirectPercentValueMixin(NestedValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class ReciprocalValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class ShellStunValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class NestedShellStunValuesMixin(NestedValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class MultiValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getParamValue(cls, curEq, param):
        ...

class TextParam(AbilityParam, DisplayValuesMixin):
    @classmethod
    def updateParams(cls, curEq, param):
        ...

class MultiTextParam(AbilityParam, DisplayValuesMixin):
    @classmethod
    def updateParams(cls, curEq, param):
        ...

class FixedTextParam(AbilityParam):
    @classmethod
    def updateParams(cls, curEq, param):
        ...

class DirectNumericTextParam(TextParam, DirectValuesMixin):
    ...

class DirectSecondsTextParam(TextParam, DirectValuesMixin):
    ...

class DirectMetersTextParam(TextParam, DirectValuesMixin):
    ...

class NestedNumericTextParam(TextParam, NestedValuesMixin):
    ...

class NestedMetersTextParam(TextParam, NestedValuesMixin):
    ...

class PercentNumericTextParam(TextParam, PercentValueMixin):
    ...

class AbsPercentNumericTextParam(TextParam, AbsPercentValueMixin):
    ...

class NestedPercentNumericTextParam(TextParam, NestedPercentValueMixin):
    ...

class NestedAbsPercentNumbericTextParam(TextParam, NestedAbsPercentTupleValueMixin):
    ...

class DirectPercentNumericTextParam(TextParam, DirectPercentValueMixin):
    ...

class NestedDirectPercentNumericTextParam(TextParam, NestedDirectPercentValueMixin):
    ...

class ReciprocalNumericTextParam(TextParam, ReciprocalValuesMixin):
    ...

class ShellStunSecondsDeltaBarParam(TextParam, ShellStunValuesMixin):
    ...

class NestedShellStunSecondsDeltaBarParam(TextParam, NestedShellStunValuesMixin):
    ...

class MultipleMetersTextParam(MultiTextParam, MultiValuesMixin):
    ...

def _getAttrName(param):
    ...
def _cutDigits(value):
    ...
def _getFormattedNum(value):
    ...
def checkIfVehicleIsHidden(intCD):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isVehLevelUnlockableInBattle(vehLevel, epicController=None):
    ...
def getFrontLineSkills():
    ...
def createEpicParam(curLvlEq, tooltipIdentifier):
    ...
def getTimeToEndStr(timeStamp):
    ...
def getTimeToStartStr(timeStamp):
    ...
def getOfferTokenByGift(tokenID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAlertStatusVO(epicController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getAlertStatusText(timeLeft, hasAvailableServers, connectionMgr=None, epicController=None):
    ...
def _getTimeLeftStr(timeStamp):
    ...
