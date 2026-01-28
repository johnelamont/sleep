# Sleep Function

A serverless REST API endpoint built with [Zoho Catalyst](https://catalyst.zoho.com/) that sleeps for a specified number of seconds.

## Overview

This is a lightweight function-as-a-service (FaaS) application demonstrating a basic HTTP endpoint on the Zoho Catalyst platform. It accepts a `seconds` parameter and pauses execution for that duration before returning a response.

## Project Structure

```
sleep/
├── .catalystrc                 # Local Catalyst configuration
├── catalyst.json               # Project manifest
└── functions/
    └── sleep_function/
        ├── index.py            # Handler implementation
        ├── catalyst-config.json # Function configuration
        └── requirements.txt    # Python dependencies
```

## Technology Stack

- **Platform**: Zoho Catalyst
- **Runtime**: Python 3.9
- **Function Type**: BasicIO (HTTP request/response handler)

## API Reference

### Sleep Endpoint

**Endpoint**: `/sleep_function`

**Method**: GET

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `seconds` | number | Yes | Number of seconds to sleep (0-30) |

**Example Request**:
```bash
curl "https://sleep-900403292.development/sleep_function?seconds=5"
```

**Success Response**:
```json
{
  "success": true,
  "message": "Slept for 5 seconds",
  "slept_for": 5
}
```

**Error Responses**:

Missing parameter:
```json
{"error": "seconds parameter is required", "success": false}
```

Invalid type:
```json
{"error": "Invalid seconds parameter. Must be a number.", "success": false}
```

Out of range:
```json
{"error": "Maximum sleep time is 30 seconds", "success": false}
```

Negative value:
```json
{"error": "Seconds must be a positive number", "success": false}
```

## Dependencies

- `zcatalyst-sdk==1.0.3` - Zoho Catalyst Python SDK

## Installation

### Prerequisites

- Python 3.9+
- Zoho Catalyst CLI

### Local Setup

```bash
pip install -r functions/sleep_function/requirements.txt
```

### Deploy to Catalyst

```bash
catalyst deploy
```

## Configuration

The function is configured via `catalyst-config.json`:

- **Runtime**: Python 3.9
- **Type**: BasicIO
- **Entry Point**: `index.py`

## License

[Specify your license]
