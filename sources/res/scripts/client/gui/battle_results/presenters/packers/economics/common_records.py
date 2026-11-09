# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/common_records.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/economics/common_records.py
from gui.battle_results.pbs_helpers.economics import hasAogasFine
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyRecord
from gui.battle_results.presenters.packers.economics.value_extractors import getDeserterViolation, getAfkViolation, getSuicideViolation, getDecreasingBaseAccountFactor, getDecreasingPremiumAccountFactor
from gui.battle_results.settings import CurrenciesConstants
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_value_model import ValueModifiers
_STR_PATH = R.strings.battle_results.details.calculations
AOGAS_FACTOR = CurrencyRecord(recordNames=('aogasFactor10', ), subtractRecords=(), baseAccountValueExtractor=getDecreasingBaseAccountFactor, premiumAccountValueExtractor=getDecreasingPremiumAccountFactor, detailsValuesExtractors=(
 hasAogasFine,), capsToBeChecked=None, paramName=CurrencyRecordsItemModel.AOGAS_FACTOR, label=_STR_PATH.aogasFactor, modifiers=(
 ValueModifiers.MUL, ValueModifiers.SHOW_NEGATIVE_IMPACT), showZeroValue=True, currencyType=CurrenciesConstants.COMMON_CURRENCY)
DESERTER_VIOLATION = CurrencyRecord(recordNames=(), subtractRecords=(), baseAccountValueExtractor=getDeserterViolation, premiumAccountValueExtractor=getDeserterViolation, detailsValuesExtractors=(), capsToBeChecked=None, paramName=CurrencyRecordsItemModel.DESERTER_VIOLATION, label=_STR_PATH.fairPlayViolation.deserter, modifiers=(
 ValueModifiers.PROCENT,), showZeroValue=False, currencyType=CurrenciesConstants.COMMON_CURRENCY)
AFK_VIOLATION = CurrencyRecord(recordNames=(), subtractRecords=(), baseAccountValueExtractor=getAfkViolation, premiumAccountValueExtractor=getAfkViolation, detailsValuesExtractors=(), capsToBeChecked=None, paramName=CurrencyRecordsItemModel.AFK_VIOLATION, label=_STR_PATH.fairPlayViolation.afk, modifiers=(
 ValueModifiers.PROCENT,), showZeroValue=False, currencyType=CurrenciesConstants.COMMON_CURRENCY)
SUICIDE_VIOLATION = CurrencyRecord(recordNames=(), subtractRecords=(), baseAccountValueExtractor=getSuicideViolation, premiumAccountValueExtractor=getSuicideViolation, detailsValuesExtractors=(), capsToBeChecked=None, paramName=CurrencyRecordsItemModel.SUICIDE_VIOLATION, label=_STR_PATH.fairPlayViolation.suicide, modifiers=(
 ValueModifiers.PROCENT,), showZeroValue=False, currencyType=CurrenciesConstants.COMMON_CURRENCY)
