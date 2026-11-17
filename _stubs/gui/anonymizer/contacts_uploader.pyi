# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/anonymizer/contacts_uploader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from constants import BattleUserActions as BattleUserActions, REQUEST_COOLDOWN as REQUEST_COOLDOWN
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto import proto_getter as proto_getter
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, CLIENT_ACTION_ID as CLIENT_ACTION_ID
_logger: Any

class ContactsUploader(object):
    __slots__: tuple
    __callbackID: Any
    __arenaUniqueID: Any
    __idToActions: Any
    __idToNames: Any
    def __init__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    @property
    def isProcessing(self):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self, arenaUniqueID, contactsBlob):
        ...
    def stop(self):
        ...
    def _onShadowActionFailed(self, dbID, actionID, error):
        ...
    def _onShadowActionDone(self, dbID, actionID):
        ...
    def _flushArenaRelations(self):
        ...
    def __onFlushResponse(self, _, resultID, __):
        ...
    def __tryUploadContact(self, dbID=None, leftActions=None):
        ...
