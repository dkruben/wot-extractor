# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/dev/gifter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process
from gui.gift_system.constants import GifterResponseState as GifterResponseState
from gui.gift_system.hubs.base.gifter import GiftEventBaseGifter as GiftEventBaseGifter
from gui.gift_system.hubs.dev import IDevMessagesPusher as IDevMessagesPusher
from gui.shared.formatters import text_styles as text_styles
_logger: Any

class GiftEventDevGifter(GiftEventBaseGifter, IDevMessagesPusher):
    __slots__: tuple
    def __repr__(self):
        ...
    # decorador original: @adisp_process
    def sendGift(self, entitlementCode, receiverID, metaInfo, callback=None):
        ...
    @classmethod
    def _formatMessage(cls, message):
        ...
