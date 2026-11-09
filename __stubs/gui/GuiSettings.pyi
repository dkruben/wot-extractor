# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/GuiSettings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import nations as nations
import constants as constants
import resource_helper as resource_helper
from helpers import getClientLanguage as getClientLanguage, time_utils as time_utils
from gui import macroses as macroses
from soft_exception import SoftException as SoftException
_logger: Any
GUI_SETTINGS_FILE_PATH = 'gui/gui_settings.xml'
VIDEO_SETTINGS_FILE_PATH = 'gui/video_settings.xml'
LoginRssFeedProps: Any
BrowserProps: Any
PostBattleExchangeProps: Any
EasterEggProps: Any
_MacrosValue: Any
_SETTING_CONVERTERS: dict
_DEFAULT_SETTINGS: dict

class EULAProps(object):
    __slots__: tuple
    __full: Any
    __url: Any
    def __init__(self, full=None, url=''):
        ...
    @property
    def full(self):
        ...
    @property
    def url(self):
        ...

class GuiSettings(object):
    __settings: Any
    def __init__(self):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def __contains__(self, item):
        ...
    @property
    def isShowLanguageBar(self):
        ...
    def isEmpty(self, name):
        ...
    def isGuiEnabled(self):
        ...
    def lookup(self, name):
        ...
    def checkAndReplaceWebShopMacros(self, url):
        ...
    def checkAndReplaceWebBridgeMacros(self, url):
        ...
    def __checkAndReplaceMacros(self, rootUrlName, url):
        ...
    def __applyMacros(self, value):
        ...

def _readMacros(xmlCtx, section, valueName='value', nameFromSection=True):
    ...
def _readItemMacros(xmlCtx, section, keys=None):
    ...
def _convertVector4ToTuple(_, item):
    ...
def _convertToNamedTuple(settings, item):
    ...
def _convertEULASetting(_, item):
    ...
