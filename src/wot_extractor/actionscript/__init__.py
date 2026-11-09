"""ActionScript/Scaleform (fase D): catalogo dos SWF, codigo AS3 e recursos incorporados."""

from .engine import ASOptions, ASResult, run_actionscript
from .ffdec import FFDec, find_ffdec

__all__ = ["ASOptions", "ASResult", "FFDec", "find_ffdec", "run_actionscript"]
