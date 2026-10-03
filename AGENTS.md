# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
hazard-rate-estimator

Checker:
alert-fatigue-suppressor

## Coordination Protocol
- **Primary Agent**: icu-sepsis-early-warning-sentinel
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
