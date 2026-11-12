# Customer Impact Prioritizer architecture

Ranks incidents by affected users, payment impact, region spread, and service tier.

```mermaid
flowchart LR
    A["Incident impact CSV"]
    B["Weight user count, payments, region spread, and tier"]
    C["Sort by impact score"]
    D["Ordered incidents with scores"]
    A --> B --> C --> D
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
