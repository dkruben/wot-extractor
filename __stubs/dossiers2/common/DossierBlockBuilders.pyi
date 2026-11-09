# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dossiers2/common/DossierBlockBuilders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import List as List, Union as Union
from dossiers2.common.DossierBlocks import *
from dossiers2.custom.records import RECORDS as RECORDS, RECORD_INDICES as RECORD_INDICES, BIT_STORAGES as BIT_STORAGES
from serialization.serializable_component import SerializableComponentChildType as SerializableComponentChildType
from dossiers2.common.DossierDescr import DossierDescr as DossierDescr
EVENT_HANDLERS_TYPE: Any
_SUPPORTED_FORMATS: Any
TYPE_BLOCK_BUILDER: Any

class IBlockBuilderWithRecordsLayout(object):
    name = None
    recordsLayout: list
    def build(self, dossierDescr, compDescr=''):
        ...

class StaticSizeBlockBuilder(IBlockBuilderWithRecordsLayout):
    name: Any
    recordsLayout: Any
    __eventsHandlers: Any
    __popUpRecords: Any
    __logRecords: Any
    __layout: Any
    __packing: Any
    __format: Any
    __initialData: Any
    __blockSize: Any
    def __init__(self, name, recordsLayout, eventsHandlers, popUpRecords, logRecords=None):
        ...
    def build(self, dossierDescr, compDescr=''):
        ...

class DictBlockBuilder(object):
    name: Any
    __keyFormat: Any
    __valueFormat: Any
    __eventsHandlers: Any
    __popUpRecords: Any
    __logRecords: Any
    def __init__(self, name, keyFormat, valueFormat, eventsHandlers, popUpRecords=None, logRecords=None):
        ...
    def build(self, dossierDescr, compDescr=''):
        ...

class ListBlockBuilder(object):
    name: Any
    __itemFormat: Any
    __eventsHandlers: Any
    def __init__(self, name, itemFormat, eventsHandlers):
        ...
    def build(self, dossierDescr, compDescr=''):
        ...

class BinarySetDossierBlockBuilder(IBlockBuilderWithRecordsLayout):
    name: Any
    recordsLayout: Any
    __valueToPosition: Any
    __eventHandlers: Any
    __popUpRecords: Any
    __logRecords: Any
    def __init__(self, name, valueNames, eventHandlers, popUpRecords, logRecords=None):
        ...
    def build(self, dossierDescr, compDescr=''):
        ...
    def __buildValueToPosition(self, valueNames):
        ...

class SerializableBlockBuilder(IBlockBuilderWithRecordsLayout):
    name: Any
    componentClass: Any
    parserCallback: Any
    recordsLayout: Any
    __eventHandlers: Any
    __popUpRecords: Any
    __logRecords: Any
    def __init__(self, name, componentClass, parserCallback, eventHandlers, popUpRecords, logRecords):
        ...
    def build(self, dossierDescr, compDescr=''):
        ...
