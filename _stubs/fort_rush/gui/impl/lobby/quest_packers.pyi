# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/quest_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.gui.impl.lobby.bonus_packers import getFortRushMissionBonusPacker as getFortRushMissionBonusPacker
from fort_rush.gui.impl.lobby.bonus_packers import FortRushTokenBonusUIPacker as FortRushTokenBonusUIPacker
from gui.shared.missions.packers.events import DailyQuestUIDataPacker as DailyQuestUIDataPacker, findFirstConditionModel as findFirstConditionModel

class FortRushDailyQuestUIDataPacker(DailyQuestUIDataPacker):
    def _getBonusPacker(self):
        ...
    def _resolveQuestIcon(self, model):
        ...
