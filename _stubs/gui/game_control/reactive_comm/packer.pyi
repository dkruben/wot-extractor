# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/reactive_comm/packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import cbor as cbor
from gui.game_control.reactive_comm.constants import SubscriptionServerStatus as SubscriptionServerStatus
from gui.game_control.reactive_comm.constants import SubscriptionCommand as SubscriptionCommand

class ServiceMessage(object):
    __slots__: tuple
    cid: Any
    channel: Any
    status: Any
    seqid: Any
    data: Any
    def __init__(self, cid=None, channel='', status='', seqid=None, data=None, **_):
        ...
    @property
    def isStatusReceived(self):
        ...
    @property
    def isMessageReceived(self):
        ...
    @property
    def isValid(self):
        ...

def packCommand(channel, command):
    ...
def unpackMessage(payload):
    ...
