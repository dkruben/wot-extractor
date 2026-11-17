# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/ingame_help/detailed_help_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.ingame_help.detailed_help_pages import DetailedHelpPagesBuilder as DetailedHelpPagesBuilder, addPage as addPage
from gui.shared.formatters import text_styles as text_styles
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Union as Union, List as List, Any as Any
from frameworks.wulf import PyResAccessor as PyResAccessor

class Comp7CorePagesBuilder(DetailedHelpPagesBuilder):
    _PAGE_NAMES: tuple
    _CORE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7Core
    _CORE_RES_ROOT_IMAGES = R.images.comp7_core.gui.maps.icons.battleHelp
    _MODE_RES_ROOT_TEXTS = None
    _MODE_RES_ROOT_IMAGES = None
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _getPageResBranchTexts(cls, pageName):
        ...
    @classmethod
    def _getPageResBranchImages(cls, pageName):
        ...
    @classmethod
    def _getHeader(cls, pageName):
        ...
    @classmethod
    def _getTitle(cls, pageName):
        ...
    @classmethod
    def _getDescr(cls, pageName):
        ...
    @classmethod
    def _getImage(cls, pageName):
        ...
