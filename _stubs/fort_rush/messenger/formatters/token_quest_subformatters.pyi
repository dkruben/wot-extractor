# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.helpers.utils import isFREventProgressionQuest as isFREventProgressionQuest
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from messenger.formatters.token_quest_subformatters import SyncTokenQuestsSubFormatter as SyncTokenQuestsSubFormatter

class FortRushProgressionQuestFormatter(SyncTokenQuestsSubFormatter):
    def format(self, message, *args):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
