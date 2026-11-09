"""Detecao das instalacoes do World of Tanks (EU / CT)."""

from .detector import DetectionResult, detect
from .install import ClientInstall, inspect_install

__all__ = ["ClientInstall", "DetectionResult", "detect", "inspect_install"]
