# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanInvitesWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from functools import partial as partial
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import gui as gui
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.daapi.view.meta.ClanInvitesWindowMeta import ClanInvitesWindowMeta as ClanInvitesWindowMeta
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES as CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.clans import formatters as formatters
from gui.clans.clan_helpers import ClanInvitesPaginator as ClanInvitesPaginator
from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.clans.settings import CLAN_INVITE_STATES as CLAN_INVITE_STATES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showClanSendInviteWindow as showClanSendInviteWindow
from gui.shared.events import CoolDownEvent as CoolDownEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.view_helpers import CooldownHelper as CooldownHelper
from gui.shared.view_helpers.emblems import ClanEmblemsHelper as ClanEmblemsHelper
from gui.wgcg.clan.contexts import ClanApplicationsCtx as ClanApplicationsCtx, ClanInvitesCtx as ClanInvitesCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from helpers import dependency as dependency
from helpers import i18n as i18n
from helpers.i18n import makeString as _ms
from skeletons.gui.web import IWebController as IWebController

class ClanInvitesWindow(ClanInvitesWindowMeta, ClanListener, ClanEmblemsHelper):
    __coolDownRequests: list
    __actualRequestsCount: Any
    __processedInvitesCount: Any
    _cooldown: Any
    __clanDbID: Any
    __clanDossier: Any
    __pagiatorsController: Any
    def __init__(self, *args, **kwargs):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def onAccountClanProfileChanged(self, profile):
        ...
    def onClanInfoReceived(self, clanDbID, clanInfo):
        ...
    def onInvitesButtonClick(self):
        ...
    def onWindowClose(self):
        ...
    def onClanEmblem128x128Received(self, clanDbID, emblem):
        ...
    @property
    def clanProfile(self):
        ...
    @property
    def paginatorsController(self):
        ...
    @property
    def clanInfo(self):
        ...
    def resyncClanInfo(self, force=False):
        ...
    def showWaiting(self, show):
        ...
    def formatInvitesCount(self, paginator):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onCooldownHandle(self, isInCooldown):
        ...
    def _onPaginatorListChanged(self, alias, f, selectedID, isFullUpdate, isReqInCoolDown, result):
        ...
    def _updateClanEmblem(self):
        ...
    def _updateClanInfo(self):
        ...
    def _updateHeaderState(self):
        ...
    def __updateTabsState(self):
        ...

class _PaginatorsController(object):
    clanCtrl: Any
    __clanDbID: Any
    __paginators: Any
    def __init__(self, clanDbID):
        ...
    def getPanginator(self, viewAlias, f):
        ...
    def setCallback(self, callback):
        ...
    def removeCallbacks(self):
        ...
    def resetAllPanginators(self):
        ...
    def markPanginatorsAsUnSynced(self, viewAlias):
        ...
    def isInProgress(self):
        ...
    def __setUpPaginators(self):
        ...
    def __addPaginator(self, viewAlias, f, panginator):
        ...
