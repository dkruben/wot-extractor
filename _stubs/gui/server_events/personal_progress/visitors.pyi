# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/visitors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from personal_missions_constants import PROGRESS_TEMPLATE as PROGRESS_TEMPLATE
from gui.server_events.personal_progress import metrics_wrappers as metrics_wrappers
WrapperInfo: Any

class WrappersVisitor(object):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class BinaryProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class ValueLikeBinaryProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class ValueProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class LobbyValueProgressVisitor(ValueProgressVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...

class CounterProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class LimiterProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...

class TimerProgressVisitor(WrappersVisitor):
    @classmethod
    def isSuitableForProgress(cls, progress):
        ...
    @classmethod
    def getWrappers(cls):
        ...
