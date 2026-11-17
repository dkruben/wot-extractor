# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/ingame_help/detailed_help_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7_core.gui.ingame_help.detailed_help_pages import Comp7CorePagesBuilder as Comp7CorePagesBuilder
from comp7_common.comp7_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from comp7.gui.ingame_help import HelpPagePriority as HelpPagePriority
from gui.impl.gen import R as R

class Comp7PagesBuilder(Comp7CorePagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    _PAGE_NAMES: tuple
    _MODE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7
    _MODE_RES_ROOT_IMAGES = R.images.comp7.gui.maps.icons.battleHelp
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...
