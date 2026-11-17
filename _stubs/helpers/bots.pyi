# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/bots.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import unicodedata as unicodedata
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from constants import LocalizableBotName as LocalizableBotName, BotNamingType as BotNamingType, IS_DEVELOPMENT as IS_DEVELOPMENT
from items import tankmen as tankmen, vehicles as vehicles
from helpers import getLanguageCode as getLanguageCode, i18n as i18n
_NAME_FORMAT_CREW_WINBACK = '{0}_{1}'
_NAME_FORMAT_CREW = ':{0} {1}:'
_DEV_PREFIX_FORMAT_CREW = '{0}_{1}_{2} '
_DEV_PREFIX_FORMAT_VEHICLE = '[{0}] '
_DEV_PREFIX_FORMAT_CUSTOM = '[{0}] '
_WINBACK_ENGLISH_CREW_CODES: tuple

def preprocessBotName(name, arenaBonusType=...):
    ...
def _removeSpecialSymbols(unicodeStr):
    ...
