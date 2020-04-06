# HIKE API Schemas

## Description

This folder contains the JSON Schemas for event API messages from TA3 to TA4 HIKE system

These events are sent in the form of a REST POST request:
### POST /op/{op_id}/event
```
{
    timestamp,
    event_type,
    event_data
}
```

where event_data is expanded upon depending on event type

## Contents

**eventWrapper.json.schema** - general event format for used by all events

**transactionResponse.json.schema** - 0x0 Transaction Response

**agentSpawnEvent.json.schema** - 0x1 Agent Spawn

**exploitDeploymentEvent.json.schema** - 0x2 Exploit Deployment

**appliedOnHostAction.json.schema** - 0x3 Applied On-Host Action

**newHostDetection.json.schema** - 0x4 New Host Detection

**agentRemovalEvent.json.schema** - 0x5 Event Removal

**operationPhaseUpdate.json.schema** - 0x6 Operation Phase Update

**newActiveFingerprint.json.schema** - 0x7 New Active Fingerprint

**policyRequest.json.schema** - 0x8 Policy Request

**exploitDevelopmentRequest.json.schema** - 0x9 Exploit Development Request

**encounteredError.json.schema** - 0xA Encountered Error
