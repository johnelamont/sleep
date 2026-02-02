# Sleep Function

A serverless REST API endpoint built with [Zoho Catalyst](https://catalyst.zoho.com/) that sleeps for a specified duration.

## Overview

This is a lightweight function-as-a-service (FaaS) application demonstrating a basic HTTP endpoint on the Zoho Catalyst platform. It accepts either a `seconds` or `milliseconds` parameter and pauses execution for that duration before returning a response.

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
| `seconds` | number | * | Number of seconds to sleep (0-30) |
| `milliseconds` | number | * | Number of milliseconds to sleep (0-30000) |

\* Provide one or the other, not both. Do NOT exceed 30 seconds or 30000 milliseconds

**Example Requests**:
```bash
# Using seconds
curl "https://sleep-900403292.development/sleep_function?seconds=5"

# Using milliseconds
curl "https://sleep-900403292.development/sleep_function?milliseconds=500"
```

**Success Response**:
```json
{
  "success": true,
  "message": "Slept for 5 seconds",
  "slept_for": 5,
  "unit": "seconds"
}
```

```json
{
  "success": true,
  "message": "Slept for 500 milliseconds",
  "slept_for": 500,
  "unit": "milliseconds"
}
```

**Error Responses**:

Missing parameter:
```json
{"error": "seconds or milliseconds parameter is required", "usage": "?seconds=NUMBER or ?milliseconds=NUMBER"}
```

Both parameters provided:
```json
{"error": "Provide either seconds or milliseconds, not both", "usage": "?seconds=NUMBER or ?milliseconds=NUMBER"}
```

Invalid type:
```json
{"error": "Invalid seconds parameter. Must be a number.", "provided": "abc"}
```

Out of range:
```json
{"error": "Maximum sleep time is 30 seconds", "provided": 60}
```

Negative value:
```json
{"error": "Seconds must be non-negative", "provided": -5}
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
