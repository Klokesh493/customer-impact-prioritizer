# Customer Impact Prioritizer

Ranks incidents by affected users, payment impact, region spread, and service tier.

Focus: Consumer-scale SRE incident response.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 impact_prioritizer.py sample_incidents.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

An incident commander needs a consistent way to order incidents by user impact, payment impact, region spread, and service tier.

## Project walkthrough

```mermaid
flowchart LR
    A["Incident impact CSV"]
    B["Weight user count, payments, region spread, and tier"]
    C["Sort by impact score"]
    D["Ordered incidents with scores"]
    A --> B --> C --> D
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 impact_prioritizer.py sample_incidents.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
