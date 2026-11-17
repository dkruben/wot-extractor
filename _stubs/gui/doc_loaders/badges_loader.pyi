# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/badges_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import resource_helper as resource_helper
from constants import ITEM_DEFS_PATH as ITEM_DEFS_PATH
from gui.shared.gui_items.badge import BadgeLayouts as BadgeLayouts, BadgeTypes as BadgeTypes
from realm import CURRENT_REALM as CURRENT_REALM
from soft_exception import SoftException as SoftException
from typing import Optional as Optional, Dict as Dict
_BADGES_XML_PATH: Any
_badges = None

def _readBadges():
    ...
def getSelectedByLayout(badgesIDs):
    ...
def getAvailableBadges():
    ...
def reloadAvailableBadges():
    ...
