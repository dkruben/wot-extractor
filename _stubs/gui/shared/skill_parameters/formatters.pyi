# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/skill_parameters/formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl import backport as backport
from gui.impl.backport import getNiceNumberFormat as getNiceNumberFormat
from gui.impl.gen import R as R
from gui.shared.gui_items import VEHICLE_ATTR_TO_KPI_NAME_MAP as VEHICLE_ATTR_TO_KPI_NAME_MAP
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText as getVehicleParameterText
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.components.skills_constants import ParamMeasureType as ParamMeasureType, ParamSignType as ParamSignType
from math_common import decimal_round as decimal_round
from items.readers.skills_readers import SkillDescrsArg as SkillDescrsArg

def getDescriptionValue(paramDescrArg, value):
    ...
def _formatParamValue(paramDescrArg, value):
    ...
def getMeasureText(value, perkparamDescrArg):
    ...
def getKpiValue(paramDescrArg, value):
    ...
def getParamSign(value):
    ...
def getKpiDescription(paramDescrArg):
    ...
