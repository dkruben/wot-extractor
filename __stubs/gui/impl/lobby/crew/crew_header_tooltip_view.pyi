# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_header_tooltip_view_model import CrewHeaderTooltipViewModel as CrewHeaderTooltipViewModel
from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonusEnum as IdleCrewBonusEnum
from gui.impl.pub import ViewImpl as ViewImpl
from gui.game_control.wot_plus.utils import getPassiveCrewXPPerMinuteFromAllTiers as getPassiveCrewXPPerMinuteFromAllTiers
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items import Vehicle as Vehicle
_MINUTES_MULTIPLICATOR = 5

class CrewHeaderTooltipView(ViewImpl):
    __slots__: tuple
    _wotPlusCtrl: Any
    _itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, idleCrewBonus):
        ...
