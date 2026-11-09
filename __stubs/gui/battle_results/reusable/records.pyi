# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/records.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from ValueReplay import ValueReplay as ValueReplay
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.system_factory import collectReplayRecordMap as collectReplayRecordMap
_SUPPORTED_OPS: dict

class ResultRecord(object):
    __slots__: tuple
    def getRecord(self, *args):
        ...
    def findRecord(self, criteria):
        ...
    def getFactor(self, *args):
        ...

class RawRecords(ResultRecord):
    __slots__: tuple
    _records: Any
    def __init__(self, records):
        ...
    def getRecord(self, *names):
        ...

class ReplayRecord(ResultRecord):
    __slots__: tuple
    _name: Any
    _value: Any
    _diff: Any
    def __init__(self, name, value, diff):
        ...
    def getName(self):
        ...
    def getRecord(self):
        ...
    def _getFactor(self):
        ...

class SubReplayRecord(ReplayRecord):
    __slots__: tuple
    def getRecord(self):
        ...

class FactorReplayRecord(ReplayRecord):
    __slots__: tuple
    def getRecord(self):
        ...
    def getFactor(self):
        ...

class CoefficientReplayRecord(ReplayRecord):
    __slots__: tuple
    def getRecord(self):
        ...

class ReplayRecords(ResultRecord):
    __slots__: tuple
    _records: Any
    def __init__(self, replay, *last):
        ...
    def getRecord(self, *names):
        ...
    def findRecord(self, criteria):
        ...
    def getFactor(self, name):
        ...
    def _getRecord(self, name):
        ...
    def _addRecord(self, op, name, value, diff):
        ...

class RecordsIterator(ResultRecord):
    __slots__: tuple
    _seq: Any
    _indexes: Any
    def __init__(self, seq=None):
        ...
    def __iter__(self):
        ...
    def next(self):
        ...
    def addRecords(self, record):
        ...
    def getRecord(self, *names):
        ...
    def findRecord(self, criteria):
        ...
    def getFactor(self, name):
        ...
    def _rebuild(self):
        ...
    def _sum(self, method, *names):
        ...

def convertFactorToPercent(factor):
    ...
def makeReplayValueRound(value):
    ...
