# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/dog_tags/dog_tag_processors.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dog_tags/dog_tag_processors.py
import typing
from dog_tags_common.config.common import DEFAULT_GRADE
from dog_tags_common.dog_tags_storage import EMPTY_PROGRESS_RECORD, ProgressRecord
if typing.TYPE_CHECKING:
    from dossiers2 import DossierDescr
    from dog_tags_common.config.dog_tag_framework import ComponentDefinition

def getCoupledDogTagProgress(accDossierDescr, component):
    unlockKey = component.unlockKey
    achievementType, achievementId, _ = unlockKey
    achievementId = int(achievementId)
    if achievementType is None or achievementId is None or accDossierDescr is None or achievementType not in accDossierDescr or achievementId not in accDossierDescr[achievementType]:
        return EMPTY_PROGRESS_RECORD
    return ProgressRecord(accDossierDescr[achievementType][achievementId][0], DEFAULT_GRADE)
