# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.banner_tooltip_model import BannerTooltipModel as BannerTooltipModel
from gui.shared.formatters.ranges import toRangeString as toRangeString, toRomanRangeString as toRomanRangeString
from gui.shared.utils import isRomanNumberForbidden as isRomanNumberForbidden
from frontline.gui.frontline_helpers import getFrontlineState as getFrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState as FrontlineState
from frontline.constants.common import STATES_MAP as STATES_MAP
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP as FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP

class BannerTooltipView(ViewImpl):
    __epicController: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
