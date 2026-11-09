# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/types.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/types.py
from __future__ import absolute_import
import typing
from enum import Enum
FeatureType = typing.Union[(str, Enum)]
GroupType = typing.Union[(str, Enum)]
ActionType = typing.Union[(str, Enum)]
LogLevelType = typing.Union[(int, Enum)]
TimeLimitType = float
PartnerIdType = typing.Optional[str]
ItemType = typing.Union[(str, Enum)]
ItemStateType = typing.Optional[typing.Union[(str, Enum)]]
ParentScreenType = typing.Optional[typing.Union[(str, Enum)]]
InfoType = typing.Optional[typing.Union[(str, Enum)]]
SourceItemType = typing.Union[(str, Enum)]
DestinationItemType = typing.Union[(str, Enum)]
TransitionMethodType = typing.Union[(str, Enum)]
