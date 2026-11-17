# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/doc_loaders/settings_set.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from messenger.doc_loaders import _xml_helpers as _xml_helpers
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
_LOBBY_SET_READERS: dict
_LOBBY_ITEM_READERS: dict
_ReceiverInBattle: Any
_BATTLE_SET_READERS: dict
_BATTLE_ITEM_READERS: dict
_SETTINGS_LOADERS: dict

def _readSet(xmlCtx, section, _, readers):
    ...
def _readSettings(xmlCtx, section, settings, setReaders, itemReaders):
    ...
def _readServiceChannel(xmlCtx, section, settings):
    ...
def _readLobbyColors(xmlCtx, section, settings):
    ...
def _readBattleMessageLifeCycle(xmlCtx, section, settings):
    ...
def _readReceiverValue(xmlCtx, section, settings=None):
    ...
def _readReceivers(xmlCtx, section, settings):
    ...
def load(xmlCtx, section, messengerSettings):
    ...
