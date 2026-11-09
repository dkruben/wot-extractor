# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import viewvalues as viewvalues
from past.builtins import unicode as unicode
import nations as nations
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, HAS_DEV_RESOURCES as HAS_DEV_RESOURCES, ARENA_PERIOD as ARENA_PERIOD
from gui import promo as promo
from gui.GuiSettings import GuiSettings as _GuiSettings
from helpers.html.templates import XMLCollection as XMLCollection
from gui.active_vehicle import ActiveVehicleSeasonType as ActiveVehicleSeasonType
_logger: Any
g_guiResetters: Any
g_repeatKeyHandlers: Any
g_keyEventHandlers: Any
g_mouseEventHandlers: Any
g_tankActiveCamouflage: Any
GUI_SETTINGS: Any
DEPTH_OF_BotsMenu = 0.05
DEPTH_OF_Battle = 0.1
DEPTH_OF_Statistic = 0.1
DEPTH_OF_PlayerBonusesPanel = 0.2
DEPTH_OF_Aim = 0.6
DEPTH_OF_GunMarker = 0.56
DEPTH_OF_VehicleMarker = 0.9
TANKMEN_ROLES_ORDER_DICT: dict
NONE_NATION_NAME = 'none'
ALL_NATION_INDEX = -1
GUI_NATIONS: Any
new_order_list: list
GUI_NATIONS_ORDER_INDEX: dict
GUI_NATIONS_ORDER_INDEX_REVERSED: dict
GUI_NATIONS_ORDER_INDICES: dict
HTML_TEMPLATES_DIR_PATH = 'gui/{0:>s}.xml'
HTML_TEMPLATES_PATH_DELIMITER = ':'
g_htmlTemplates: Any

class HtmlTemplatesCache(defaultdict):
    def __missing__(self, key):
        ...

class GUI_CTRL_MODE_FLAG(object):
    CURSOR_DETACHED = 0
    CURSOR_ATTACHED = 1
    CURSOR_VISIBLE = 2
    MOVING_DISABLED = 4
    AIMING_ENABLED = 8
    GUI_ENABLED: Any

def onRepeatKeyEvent(event):
    ...
def _nationSortKeyByName(nation):
    ...
def nationSortKeyByIndex(index):
    ...
def getNationIndex(nationOrderIndex):
    ...
def _reload_ht():
    ...
def makeHtmlString(path, key, ctx=None, **kwargs):
    ...
def getGuiServicesConfig(manager):
    ...
