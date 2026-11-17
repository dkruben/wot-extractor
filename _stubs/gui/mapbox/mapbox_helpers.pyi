# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/mapbox/mapbox_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ArenaType as ArenaType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import AlertData as AlertData
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus, PeriodType as PeriodType
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.server_events.bonuses import getServiceBonuses as getServiceBonuses
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency, time_utils as time_utils
from helpers.time_utils import getTimestampFromISO as getTimestampFromISO
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IMapboxController as IMapboxController
from frameworks.wulf import ViewEvent as ViewEvent
from frameworks.wulf.windows_system.window import Window as Window
SPECIAL_CARDS: tuple
_MECHANICS_CARDS: tuple
_ALL_NON_MAPS_CARDS: Any
_BATTLE_ENDED_PERIODS: Any
_BONUS_FORMAT_ADAPTERS: dict

def convertTimeFromISO(timeStr):
    ...
def getMapboxRewardTooltip(event, tooltipData, parentWindow):
    ...
def getPrimeTimeStatusVO():
    ...
def getTillTimeString(timeStamp):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMapboxBattlesStatus(mapboxCtrl=None):
    ...
def prepareProgressionData(mapsData, validMaps):
    ...
def formatMapboxBonuses(reward):
    ...
def formatMapboxRewards(reward):
    ...
def _adaptMapboxDossierFormat(dossierValue):
    ...
def _adaptCDKeys(itemValue):
    ...
