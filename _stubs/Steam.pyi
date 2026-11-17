# wot-extractor: STUB do modulo 'Steam', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (3 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

def activateGameOverlayToWebPage(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def gameOverlayActivated(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)
def isInited(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 0 argumento(s) posicional(is)
def isOverlayEnabled(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 0 argumento(s) posicional(is)
def microTxnAuthorizationResponse(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
