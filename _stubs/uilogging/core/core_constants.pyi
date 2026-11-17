# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/core_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from constants import AUTH_TOKEN_REQUEST_TIMEOUT as AUTH_TOKEN_REQUEST_TIMEOUT
from gui.clans.settings import REQUEST_TIMEOUT as REQUEST_TIMEOUT
HTTP_OK_STATUS = 200
HTTP_SESSION_EXPIRED = 498
HTTP_DEFAULT_TIMEOUT = 30
FINAL_FLUSH_TIMEOUT = 3
DEFAULT_COMPRESSION_LEVEL = 5
LOGS_SEND_PERIOD = 5.0
LOGS_FORCE_SEND_PERIOD = 600.0
LOGS_MAX_QUEUE_SIZE = 5000
LOGS_MAX_COUNT_PER_SEND = 50
LOG_RECORD_MAX_PROPERTIES_COUNT = 1000
REQUEST_SESSION_TIMEOUT: Any
RETRY_REQUEST_SESSION_DELAY = 0.5
ENSURE_SESSION_TICK = 5.0
MAX_SESSION_GET_RETRIES = 3
MIN_SESSION_LIFE_TIME: Any

class HttpHeaders(str, Enum):
    AUTH_TOKEN = 'X-TOKEN'
    USER_ID = 'X-SPA-ID'
    CONTENT_TYPE = 'Content-Type'
