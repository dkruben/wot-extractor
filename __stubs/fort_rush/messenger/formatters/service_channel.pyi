# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ArenaType as ArenaType
from fort_rush_common.fort_rush_constants import EventStates as EventStates
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.money import Currency as Currency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import BattleResultsFormatter as BattleResultsFormatter, ServiceChannelFormatter as ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData

class FortRushBattleResultsFormatter(BattleResultsFormatter):
    _battleResultKeys: dict
    def _prepareFormatData(self, message):
        ...

class FortRushEventStatesFormatter(ServiceChannelFormatter):
    __TEMPLATES: dict
    def format(self, message, *args):
        ...
