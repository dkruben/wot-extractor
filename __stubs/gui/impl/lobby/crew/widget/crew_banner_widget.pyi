# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/widget/crew_banner_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_banner_widget_model import CrewBannerWidgetModel as CrewBannerWidgetModel
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getPerksResetGracePeriod as getPerksResetGracePeriod
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showResetAllPerksDialog as showResetAllPerksDialog, showFillAllPerksDialog as showFillAllPerksDialog
from gui.shared.gui_items.items_actions.actions import ResetAllTankmenSkillsAction as ResetAllTankmenSkillsAction, FillAllTankmenSkillsAction as FillAllTankmenSkillsAction
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_await as wg_await, wg_async as wg_async

class CrewBannerWidget(ViewImpl):
    LAYOUT_ID = R.views.lobby.crew.widgets.CrewBannerWidget
    lobbyContext: Any
    itemsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def fillModel(self):
        ...
    # decorador original: @wg_async
    def __onFill(self):
        ...
    # decorador original: @wg_async
    def __onReset(self):
        ...
