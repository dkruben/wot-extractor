# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dict2model/types.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dict2model/types.py
from __future__ import absolute_import
import typing
from dict2model.models import Model
from dict2model.validate import Validator
_ModelClassType = typing.TypeVar('_ModelClassType', bound=typing.Type[Model])
SchemaModelClassesType = typing.Union[(_ModelClassType, typing.Type[typing.Dict])]
ValidatorType = typing.Union[(Validator, typing.Callable[([typing.Any], typing.Any)])]
ValidatorsType = typing.Optional[typing.Union[(ValidatorType, typing.List[ValidatorType])]]
TFilterParams = typing.Optional[typing.Any]
TFilter = typing.Callable[([TFilterParams], bool)]
