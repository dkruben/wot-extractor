# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/ingame_help/fun_random_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random_common.fun_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from fun_random.gui.ingame_help import HelpPagePriority as HelpPagePriority
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode as hasBattleSubMode
from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext as HelpHintContext
from gui.impl import backport as backport
from gui.ingame_help.detailed_help_pages import addPage as addPage, DetailedHelpPagesBuilder as DetailedHelpPagesBuilder
from gui.shared.formatters import text_styles as text_styles

class FunRandomHelpPagesBuilder(DetailedHelpPagesBuilder, FunSubModesWatcher):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def isExclusive(cls):
        ...
    @classmethod
    def priority(cls):
        ...
    @classmethod
    # decorador original: @hasBattleSubMode(...)
    def buildPages(cls, _):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...
