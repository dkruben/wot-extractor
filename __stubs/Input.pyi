# wot-extractor: STUB do modulo 'Input', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (9 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

InputLayer: Any  # importado com 'from Input import' em 2 ficheiro(s)
InputTriggerPressed: Any  # importado com 'from Input import' em 1 ficheiro(s)
KeyInputAction: Any  # importado com 'from Input import' em 1 ficheiro(s)
TriggerEvent: Any  # importado com 'from Input import' em 6 ficheiro(s)
def inputSystem(*args: Any, **kwargs: Any) -> Any: ...  # chamado 29x com 0 argumento(s) posicional(is)
def isActive(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def isFired(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def loadProfiles(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is)
def setCommandMapping(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)
def setCommandMappingNames(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def unloadProfiles(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
