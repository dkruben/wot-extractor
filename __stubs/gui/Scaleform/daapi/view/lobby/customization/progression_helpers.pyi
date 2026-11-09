# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/progression_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import binascii as binascii
import logging as logging
import struct as struct
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import EVENT_TYPE as EVENT_TYPE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events import formatters as formatters
from gui.server_events.events_helpers import MISSIONS_STATES as MISSIONS_STATES
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from helpers.i18n import makeString as _ms
from gui.shared.system_factory import collectCustomizationHangarDecorator as collectCustomizationHangarDecorator
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
C11nProgressionLinkBtnParams: Any

def makeEventID(itemIntCD, vehicleIntCD):
    ...
def parseEventID(eventID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getProgressionPostBattleInfo(itemIntCD, vehicleIntCD, progressionData, itemsCache=None):
    ...
def getProgressiveCustomizationProgress(reusable):
    ...
def getC11nProgressionLinkBtnParams(vehicle):
    ...
def getC11n2dProgressionLinkBtnParams():
    ...
def __makeAwardsVO(item, level, vehicleIntCD):
    ...
def __makeProgressList(item, level, progressionData):
    ...
def __makeProgressVO(conditionId, description, maxProgress, currentProgress, progressDiff):
    ...
