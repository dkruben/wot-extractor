# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/currency_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from soft_exception import SoftException as SoftException
from shared_utils import first as first
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.gen import R as R
from gui.battle_results.presenters.packers.interfaces import ICurrencyPacker as ICurrencyPacker
from gui.impl.gen.view_models.views.lobby.battle_results.currency_record_model import CurrencyRecordModel as CurrencyRecordModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_details_model import CurrencyRecordsItemDetailsModel as CurrencyRecordsItemDetailsModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel as CurrencyRecordsItemModel
from typing import List as List, Any as Any, Tuple as Tuple
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.pbs_helpers.economics import FinancialRecordValues as FinancialRecordValues
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_model import CurrencyRecordsModel as CurrencyRecordsModel
_logger: _Any
CurrencyRecord: _Any
CurrencyGroup: _Any

class CurrencyPacker(ICurrencyPacker):
    _EARNED = None
    _EXPENSES = None
    _TOTAL = None
    _ADDITIONAL = None
    _EXTRACTORS: dict
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls, battleResults):
        ...
    @classmethod
    def _fillRecords(cls, recordsModel, battleResults, records, recordsConfigs):
        ...
    @classmethod
    def _createRecordModel(cls, battleResults, records, configs):
        ...
    @classmethod
    def _packGroup(cls, model, records, battleResults, recordsConfigsExtractor, sourceConfig):
        ...
    @staticmethod
    def __packValueModel(valueModel, recordConfig, value):
        ...
    @staticmethod
    def _getValues(battleResults, records, configs):
        ...

class DetailedCurrencyPacker(ICurrencyPacker):
    _EARNED = None
    _EXPENSES = None
    _TOTAL = None
    _EXTRACTORS: dict
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls):
        ...
    @classmethod
    def _packGroup(cls, model, records, battleResults, recordsConfigsExtractor, sourceConfig):
        ...
    @classmethod
    def _fillRecords(cls, recordsModel, battleResults, records, recordsConfigs):
        ...
    @classmethod
    def _createRecordModel(cls, battleResults, record, config):
        ...
    @staticmethod
    def _getValues(battleResults, record, config):
        ...
    @staticmethod
    def _packAdditionalValues(model, battleResults, config):
        ...
