# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from account_helpers.AccountSettings import AccountSettings as AccountSettings, MODE_SELECTOR_BATTLE_PASS_SHOWN as MODE_SELECTOR_BATTLE_PASS_SHOWN
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import BattlePassState as BattlePassState
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel as ModeSelectorNormalCardModel
BATTLE_PASS_SEASON_ID = 'seasonId'
_arenaBonusTypeByModeName: dict

def setBattlePassState(itemVM):
    ...
def resetBattlePassStateForItem(itemVM):
    ...
def saveBattlePassStateForItem(modeSelectorItem, value):
    ...
def saveBattlePassStateForItems(itemList):
    ...
