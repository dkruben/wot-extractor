# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSAccountComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import AccountCommands as AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent as BaseAccountExtensionComponent
from PlayerEvents import g_playerEvents as events
from helpers import dependency as dependency
from last_stand.gui.ls_account_settings import clearNewStatusUnlockLevel as clearNewStatusUnlockLevel
from last_stand.gui.ls_gui_constants import DIFFICULTY_TOKEN_TO_LEVEL as DIFFICULTY_TOKEN_TO_LEVEL
from last_stand_common import last_stand_constants as last_stand_constants
from last_stand_common.ls_account_commands import CMD_LS_UNLOCK_TOKEN as CMD_LS_UNLOCK_TOKEN, CMD_LS_LOCK_TOKEN as CMD_LS_LOCK_TOKEN, CMD_LS_ARTEFACT_OPEN as CMD_LS_ARTEFACT_OPEN, CMD_LS_BUY_BUNDLE as CMD_LS_BUY_BUNDLE
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class LSInfoSessionCache(object):
    DATA_KEY = last_stand_constants.LS_INFO_PDATA_KEY
    cache = None
    @classmethod
    def vehicleDailyCompleted(cls):
        ...
    @classmethod
    def curDay(cls):
        ...
    @classmethod
    def init(cls):
        ...
    @classmethod
    def _onClientSynchronize(cls, isFullSync, diff):
        ...
    @classmethod
    def __deleteInstance(cls):
        ...

class LSAccountComponent(BaseAccountExtensionComponent):
    def __init__(self):
        ...
    @property
    def vehicleDailyCompleted(self):
        ...
    @property
    def curDay(self):
        ...
    def enqueueBattle(self, queueType, vehInvID):
        ...
    def dequeueBattle(self, queueType):
        ...
    def unlockToken(self, token, tokenCount=1, callback=None):
        ...
    def lockToken(self, token, callback=None):
        ...
    def openArtefact(self, artefactID, isSkipQuest, callback=None):
        ...
    def buyBundle(self, bundleID, count=1, callback=None):
        ...
