# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/bonuses_wot_plus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.server_events import bonuses as wotp_b
from renewable_subscription_common.schema import Features as Features
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from gui.server_events.bonuses import WoTPlusBonus as WoTPlusBonus
_FEATURE_TO_BONUS_ORDER_LIST: tuple

def _baseArgsProvider(storage):
    ...
def _updateList(bonusList, bunusClass, bonusArguments):
    ...
def _updateBonusList(bonusList, featureIDList, storage):
    ...
def _getAvailableBonusesForTier(storage, tierID):
    ...
def getAvailableCoreBonuses(storage):
    ...
def getAvailableProBonuses(storage):
    ...
def getUniqueAvailableProBonuses(storage):
    ...
def getSubscriptionAvailableBonuses(storage):
    ...
