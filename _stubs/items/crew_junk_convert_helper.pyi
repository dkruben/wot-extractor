# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/crew_junk_convert_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
from items import tankmen as tankmen, vehicles as vehicles
from typing import Dict as Dict, List as List, Tuple as Tuple
from items.tankmen import TankmanDescr as TankmanDescr
XP_TRASH_LIMIT = 210060
VALID_GROUP: tuple
NATIONS_CREW_BOOKS: dict
CREW_BOOK_XP = 250001
GUIDE_XP = 100001
BROCHURE_XP = 20001

def findJunkTankmen(tankmenCompDescrs, tankmenVehicles=None):
    ...
def calculateXpFromTankmen(tankmenCompDescrs):
    ...
def getNationBooksFromXp(xpByNation):
    ...
def _savingTrashTankmanXP(tankmanDescr, cashVehicleNativeType, savingXPByNation):
    ...
def isTrashTankman(tankman):
    ...
def checkXPLimit(tankman):
    ...
def checkFreeSkills(tankman):
    ...
def checkUnique(tankman):
    ...
