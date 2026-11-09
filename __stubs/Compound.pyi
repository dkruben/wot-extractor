# wot-extractor: STUB do modulo 'Compound', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (4 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

AppearanceDeactivatedEvent: Any  # importado com 'from Compound import' em 1 ficheiro(s)
def AppearanceRefreshRequestedEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
Compound: Any  # importado com 'from Compound import' em 1 ficheiro(s)
CompoundBasedComposerComponent: Any  # usado sem chamada 4x
LocalTransformNodeFollower: Any  # usado sem chamada 2x
NodeInteractType: Any  # usado sem chamada 3x
NodeLeaderComponent: Any  # usado sem chamada 2x
def onClientCompositionAboutToBeRemoved(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
