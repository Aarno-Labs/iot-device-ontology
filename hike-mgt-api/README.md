# HIKE API Schemas

## Description

This folder contains the JSON Schemas for event API messages from TA3 to TA4 HIKE system

These events are sent in the form of a REST POST request:

### POST /op/{op_id}/event
```
{
    opID,
    timestamp,
    eventType,
    eventData
}
```

where eventData is expanded upon depending on event type

## Contents

**transactionResponseEvent.json.schema** - 0x0 Transaction Response

**agentSpawnEvent.json.schema** - 0x1 Agent Spawn

**exploitDeploymentEvent.json.schema** - 0x2 Exploit Deployment

**appliedOnHostActionEvent.json.schema** - 0x3 Applied On-Host Action

**newHostDetectionEvent.json.schema** - 0x4 New Host Detection

**agentRemovalEvent.json.schema** - 0x5 Event Removal

**operationPhaseUpdateEvent.json.schema** - 0x6 Operation Phase Update

**newActiveFingerprintEvent.json.schema** - 0x7 New Active Fingerprint

**policyRequestEvent.json.schema** - 0x8 Policy Request

**exploitDevelopmentRequestEvent.json.schema** - 0x9 Exploit Development Request

**encounteredErrorEvent.json.schema** - 0xA Encountered Error

**ta1FingerprintDataEvent.json.schema** - 0xB TA Fingerprint Data
