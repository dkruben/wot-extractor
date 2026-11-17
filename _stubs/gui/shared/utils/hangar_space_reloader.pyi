# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/hangar_space_reloader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpaceReloader as IHangarSpaceReloader
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.Scaleform.Waiting import Waiting as Waiting
_logger: Any

class ErrorFlags(object):
    NONE = 0
    INVALID_NAME = 1
    ALREADY_PROCESSING_RELOAD = 2
    WAITING_FOR_SPACE = 4
    SPACE_PATH_NOT_INITED = 8
    DUPLICATE_REQUEST = 16
    HANGAR_NOT_READY = 32

class HangarSpaceReloader(IHangarSpaceReloader):
    hangarSpace: Any
    __loadingSpacePath: Any
    __waitingMessage: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def changeHangarSpace(self, spaceName, visibilityMask, waitingMessage=None, backgroundImage=None, actionChange=False, force=False):
        ...
    @staticmethod
    def buildHangarSpacePath(spaceId):
        ...
    @property
    def hangarSpacePath(self):
        ...
    def __onHangarSpaceLoaded(self):
        ...
    def __onSpaceDestroy(self, inited):
        ...
    def __hideWaiting(self):
        ...
