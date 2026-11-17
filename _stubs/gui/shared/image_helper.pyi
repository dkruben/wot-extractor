# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/image_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import ResMgr as ResMgr
from adisp import adisp_async as adisp_async
from constants import GF_RES_PROTOCOL as GF_RES_PROTOCOL
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from gui.shared.utils import mapTextureToTheMemory as mapTextureToTheMemory, getImageSize as getImageSize, removeTextureFromMemory as removeTextureFromMemory

class ImageHelper(object):
    @staticmethod
    def getMemoryTexturePath(image, temp=True):
        ...
    @staticmethod
    def removeTextureFromMemory(textureID):
        ...
    @staticmethod
    def requestImageByUrl(url, callback, size=None, defaultGetter=None):
        ...

class ImagesFetchCoordinator(object):
    __texturesCache: Any
    __isDying: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    # decorador original: @adisp_async
    def fetchImageByUrl(self, url, oneUse=True, callback=None):
        ...
    def clearMappedImageByUrl(self, url):
        ...
    def clearAllMappedImages(self):
        ...
    def fini(self):
        ...

def readLocalImage(path):
    ...
def getTextureLinkByID(imageID, prefix=...):
    ...
