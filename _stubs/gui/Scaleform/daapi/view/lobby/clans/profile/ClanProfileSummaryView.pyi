# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileSummaryView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from adisp import adisp_process as adisp_process
from constants import IS_CHINA as IS_CHINA
from gui.Scaleform.daapi.view.meta.ClanProfileSummaryViewMeta import ClanProfileSummaryViewMeta as ClanProfileSummaryViewMeta
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES as _STYLE
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.clans.clan_helpers import isStrongholdsEnabled as isStrongholdsEnabled
from gui.clans.data_wrapper.utils import formatField as formatField, isValueAvailable as isValueAvailable
from gui.clans.formatters import DUMMY_UNAVAILABLE_DATA as DUMMY_UNAVAILABLE_DATA
from gui.clans.items import StrongholdStatisticsData as StrongholdStatisticsData
from gui.clans.settings import CLIENT_CLAN_RESTRICTIONS as _RES
from gui.impl import backport as backport
from gui.shared.events import OpenLinkEvent as OpenLinkEvent
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.image_helper import ImagesFetchCoordinator as ImagesFetchCoordinator
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper as UsersInfoHelper
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_DIVISIONS: tuple
_STATES: dict

class StrongholdDataReceiver(object):
    __disposed: Any
    __clanDossier: Any
    __updateStrongholdCallback: Any
    __strongholdStats: Any
    __imagesFetchCoordinator: Any
    def __init__(self, clanDossier, updateStrongholdCallback):
        ...
    def getStatsVO(self):
        ...
    def getLeaguesVO(self):
        ...
    def dispose(self):
        ...
    # decorador original: @adisp_process
    def updateStrongholdStatistics(self):
        ...
    def __updateStrongholdStatistics(self):
        ...

class ClanProfileSummaryView(ClanProfileSummaryViewMeta, UsersInfoHelper):
    _lobbyContext: Any
    __stateMask: Any
    __strongholdStatsVOReceiver: Any
    _isGlobalMapEnabled: Any
    _dummyMustBeShown: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def setClanDossier(self, clanDossier):
        ...
    def onAccountWebVitalInfoChanged(self, fieldName, value):
        ...
    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        ...
    # decorador original: @adisp_process
    def onAccountClanProfileChanged(self, profile):
        ...
    def onClanEmblem128x128Received(self, clanDbID, emblem):
        ...
    def onClanEmblem256x256Received(self, clanDbID, emblem):
        ...
    # decorador original: @adisp_process
    def onUserNamesReceived(self, names):
        ...
    def hyperLinkGotoDetailsMap(self):
        ...
    def hyperLinkGotoMap(self):
        ...
    def sendRequestHandler(self):
        ...
    def _onAppSuccessfullySent(self):
        ...
    def _updateClanEmblem(self, clanDbID):
        ...
    def _updateHeaderState(self):
        ...
    def _dispose(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __updateStrongholdBlock(self, stats, leagues=None):
        ...
    def __makeGeneralBlock(self, clanInfo, syncUserInfo=False):
        ...
    def __makeGlobalMapBlock(self, globalMapStats, ratings):
        ...
    def __makeStatsBlock(self, listValues):
        ...
    def __makeLeaguesBlock(self, leagues):
        ...
    def __updateStatus(self):
        ...

def _stateVO(showRequestBtn, mainStatus=None, tooltip='', enabledRequestBtn=False, addStatus=None, showPersonalBtn=False):
    ...
def _status(i18nKey, style, icon=None):
    ...
