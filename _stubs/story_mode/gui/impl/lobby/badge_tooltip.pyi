# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/badge_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.utils import getPlayerName as getPlayerName
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.shared import IItemsCache as IItemsCache
from story_mode.gui.impl.gen.view_models.views.lobby.badge_tooltip_view_model import BadgeTooltipViewModel as BadgeTooltipViewModel

class BadgeTooltip(ViewImpl):
    __itemsCache: Any
    _DEFAULT_ICON: Any
    _DEFAULT_LEVEL = 'I'
    _badgeId: Any
    def __init__(self, badgeId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
