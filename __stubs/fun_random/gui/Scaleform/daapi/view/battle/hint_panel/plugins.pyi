# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/battle/hint_panel/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import FUN_RANDOM_HINT_SECTION as FUN_RANDOM_HINT_SECTION, HINTS_LEFT as HINTS_LEFT
from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext as HelpHintContext
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode as hasBattleSubMode
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HintPriority as HintPriority
from gui.Scaleform.daapi.view.battle.shared.hint_panel.plugins import PreBattleHintPlugin as PreBattleHintPlugin, HelpPlugin as HelpPlugin

class FunRandomPreBattleHintPlugin(PreBattleHintPlugin, FunSubModesWatcher):
    @classmethod
    # decorador original: @hasBattleSubMode(...)
    def isSuitable(cls):
        ...

class FunRandomHelpPlugin(HelpPlugin, FunSubModesWatcher):
    def __init__(self, parentObj):
        ...
    @classmethod
    # decorador original: @hasBattleSubMode(...)
    def isSuitable(cls):
        ...

def updatePlugins(plugins):
    ...
