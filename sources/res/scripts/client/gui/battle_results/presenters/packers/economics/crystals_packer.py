# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/crystals_packer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/economics/crystals_packer.py
from gui.impl.gen import R
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker, CurrencyGroup
from gui.battle_results.presenters.packers.economics.crystals_records import ORIGINAL_CRYSTALS, EVENT_CRYSTALS, AUTO_EQUIP_CRYSTALS, TOTAL_CRYSTALS
_STR_PATH = R.strings.battle_results.details.calculations

class CrystalsPacker(CurrencyPacker):
    _EARNED = CurrencyGroup(label=_STR_PATH.title.base, records=(ORIGINAL_CRYSTALS, EVENT_CRYSTALS))
    _EXPENSES = CurrencyGroup(label=_STR_PATH.title.expenses, records=(AUTO_EQUIP_CRYSTALS,))
    _TOTAL = CurrencyGroup(label=None, records=(TOTAL_CRYSTALS,))

    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        return (((lambda _: battleResults.reusable.personal.getCrystalDetailsRecords()),), zip)
