# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/personal_case/personal_data_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CREW_SKINS_VIEWED as CREW_SKINS_VIEWED
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.dialogs.dialogs import showSkinApplyDialog as showSkinApplyDialog, showDocumentChangeDialog as showDocumentChangeDialog
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.filter_panel_widget_model import FilterPanelType as FilterPanelType
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import PersonalDataCardModel as PersonalDataCardModel, DataCardState as DataCardState, DataCardType as DataCardType
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_view_model import PersonalDataViewModel as PersonalDataViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.crew.filter import getPersonalDataCardTypeSettings as getPersonalDataCardTypeSettings
from gui.impl.lobby.crew.filter.data_providers import CompoundDataProvider as CompoundDataProvider, CrewSkinsDataProvider as CrewSkinsDataProvider, DocumentsDataProvider as DocumentsDataProvider
from gui.impl.lobby.crew.filter.filter_panel_widget import FilterPanelWidget as FilterPanelWidget
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.impl.lobby.crew.personal_case import IPersonalTab as IPersonalTab
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, Tankman as Tankman
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName, CrewSkin as CrewSkin, GenderRestrictionsLocales as GenderRestrictionsLocales
from gui.shared.gui_items.processors.tankman import CrewSkinUnequip as CrewSkinUnequip
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.components.crew_skins_constants import CREW_SKIN_PROPERTIES_MASKS as CREW_SKIN_PROPERTIES_MASKS, TANKMAN_SEX as TANKMAN_SEX
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from frameworks.wulf import Array as Array

class PersonalDataView(IPersonalTab, ViewImpl):
    __slots__: tuple
    TITLE: Any
    itemsCache: Any
    lobbyContext: Any
    platoonCtrl: Any
    tankmanID: Any
    __tankman: Any
    __filterState: Any
    filterPanelWidget: Any
    __dataProviders: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def tankman(self):
        ...
    def onChangeTankman(self, tankmanID):
        ...
    def onStopAnimations(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    @staticmethod
    def getTooltipData(event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _clear(self):
        ...
    def _finalize(self):
        ...
    def __onMembersUpdate(self):
        ...
    def __onInventoryUpdate(self, invDiff):
        ...
    # decorador original: @args2params(...)
    def __onNewCardViewed(self, cardID):
        ...
    # decorador original: @wg_async
    # decorador original: @args2params(...)
    def __onCardSelected(self, cardID, isSkin):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __unEquipCrewSkin(self):
        ...
    def __onResetFilters(self):
        ...
    def __onFilterStateUpdated(self):
        ...
    def __fillModel(self):
        ...
    def __fillSelectedCard(self, card):
        ...
    def __fillDocuments(self, cards):
        ...
    def __fillDocumentCard(self, card, cardId, icon, firstname, lastname):
        ...
    def __fillCrewSkins(self, cards):
        ...
    def __fillSkinCard(self, card, crewSkin):
        ...
    def __isTankmanLocked(self):
        ...
