# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/mapbox/mapbox_bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from shared_utils import first as first
from frameworks.wulf import Array as Array

class _MapboxBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...

def getMapboxBonusPacker():
    ...
def packMapboxRewardModelAndTooltip(rewardsList, bonusList, packer, numBattles, tooltipsList=None):
    ...
