# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/SwitchPeripheryWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from adisp import adisp_process as adisp_process
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import DialogsInterface as DialogsInterface
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES as BUTTON_LINKAGES
from gui.Scaleform.daapi.view.meta.SwitchPeripheryWindowMeta import SwitchPeripheryWindowMeta as SwitchPeripheryWindowMeta
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider as ServersDataProvider
from gui.Scaleform.genConsts.TEXT_ALIGN import TEXT_ALIGN as TEXT_ALIGN
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, REQUEST_RATE as REQUEST_RATE
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IReloginController as IReloginController

class SwitchPeripheryWindow(SwitchPeripheryWindowMeta, Notifiable):
    _BTN_WIDTH = 140
    _CLOSE_BTN_ACTION = 'closeAction'
    _SWITCH_BTN_ACTION = 'switchAction'
    relogin: Any
    connectionMgr: Any
    __ctx: Any
    _serversDP: Any
    def __init__(self, ctx):
        ...
    def onBtnClick(self, action):
        ...
    def requestForChange(self, peripheryId):
        ...
    def onWindowClose(self):
        ...
    def onDropDownOpened(self, opened):
        ...
    def _updateServersList(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    # decorador original: @adisp_process
    def __relogin(self, peripheryID):
        ...
    def __onServersUpdate(self, *args):
        ...
