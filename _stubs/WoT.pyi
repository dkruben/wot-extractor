# wot-extractor: STUB do modulo 'WoT', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (4 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

def computeStabilisedVehicleMatrixU64(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
packAngleToUint: Any  # importado com 'from WoT import' em 1 ficheiro(s)
unpackAngleFromUint: Any  # importado com 'from WoT import' em 1 ficheiro(s)
def unpackAuxVehiclePhysicsData(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)
def unpackWheelScroll(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def unpackWheelSteering(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
