# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/search/ClanSearchInfo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from adisp import adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import HeaderItemsTypes as HeaderItemsTypes, ProfileUtils as ProfileUtils
from gui.Scaleform.daapi.view.meta.ClanSearchInfoMeta import ClanSearchInfoMeta as ClanSearchInfoMeta
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.clans import formatters as clans_fmts
from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.clans.settings import CLIENT_CLAN_RESTRICTIONS as CLIENT_CLAN_RESTRICTIONS, MAX_CLAN_MEMBERS_COUNT as MAX_CLAN_MEMBERS_COUNT
from gui.impl import backport as backport
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.view_helpers import ClanEmblemsHelper as ClanEmblemsHelper
from gui.wgcg.base.contexts import CreateApplicationCtx as CreateApplicationCtx
from helpers.i18n import makeString as _ms

class ClanSearchInfo(ClanSearchInfoMeta, ClanListener, ClanEmblemsHelper):
    __dataProvider: Any
    __selectedClan: Any
    def __init__(self):
        ...
    def bindDataProvider(self, dataProvider):
        ...
    def openClanProfile(self):
        ...
    def onAccountClanProfileChanged(self, profile):
        ...
    # decorador original: @adisp_process
    def sendRequest(self):
        ...
    def requestData(self, clanId):
        ...
    def onClanEmblem128x128Received(self, clanDbID, emblem):
        ...
    def _populate(self):
        ...
    def _updateClanEmblem(self):
        ...
    def _updateDetailedInfo(self):
        ...
    def _updateSetaledState(self):
        ...
    def __initControls(self):
        ...

class _ClanAdapter(object):
    __clanInfo: Any
    def __init__(self, clanInfo):
        ...
    def getDbID(self):
        ...
    def canAcceptsJoinRequests(self):
        ...
    def hasFreePlaces(self):
        ...

def _packItemData(text, description, tooltip, icon):
    ...
