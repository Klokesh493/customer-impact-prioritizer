# Customer Impact Prioritizer walkthrough

## Business problem

An incident commander needs a consistent way to order incidents by user impact, payment impact, region spread, and service tier.

## Reproduce the workflow

Run `python3 impact_prioritizer.py sample_incidents.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
26 checkout card failures
01 photos upload retries
```

The sample supplies these fields. `service`, `summary`, `tier`, `affected_users`, `payment_impact`, `regions`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
