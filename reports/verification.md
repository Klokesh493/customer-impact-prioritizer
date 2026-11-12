# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 impact_prioritizer.py sample_incidents.csv
26 checkout card failures
01 photos upload retries
test_places_high_customer_impact_first (test_impact_prioritizer.ImpactPrioritizerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
