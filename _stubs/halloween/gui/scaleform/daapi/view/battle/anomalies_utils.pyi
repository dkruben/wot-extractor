# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/anomalies_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import re as re
from builtins import range as range
import typing as typing
import BigWorld as BigWorld
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.configs.hw_upgrades_config import getConfig as getConfig
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui import makeHtmlString as makeHtmlString
from gui.battle_control import avatar_getter as avatar_getter
from typing import Optional as Optional, List as List, Set as Set
_TEXT_PATH_ANOMALIES = R.strings.halloween_buffs.buffs

class _StyleBase(object):
    DEFAULT_STYLE = ''
    EPIC_STYLE = ''
    SECRET_STYLE = ''
    @classmethod
    def getStyle(cls, isEpic=False, isSecret=False):
        ...

class _ParamStyle(_StyleBase):
    DEFAULT_STYLE = 'boldTitle'
    EPIC_STYLE = 'boldTitleEpic'
    SECRET_STYLE = 'boldTitleSecret'

class _DescriptionStyle(_StyleBase):
    DEFAULT_STYLE = 'hwAnomalyDescriptor'
    EPIC_STYLE = 'hwAnomalyDescriptorEpic'
    SECRET_STYLE = 'hwAnomalyDescriptorSecret'

class _TitleStyle(_StyleBase):
    DEFAULT_STYLE = 'title'
    EPIC_STYLE = 'titleEpic'
    SECRET_STYLE = 'titleSecret'

# decorador original: @dependency.replace_none_kwargs(...)
def selectAnomaly(anomalyIDx=None, anomalyID=None, sessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isAnomalyInCombo(anomalyID, anomaliesCtrl=None):
    ...
def isAnomalyNew(anomalyID):
    ...
def _getParams(anomalyName):
    ...
def anomalyHeader(anomalyName):
    ...
def anomalyBody(anomalyName):
    ...
def anomalyTitle(anomalyName, isEpic=False, isSecret=False):
    ...
def anomalyDescriptionList(anomalyName, valueConvert=None, isEpic=False, isSecret=False):
    ...
def getKnownAnomaliesIDs():
    ...
