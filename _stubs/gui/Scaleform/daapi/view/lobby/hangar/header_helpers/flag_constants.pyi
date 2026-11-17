# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/flag_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.personal_mission_flags import PersonalMissionsFlag as PersonalMissionsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import RankedQuestsFlag as RankedQuestsFlag, ElenQuestsFlag as ElenQuestsFlag, BattleQuestsFlag as BattleQuestsFlag, MarathonQuestsFlag as MarathonQuestsFlag, MapboxQuestsFlag as MapboxQuestsFlag
from gui.shared.system_factory import registerQuestFlag as registerQuestFlag

class QuestFlagTypes(object):
    PERSONAL_MISSIONS = 'personalMissions'
    BATTLE = 'battleQuests'
    MAPBOX = 'mapboxQuests'
    MARATHON = 'marathonQuests'
    ELEN = 'elenQuests'
    RANKED = 'rankedQuests'
