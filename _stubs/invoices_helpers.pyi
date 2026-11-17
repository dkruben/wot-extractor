# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/invoices_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import DOSSIER_TYPE as DOSSIER_TYPE
from dossiers2.custom.clan_layout import CLAN_DOSSIER_LIST_BLOCKS as CLAN_DOSSIER_LIST_BLOCKS
from dossiers2.custom.account_layout import ACCOUNT_DOSSIER_STATIC_BLOCKS as ACCOUNT_DOSSIER_STATIC_BLOCKS, ACCOUNT_DOSSIER_BINARY_SET_BLOCKS as ACCOUNT_DOSSIER_BINARY_SET_BLOCKS, ACCOUNT_DOSSIER_BLOCKS as ACCOUNT_DOSSIER_BLOCKS, ACCOUNT_DOSSIER_DICT_BLOCKS as ACCOUNT_DOSSIER_DICT_BLOCKS, ACCOUNT_DOSSIER_LIST_BLOCKS as ACCOUNT_DOSSIER_LIST_BLOCKS

def checkAccountDossierOperation(dossierType, blockName, recordName, opType):
    ...
def checkClanDossierOperation(dossierType, blockName, recordName, opType):
    ...
def getLogDefaultsDossierOperation(finOpType, itemTypeIdx, partnerID=0, actionSetID=0):
    ...
