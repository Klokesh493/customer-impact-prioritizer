# Customer Impact Prioritizer architecture

Ranks incidents by affected users, payment impact, region spread, and service tier.

```mermaid
flowchart LR
    N0["sample_incidents.csv"]
    N1["impact_prioritizer.py"]
    N2["score / prioritize"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
