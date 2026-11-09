# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/credits_packer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/economics/credits_packer.py
from gui.battle_results.presenters.packers.economics import credits_records
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker, CurrencyGroup
from gui.battle_results.presenters.packers.economics.common_records import AOGAS_FACTOR, AFK_VIOLATION, DESERTER_VIOLATION, SUICIDE_VIOLATION
from gui.battle_results.presenters.packers.economics.gold_records import GOLD_PIGGY_BANK, GOLD_EVENT_PAYMENTS
from gui.battle_results.pbs_helpers.economics import getDirectMoneyRecords
from gui.impl.gen import R
_STR_PATH = R.strings.battle_results.details.calculations

class CreditsPacker(CurrencyPacker):
    _EARNED = CurrencyGroup(label=None, records=(
     credits_records.BASE_EARNED_CREDITS,
     credits_records.SQUAD_BONUS_CREDITS,
     credits_records.ACHIEVEMENT_CREDITS,
     credits_records.BOOSTERS_CREDITS,
     credits_records.BATTLE_PAYMENTS_CREDITS,
     credits_records.EVENT_PAYMENTS_CREDITS,
     credits_records.REFERRAL_BONUS_CREDITS,
     credits_records.WOT_PLUS_CURRENT_ONLY_BONUS_CREDITS,
     DESERTER_VIOLATION,
     SUICIDE_VIOLATION,
     AFK_VIOLATION,
     credits_records.FRIENDLY_FIRE_PENALTY_CREDITS,
     credits_records.FRIENDLY_FIRE_COMPENSATION_CREDITS,
     AOGAS_FACTOR))
    _EXPENSES = CurrencyGroup(label=_STR_PATH.title.expenses, records=(
     credits_records.AUTO_REPAIR_CREDITS,
     credits_records.AUTO_LOAD_CREDITS,
     credits_records.AUTO_EQUIP_CREDITS))
    _TOTAL = CurrencyGroup(label=None, records=(credits_records.TOTAL_CREDITS,))
    _ADDITIONAL = CurrencyGroup(label=None, records=(
     credits_records.PIGGY_BANK_CREDITS,
     GOLD_PIGGY_BANK,
     GOLD_EVENT_PAYMENTS))

    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        return ((getDirectMoneyRecords,), zip)
