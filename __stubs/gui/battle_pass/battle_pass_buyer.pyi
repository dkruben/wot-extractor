# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_buyer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.battle_pass.battle_pass_constants import ChapterState as ChapterState
from gui.shared.event_dispatcher import showExchangeXPWindow as showExchangeXPWindow
from gui.shared.gui_items.processors.battle_pass import BuyBattlePass as BuyBattlePass, BuyBattlePassLevels as BuyBattlePassLevels, BuyBattlePassWithLevels as BuyBattlePassWithLevels
from gui.shared.money import Currency as Currency
from gui.shared.utils import decorators as decorators
from gui.shop import showBuyGoldForBattlePass as showBuyGoldForBattlePass, showBuyGoldForBattlePassLevels as showBuyGoldForBattlePassLevels
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, ISoundEventChecker as ISoundEventChecker
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class BattlePassBuyer(object):
    __itemsCache: Any
    __battlePass: Any
    __soundEventChecker: Any
    @classmethod
    # decorador original: @decorators.adisp_process(...)
    def buyBP(cls, seasonID, chapterID, onBuyCallback=None):
        ...
    @classmethod
    # decorador original: @decorators.adisp_process(...)
    def buyBPWithLevels(cls, seasonID, chapterID, onBuyCallback=None):
        ...
    @classmethod
    # decorador original: @decorators.adisp_process(...)
    def buyLevels(cls, seasonID, chapterID, levels=0, onBuyCallback=None):
        ...
    @classmethod
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __buyBattlePass(cls, seasonID, chapterID, callback):
        ...
    @staticmethod
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __buyBattlePassLevels(seasonID, chapterID, levels, callback):
        ...
    @classmethod
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __buyBattlePassWithLevels(cls, seasonID, chapterID, callback):
        ...
