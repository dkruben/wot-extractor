# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanInvitesView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES as CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.clans import formatters as formatters
from gui.clans.data_wrapper.utils import formatField as formatField, isValueAvailable as isValueAvailable
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesAbstractDataProvider as ClanInvitesAbstractDataProvider
from gui.Scaleform.daapi.view.meta.ClanInvitesViewMeta import ClanInvitesViewMeta as ClanInvitesViewMeta
from gui.clans.settings import CLAN_INVITE_STATES as CLAN_INVITE_STATES
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from helpers.i18n import makeString as _ms
from debug_utils import LOG_DEBUG as LOG_DEBUG

class ClanInvitesView(ClanInvitesViewMeta):
    @property
    def allInvitesPaginator(self):
        ...
    @property
    def actualInvitesPaginator(self):
        ...
    @property
    def expiredInvitesPaginator(self):
        ...
    @property
    def processedInvitesPaginator(self):
        ...
    def onClanInvitesCountReceived(self, clanDbID, invitesCount):
        ...
    def _onAttachedToWindow(self):
        ...
    def _createSearchDP(self):
        ...
    def _getViewAlias(self):
        ...
    def _showDummyByFilterName(self, filterName):
        ...
    def _getDefaultFilterName(self):
        ...
    def _getDefaultSortFields(self):
        ...
    def _getSecondSortFields(self):
        ...
    def _makeFilters(self):
        ...
    def _makeHeaders(self):
        ...

class InviteDataProvider(ClanInvitesAbstractDataProvider):
    def _makeVO(self, item, extraData):
        ...
    def _makeRequestTooltip(self, status, date, user=None):
        ...
