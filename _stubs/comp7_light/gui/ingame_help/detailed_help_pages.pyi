# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/ingame_help/detailed_help_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen import R as R
from comp7_core.gui.ingame_help.detailed_help_pages import Comp7CorePagesBuilder as Comp7CorePagesBuilder
from comp7_light_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from comp7_light.gui.ingame_help import HelpPagePriority as HelpPagePriority

class Comp7LightPagesBuilder(Comp7CorePagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    _MODE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7Light
    _MODE_RES_ROOT_IMAGES = R.images.comp7_light.gui.maps.icons.battleHelp
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...
