# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/rewards/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from dossiers2.custom.account_layout import ACCOUNT_DOSSIER_BLOCKS as ACCOUNT_DOSSIER_BLOCKS
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from gui.server_events.bonuses import HIDDEN_BONUSES as HIDDEN_BONUSES
from gui.shared.gui_items.dossier import getAchievementFactory as getAchievementFactory
from web.web_client_api import W2CSchema as W2CSchema, Field as Field, w2capi as w2capi, w2c as w2c, WebCommandException as WebCommandException
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.server_events import IEventsCache as IEventsCache

class _RequestMedalsSchema(W2CSchema):
    medal_ids: Any

class _RequestQuestBonusSchema(W2CSchema):
    quest_id_base: Any

class _RequestAchievementsSchema(W2CSchema):
    medal_ids: Any
    achievement_block: Any

# decorador original: @w2capi(...)
class RewardsWebApi(W2CSchema):
    itemsCache: Any
    eventsCache: Any
    # decorador original: @w2c(...)
    def requestRewardInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def requestQuestBonusesInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getAchievements(self, cmd):
        ...
    def __getBonusesInfoByQuestsBaseToken(self, questIdBase):
        ...

def _achievementBlockValidator(block, _=None):
    ...
