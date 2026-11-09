# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.clans import formatters as clans_fmts
from gui.shared import event_dispatcher as event_dispatcher, utils as utils
from shared_utils import CONST_CONTAINER as CONST_CONTAINER

class CLAN_CM_OPTIONS(CONST_CONTAINER):
    CLAN_PROFILE = 'clanProfile'
    COPY_TO_CB = 'copyToClipboard'

class BaseClanCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    __clanDbID: Any
    __clanName: Any
    __clanAbbrev: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def showClanProfile(self):
        ...
    def copyToClipboard(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
