# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/special_mode_battle/prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from collections import namedtuple as namedtuple
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import PrimeTimeViewBase as PrimeTimeViewBase
from gui.Scaleform.daapi.view.lobby.prime_time_servers_data_provider import PrimeTimesServersDataProvider as PrimeTimesServersDataProvider
from gui.shared.formatters import icons as icons, text_styles as text_styles
from helpers import time_utils as time_utils
from helpers.i18n import makeString as _ms
LocaleData: Any
ImgsData: Any

class SpecialModePrimeTimeView(PrimeTimeViewBase):
    def _getLocaleData(self):
        ...
    def _getImgsData(self):
        ...
    def _getAllServersDP(self):
        ...
    def _prepareData(self, serverList, serverName, serverTimeLeft):
        ...
    def _getPrbActionName(self, isEnabled):
        ...
    def _getEndSeasonTime(self):
        ...
    def _getTimeLeft(self, pID):
        ...
