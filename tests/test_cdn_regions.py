import unittest

from wot_extractor.cdn_regions import CDN_REGIONS, matrix, require_region


class CdnRegionsTests(unittest.TestCase):
    def test_all_targets_are_wot_and_exclude_lesta(self):
        self.assertEqual(list(CDN_REGIONS), ['EU', 'CT', 'NA', 'ASIA', 'CN'])
        self.assertEqual(len(matrix('ALL')['include']), 5)
        for target in matrix('ALL')['include']:
            self.assertEqual(target['guid'], 'WOT.' + target['realm'] + '.PRODUCTION')
            self.assertNotIn('lesta', target['host'])
        for realm in ['RU', 'PT_RU', 'LESTA', 'MT.RU.PRODUCTION']:
            with self.assertRaises(ValueError):
                require_region(realm)

    def test_selection_is_validated_and_deduplicated(self):
        self.assertEqual([x['realm'] for x in matrix('na, ASIA,cn,NA')['include']], ['NA', 'ASIA', 'CN'])
        for selection in ['', 'EU,,CT', 'EU,RU', 'ALL,NA', 'UNKNOWN']:
            with self.assertRaises(ValueError):
                matrix(selection)
