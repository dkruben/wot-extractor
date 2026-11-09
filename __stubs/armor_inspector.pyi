# wot-extractor: STUB do modulo 'armor_inspector', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (4 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

FADE_DURATION: Any  # usado sem chamada 1x
def getColor(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def getPenColor(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def hide(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 3 argumento(s) posicional(is)
def setSettings(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 7 argumento(s) posicional(is)
def setShellParams(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 13 argumento(s) posicional(is)
def show(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 8 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
