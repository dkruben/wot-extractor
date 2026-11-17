# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/resources/local/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.collection import loggers as loggers
from gui.impl import backport as backport
from gui.impl.gen import R as R
from typing import Dict as Dict, List as List
_logger: Any

class CollectionsLocalCacheMgr(object):
    __IMG = R.images.gui.maps.icons.collections.fakeCdn.images
    def startSync(self, *args, **kwargs):
        ...
    def stopSync(self, *args, **kwargs):
        ...
    def getImagesPaths(self, imagesIDs, callback=None):
        ...
    def __packImages(self, imagesIDs):
        ...
