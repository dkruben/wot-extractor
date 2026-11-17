# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_pass.battle_pass_constants import ChapterState as ChapterState
from gui.game_control.wallet import WalletController as WalletController
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils.requesters import IStatsRequester as IStatsRequester
from typing import Dict as Dict
_BATTLE_PASS_CHAPTER_STATE_NAME: dict

def formatBalance(stats):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def formatWalletCurrencyStatuses(wallet=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def formatBattlePassInfo(battlePass=None):
    ...
