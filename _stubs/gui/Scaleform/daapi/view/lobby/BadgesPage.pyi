# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/BadgesPage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from helpers import dependency as dependency
from account_helpers.AccountSettings import AccountSettings as AccountSettings, LAST_BADGES_VISIT as LAST_BADGES_VISIT, LAST_SELECTED_SUFFIX_BADGE_ID as LAST_SELECTED_SUFFIX_BADGE_ID
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IBadgesController as IBadgesController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.Scaleform.daapi.view.meta.BadgesPageMeta import BadgesPageMeta as BadgesPageMeta
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.shared.formatters import text_styles as text_styles
from gui.Scaleform.locale.BADGE import BADGE as BADGE
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.badges.BadgesCollector import BadgesCollector as BadgesCollector
from gui.badges.badges_vos import makeBadgeVO as makeBadgeVO, makeSuffixBadgeVO as makeSuffixBadgeVO

class BadgesPage(BadgesPageMeta):
    itemsCache: Any
    lobbyContext: Any
    settingsCore: Any
    badgesController: Any
    __prefixBadgeID: Any
    __suffixBadgeID: Any
    __selectedItemIdx: Any
    __badgesCollector: Any
    __backViewName: Any
    __tutorStorage: Any
    def __init__(self, ctx=None, *args, **kwargs):
        ...
    def onBackClick(self):
        ...
    def onSelectBadge(self, badgeID):
        ...
    def onDeselectBadge(self):
        ...
    def onSelectSuffixBadge(self, badgeID):
        ...
    def onDeselectSuffixBadge(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __sentSuffixBadgesVO(self):
        ...
    def __deselectNotSelectedBadge(self, badge):
        ...
    def __updateBadges(self):
        ...
    def __onWotPlusUpdate(self, *_):
        ...
    def __selectBadges(self):
        ...
    def __checkNewSuffixBadges(self):
        ...
