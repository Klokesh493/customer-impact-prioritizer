# Skills and verification

## What this repository demonstrates

An incident ranking utility that scores affected-user counts, payment impact, regional spread, and service tier. It sorts incident rows by descending score so responders can explain the priority order.

## Reproduce the result

Checkout card failures score 26 and rank ahead of photo upload retries at 1. Reproduce the primary fixture with `python3 impact_prioritizer.py sample_incidents.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The ranking depends on trustworthy input counts and fixed weights. Deduplicate reports before summing or comparing impact.

Check whether affected-user counts include duplicate reports before relying on incident ordering.

[impact_prioritizer.py](../impact_prioritizer.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
