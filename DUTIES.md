# Duties and Responsibilities for ICU Sepsis Early Warning Sentinel Agent

## Dual-Control Architecture
Maker:
hazard-rate-estimator

Checker:
alert-fatigue-suppressor

## Operational Workflow
1. The Maker (hazard-rate-estimator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (alert-fatigue-suppressor) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
