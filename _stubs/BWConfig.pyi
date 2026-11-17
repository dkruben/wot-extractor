# wot-extractor: STUB do modulo 'BWConfig', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (1 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

debugConfig: Any  # usado sem chamada 8x
def getSections(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def readBool(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 2 argumento(s) posicional(is)
def readInt(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def readString(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 2 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
