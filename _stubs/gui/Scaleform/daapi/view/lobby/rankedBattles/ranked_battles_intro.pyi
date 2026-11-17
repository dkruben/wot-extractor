# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_intro.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior as GuiSettingsBehavior
from frameworks.wulf import WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_MAIN_PAGE_SOUND_SPACE as RANKED_MAIN_PAGE_SOUND_SPACE
from gui.ranked_battles.ranked_helpers import getRankedBattlesIntroPageUrl as getRankedBattlesIntroPageUrl
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.RankedBattlesIntroMeta import RankedBattlesIntroMeta as RankedBattlesIntroMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.shared import event_dispatcher as event_dispatcher, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.shared.utils.functions import getUniqueViewName as getUniqueViewName
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from web.web_client_api import webApiCollection as webApiCollection, ui as ui_web_api, sound as sound_web_api
BLOCKS_COUNT = 3

class RankedBattlesIntro(LobbySubView, RankedBattlesIntroMeta):
    _COMMON_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE
    __rankedController: Any
    __settingsCore: Any
    __state: Any
    def onAcceptClick(self):
        ...
    def onClose(self):
        ...
    def onDetailedClick(self):
        ...
    def onPlayVideoClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self, _=None):
        ...
    def __updateTimer(self):
        ...
    def __showVideo(self):
        ...
    def __getShowStateFlags(self):
        ...
    def __setShowStateFlags(self):
        ...
