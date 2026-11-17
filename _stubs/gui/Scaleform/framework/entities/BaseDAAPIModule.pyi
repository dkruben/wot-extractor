# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/entities/BaseDAAPIModule.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from soft_exception import SoftException as SoftException
from gui.Scaleform.framework.entities.abstract.BaseDAAPIModuleMeta import BaseDAAPIModuleMeta as BaseDAAPIModuleMeta
_logger: Any

class BaseDAAPIModule(BaseDAAPIModuleMeta):
    __isScriptSet: Any
    __isPyReloading: Any
    __app: Any
    def __init__(self):
        ...
    @property
    def app(self):
        ...
    def setEnvironment(self, app):
        ...
    def setPyReloading(self, flag):
        ...
    def _getPyReloading(self):
        ...
    def setFlashObject(self, movieClip, autoPopulate=True, setScript=True):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def _printOverrideError(self, methodName):
        ...
