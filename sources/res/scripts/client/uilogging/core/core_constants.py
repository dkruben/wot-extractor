# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/core/core_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/core_constants.py
from __future__ import absolute_import
from enum import Enum
from constants import AUTH_TOKEN_REQUEST_TIMEOUT
from gui.clans.settings import REQUEST_TIMEOUT

class HttpHeaders(str, Enum):
    AUTH_TOKEN = 'X-TOKEN'
    USER_ID = 'X-SPA-ID'
    CONTENT_TYPE = 'Content-Type'


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
REQUEST_SESSION_TIMEOUT = AUTH_TOKEN_REQUEST_TIMEOUT + REQUEST_TIMEOUT + 1.0
RETRY_REQUEST_SESSION_DELAY = 0.5
ENSURE_SESSION_TICK = 5.0
MAX_SESSION_GET_RETRIES = 3
MIN_SESSION_LIFE_TIME = LOGS_SEND_PERIOD * 2
