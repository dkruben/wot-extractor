# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/live_crc_accountdata.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/live_crc_accountdata.py
from __future__ import absolute_import
from live_crc import gen_delSubkeys_fn, gen_livehash_fn, gen_mergeCache_fn, gen_extract_fn, INCLUDE
accountPersistentCacheDataScheme = {INCLUDE: {
           'economics', 'inventory', 'quests', 'tokens', 
           'potapovQuests', 'intUserSettings'}, 
   'stats': {INCLUDE: {
                     'dossier', 'eliteVehicles', 'unlocks', 'vehTypeXP'}}}
accountDataPersistentHash = gen_livehash_fn(accountPersistentCacheDataScheme)
accountDataDelPersistent = gen_delSubkeys_fn(accountPersistentCacheDataScheme)
accountDataMergePersistent = gen_mergeCache_fn(overwrite=False)
accountDataExtractPersistent = gen_extract_fn(accountPersistentCacheDataScheme)

def accountDataGetDiffForPersistent(diff):
    good_keys = {
     'economics', 'inventory', 'stats', 'quests', 'tokens', 'potapovQuests', 
     'intUserSettings'}
    mydiff = {}
    for k, v in diff.items():
        if k in good_keys or isinstance(k, tuple) and k[0] in good_keys:
            mydiff[k] = v

    return mydiff
