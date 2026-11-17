# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/EULADispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.doc_loaders.EULAVersionLoader import EULAVersionLoader as EULAVersionLoader
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from helpers import getClientLanguage as getClientLanguage
from gui import makeHtmlString as makeHtmlString, GUI_SETTINGS as GUI_SETTINGS
from gui.shared.events import CloseWindowEvent as CloseWindowEvent, LoadViewEvent as LoadViewEvent
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from Event import Event as Event
from adisp import adisp_async as adisp_async
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import ISteamCompletionController as ISteamCompletionController, IDemoAccCompletionController as IDemoAccCompletionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
VERSION_TAG = 'showLicense'
EULA_TEMPLATES_FILE_PATH = 'gui/EULA_templates.xml'
EULA_FILE_PATH = 'text/EULA.xml'

class EULADispatcher(EventSystemEntity):
    onEULAClosed: Any
    settingsCore: Any
    lobbyContext: Any
    _demoAccController: Any
    _steamRegistrationCtrl: Any
    serverVersion: Any
    isShow: Any
    EULACallback: Any
    EULAVersion: Any
    __showLicense: Any
    __eulaText: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def __onEulaClosed(self, event):
        ...
    # decorador original: @adisp_async
    def processLicense(self, callback=None):
        ...
    def __saveVersionFile(self):
        ...
    def __readEULAShort(self):
        ...
    def __readEULAFull(self):
        ...
    def fini(self):
        ...

class _TagTemplate(object):
    _template: Any
    def __init__(self, template):
        ...
    def execute(self, section, processor, result):
        ...

class _LinkTemplate(_TagTemplate):
    def execute(self, section, processor, result):
        ...

class _TitleTemplate(_TagTemplate):
    def execute(self, section, processor, result):
        ...

class _ContentTemplate(_TagTemplate):
    def execute(self, section, processor, result):
        ...

class _ChapterTemplate(object):
    __title: Any
    __content: Any
    def __init__(self, titleTemplate, contentTemplate):
        ...
    def execute(self, section, processor, result):
        ...

class _LicenseXMLProcessor(object):
    __templates: dict
    def __init__(self):
        ...
    def __loadTemplates(self):
        ...
    def execute(self, section, processor=None, result=None):
        ...
