# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/comp7_light_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.Scaleform.genConsts.COMP7_LIGHT_HANGAR_ALIASES import COMP7_LIGHT_HANGAR_ALIASES as COMP7_LIGHT_HANGAR_ALIASES
from constants_utils import ConstInjector as ConstInjector
from gui.prb_control import settings as settings
from messenger import m_constants as m_constants
COMP7_HANGAR_ALIAS = COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_LOBBY_HANGAR
COMP7_LIGHT_ENTRY_POINT_ALIAS = 'Comp7LightEntryPoint'

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    COMP7_LIGHT = 34359738368

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type: Any
    COMP7_LIGHT = 'comp7Light'
    COMP7_LIGHT_SQUAD = 'comp7LightSquad'

class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type: Any
    COMP7_LIGHT = 'comp7Light'

class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    COMP7_LIGHT_PROGRESSION_NOTIFICATIONS = 301
