# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE as COMP7_PREBATTLE_CAROUSEL_ROW_VALUE
from comp7_core.gui.Scaleform.daapi.view.battle.common import getSavedRowCountValue as getSavedRowCountValue, rowValueToRowCount as rowValueToRowCount, rowCountToRowValue as rowCountToRowValue
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION as FILTER_POPOVER_SECTION
from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover as TankCarouselFilterPopover
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles

class Comp7TankCarouselFilterPopover(TankCarouselFilterPopover):
    _carouselRowCount: Any
    def switchCarouselType(self, selected):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _readRowCount(self, ctx):
        ...
    def _saveRowCount(self):
        ...
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...
    def __saveRowCountValue(self):
        ...
