# 02 - Risk Model

Risk is modeled as a set of hard limits that are enforced at multiple layers.

## Core Risk Limits
- **Max drawdown:** stop trading if equity falls beyond the threshold.
- **Max exposure:** cap open exposure per instrument and in aggregate.
- **Order rate:** prevent sudden spikes in order volume.
- **Kill switch:** a manual or automated hard stop.

## Enforcement Layers
1. **Pre-trade checks** in the order router.
2. **Ongoing monitoring** for drawdown and anomalies.
3. **Manual controls** that can halt execution immediately.
