# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rally/rally_dps.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.impl import backport as backport
from gui.prb_control import prbEntityProperty as prbEntityProperty
from helpers import dependency as dependency
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makePlayerVO as makePlayerVO, makeUnitShortVO as makeUnitShortVO, makeSortiePlayerVO as makeSortiePlayerVO, makeStaticFormationPlayerVO as makeStaticFormationPlayerVO, makeClanBattlePlayerVO as makeClanBattlePlayerVO
from gui.Scaleform.daapi.view.lobby.rally.data_providers import BaseRallyListDataProvider as BaseRallyListDataProvider
from gui.Scaleform.framework.entities.DAAPIDataProvider import DAAPIDataProvider as DAAPIDataProvider
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.prb_control.items.unit_items import UnitCandidatesSortKey as UnitCandidatesSortKey
from gui.shared.formatters import icons as icons, text_styles as text_styles
from helpers import i18n as i18n
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.proto import proto_getter as proto_getter
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class CandidatesDataProvider(DAAPIDataProvider):
    usersStorage: Any
    _list: Any
    _mapping: Any
    def __init__(self):
        ...
    def init(self, app, flashObject, candidates):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    @property
    def collection(self):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    def buildList(self, candidates):
        ...
    def _buildData(self, candidates):
        ...
    def _makePlayerVO(self, pInfo, user, colorGetter, isPlayerSpeaking):
        ...
    def emptyItem(self):
        ...
    def hasCandidate(self, dbID):
        ...
    def rebuild(self, candidates):
        ...
    def setOnline(self, pInfo):
        ...

class SortieCandidatesDP(CandidatesDataProvider):
    def _makePlayerVO(self, pInfo, user, colorGetter, isPlayerSpeaking):
        ...

class ClanBattleCandidatesDP(CandidatesDataProvider):
    def _makePlayerVO(self, pInfo, user, colorGetter, isPlayerSpeaking):
        ...

class SortieCandidatesLegionariesDP(SortieCandidatesDP):
    __legionariesCount: Any
    def __init__(self):
        ...
    @property
    def legionariesCount(self):
        ...
    def buildList(self, candidates):
        ...
    def __addAdditionalBlocks(self, playersCount, legionariesCount):
        ...

class StaticFormationCandidatesDP(CandidatesDataProvider):
    def buildList(self, candidates):
        ...
    def _makePlayerVO(self, pInfo, user, colorGetter, isPlayerSpeaking):
        ...
    def __addAdditionalBlocks(self, playersCount, legionariesCount):
        ...

class ManualSearchDataProvider(BaseRallyListDataProvider):
    lobbyContext: Any
    usersStorage: Any
    _selectedIdx: Any
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def getVO(self, unitIndex=None):
        ...
    def buildList(self, selectedID, result):
        ...
    def updateListItem(self, userDBID):
        ...
    def updateList(self, selectedID, result):
        ...
