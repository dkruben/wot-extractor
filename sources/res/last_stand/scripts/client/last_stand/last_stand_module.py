# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/last_stand_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/last_stand_module.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from last_stand.cgf_components.show_event_component import LSShowEventSystem, LSShowEventComponent

@registerModule
class LastStandModeModule(object):
    name = 'Last Stand Mode Module'
    desc = 'Last Stand Core'
    group = 'Store Mode'
    systems = [
     CGF.RegisterSystem(LSShowEventSystem, domain=CGF.Domain.Client)]
    components = [
     LSShowEventComponent]
