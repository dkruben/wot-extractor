# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/formatters/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.role_presenter_helper import getRoleUserName as getRoleUserName
from helpers import i18n as i18n
from prebattle_shared import LIMIT_DEFAULTS as LIMIT_DEFAULTS

def getAbsenceCrewList():
    ...
def getCrewNotFullTooltip():
    ...
def getVehicleStateInvalidTooltip(restriction):
    ...
def getVehicleClassInvalidTooltip(teamsLimit, restriction):
    ...
def getLevelInvalidTooltip(teamLimits, restriction):
    ...
def getTotalLevelInvalidTooltip(teamsLimit, restriction):
    ...
def getActionDisabledTooltip(restriction, entity=None):
    ...
