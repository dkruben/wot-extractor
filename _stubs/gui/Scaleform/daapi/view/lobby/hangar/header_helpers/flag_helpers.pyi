# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/flag_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
FLAG_BY_QUEST_TYPE: dict

class LabelState(object):
    ACTIVE = 'active'
    EMPTY = 'empty'
    INACTIVE = 'inactive'
    ALL_DONE = 'all_done'

def getActiveQuestLabel(total, completed):
    ...
def headerQuestFormatterVo(enable, icon, label, questType, flag=None, flagDisabled=None, stateIcon=None, questID=None, isReward=False, tooltip='', isTooltipSpecial=False, isTooltipWulf=False):
    ...
def wrapQuestGroup(groupID, icon, quests, isRightSide=False):
    ...
