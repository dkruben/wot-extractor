# wot-extractor: STUB do modulo 'Sound', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (8 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

Audition2D: Any  # importado com 'from Sound import' em 1 ficheiro(s)
RTPCComponent: Any  # importado com 'from Sound import' em 1 ficheiro(s)
RTPCSourceType: Any  # importado com 'from Sound import' em 1 ficheiro(s)
Sound3DComponent: Any  # importado com 'from Sound import' em 1 ficheiro(s)
def getRecommendedPreset(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 0 argumento(s) posicional(is)
def getSpatialAudioPreset(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is)
def reloadSoundEngine(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is)
setSpatialAudioEnabled: Any  # importado com 'from Sound import' em 1 ficheiro(s)
def setSpatialAudioPreset(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
