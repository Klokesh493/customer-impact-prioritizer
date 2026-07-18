import unittest

from impact_prioritizer import prioritize


class ImpactPrioritizerTest(unittest.TestCase):
    def test_places_high_customer_impact_first(self):
        rows = [
            {"service": "photos", "summary": "slow", "tier": "tier2", "affected_users": "100", "payment_impact": "no", "regions": "1"},
            {"service": "checkout", "summary": "fail", "tier": "tier1", "affected_users": "9000", "payment_impact": "yes", "regions": "4"},
        ]
        self.assertEqual(prioritize(rows)[0]["service"], "checkout")


if __name__ == "__main__":
    unittest.main()
