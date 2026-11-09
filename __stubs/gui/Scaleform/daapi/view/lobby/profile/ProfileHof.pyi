# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileHof.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency, i18n as i18n
from gui.Scaleform import MENU as MENU
from gui.shared.formatters import icons as icons
from skeletons.gui.web import IWebController as IWebController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofAchievementsRatingUrl as getHofAchievementsRatingUrl, getHofVehiclesRatingUrl as getHofVehiclesRatingUrl, isHofButtonNew as isHofButtonNew, setHofButtonOld as setHofButtonOld, getHofDisabledKeys as getHofDisabledKeys, onServerSettingsChange as onServerSettingsChange
from gui.Scaleform.daapi.view.lobby.hof.web_handlers import createHofWebHandlers as createHofWebHandlers
from gui.Scaleform.daapi.view.meta.ProfileHofMeta import ProfileHofMeta as ProfileHofMeta
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS as PROFILE_CONSTANTS
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class ProfileHof(ProfileHofMeta):
    _eventsCache: Any
    _clansController: Any
    _errorsStatusMap: dict
    _requestRetriesCount = 3
    _retryDelay = 0.5
    _bgPath = '../maps/icons/hof/hof_back_landing.png'
    _buttonsWithCounter: tuple
    __status: Any
    __retriesCount: Any
    __isMaintenance: Any
    __viewDisposed: Any
    __requestProcessing: Any
    __retryCallback: Any
    def __init__(self, *args):
        ...
    def showAchievementsRating(self):
        ...
    def showVehiclesRating(self):
        ...
    # decorador original: @adisp_process
    def changeStatus(self):
        ...
    def onSectionActivated(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getCountersList(self):
        ...
    def __getRatingStatus(self):
        ...
    # decorador original: @adisp_process
    def __makeRequest(self, requestFunc, successStatus, errorCallback):
        ...
    def __refreshRequest(self):
        ...
    def __openHofBrowserView(self, url):
        ...
    def __onServerSettingChanged(self, diff):
        ...
