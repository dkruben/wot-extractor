# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/view_helpers/emblems.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from enum import IntEnum as IntEnum
from gui.clans import settings as clan_settings
from gui.shared.image_helper import ImageHelper as ImageHelper, readLocalImage as readLocalImage
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class EmblemSize(IntEnum):
    SIZE_16 = 16
    SIZE_32 = 32
    SIZE_64 = 64
    SIZE_128 = 128
    SIZE_256 = 256

class ClanEmblemsHelper(ImageHelper):
    __default: dict
    def requestClanEmblem16x16(self, clanDbID):
        ...
    def requestClanEmblem32x32(self, clanDbID):
        ...
    def requestClanEmblem64x64(self, clanDbID):
        ...
    def requestClanEmblem128x128(self, clanDbID):
        ...
    def requestClanEmblem256x256(self, clanDbID):
        ...
    def onClanEmblem16x16Received(self, clanDbID, emblem):
        ...
    def onClanEmblem32x32Received(self, clanDbID, emblem):
        ...
    def onClanEmblem64x64Received(self, clanDbID, emblem):
        ...
    def onClanEmblem128x128Received(self, clanDbID, emblem):
        ...
    def onClanEmblem256x256Received(self, clanDbID, emblem):
        ...
    def getDefaultClanEmblem(self, size):
        ...
    def __makeRequest(self, clanDbID, size, handler):
        ...

def getClanEmblemURL(clanDbID, size):
    ...
