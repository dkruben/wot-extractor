# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/telecom_rentals_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
RENT_TOKEN_NAME = 'telecom_rent_token'
PARTNERSHIP_TOKEN_NAME = 'telecom_partnership_token'
PARTNERSHIP_BLOCKED_TOKEN_NAME = 'telecom_partnership_blocked_token'
ROSTER_EXPIRATION_TOKEN_NAME = 'telecom_roster_expiration_token'
TELECOM_RENTALS_CONFIG = 'telecom_rentals_config'
TELECOM_RENTALS_RENT_KEY = 'telecom'

class PartnershipState(IntEnum):
    NO_PARTNERSHIP = 0
    ACTIVE_PARTNERSHIP = 1
    BLOCKED_PARTNERSHIP = 2
