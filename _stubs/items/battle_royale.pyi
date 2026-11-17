# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/battle_royale.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from items import vehicles as vehicles
SPAWNED_TAG_NAME = 'spawned'
BATTLE_ROYALE_TAG_NAME = 'battle_royale'
HUNTER_BOT_TAG_NAME = 'bot_hunter'

class ModulesInstaller(object):
    _UNLOCKS_START_INDEX = 2
    @classmethod
    def checkModuleValidity(cls, intCD, vehicleDescriptor):
        ...
    @classmethod
    def getItemsThisModuleUnlocks(cls, targetIntCD, vehicleDescriptor):
        ...

def isSpawnedBot(vehicleTags):
    ...
def isHunterBot(vehicleTags):
    ...
def isBattleRoyale(vehicleTags):
    ...
