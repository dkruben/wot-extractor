# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/shared/fun_system_factory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.system_factory import CollectEventsManager as CollectEventsManager
__collectFunRandomEM: Any

class FunFactoryConstants(object):
    SUB_MODE = 0
    BATTLE_RESULTS_SUB_FORMATTER = 1
    BATTLE_RESULTS_SUB_PRESENTER = 2
    BATTLE_RESULTS_SOUND_ENV = 3
    MODE_ASSETS_PACK_CONFIG_PATH = 4

def registerFunRandomSubMode(subModeImpl, subMode):
    ...
def collectFunRandomSubMode(subModeImpl):
    ...
def registerBattleResultsMessageSubFormatter(arenaGuiType, battleResultsFormatterCls):
    ...
def collectBattleResultsMessageSubFormatter(arenaGuiType):
    ...
def registerBattleResultsSubPresenter(subModeImpl, subPresenterCls, viewCls):
    ...
def collectBattleResultsSubPresenters():
    ...
def registerBattleResultsSoundEnv(arenaGuiType, battleResultsSoundEnvCls):
    ...
def collectBattleResultsSoundEnv(arenaGuiType):
    ...
def registerModeAssetsPackConfigPath(assetsPointer, path):
    ...
def collectModeAssetsPackConfigPath(assetsPointer):
    ...
