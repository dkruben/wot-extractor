# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/pet_system/cgf_components/storage_state_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/pet_system/cgf_components/storage_state_component.py
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from gui.pet_system.constants import StorageStateKey

@registerComponent
class StorageStateComponent(object):
    group = 'Pet system'
    editorTitle = 'Pet Storage State Component'
    domain = CGF.Domain.Client
    names = {name: name for name in StorageStateKey.ALL}
    storageObjectKey = ComponentProperty(type=CGF.PropertyType.String, editorName='storage object key', value='active', annotations={'comboBox': names})
