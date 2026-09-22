# CloudPulse

CloudPulse is a local-first cloud observability and FinOps platform for collecting infrastructure telemetry, detecting anomalies, analyzing operational events, and exposing metrics through containerized Python services.

## Architecture

CloudPulse is composed of independent services:

- Ingestion Service - receives infrastructure telemetry and events.
- Anomaly Service - detects statistical anomalies.
- RCA Service - performs root-cause analysis workflows.
- FinOps Service - analyzes infrastructure cost data.
- API Gateway - provides HTTP endpoints for the platform.
- AI Service - supports AI-assisted operational analysis.

## Technology Stack

- Python
- FastAPI
- Docker
- Docker Compose
- PostgreSQL
- Prometheus-compatible metrics
- Statistical anomaly detection
- AI-assisted analysis

## Anomaly Detection

CloudPulse uses a standardized score for basic anomaly detection:

    z = |(x - mean) / standard_deviation|

Higher absolute z-scores indicate observations that differ more strongly from the historical baseline.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Service health and information |
| `/collect` | Collect telemetry |
| `/metrics` | Expose metrics |
| `/detect` | Run anomaly detection |
| `/event` | Submit an operational event |
| `/analyze` | Run analysis |

## Project Structure

```text
cloudpulse/
|-- services/
|   |-- ai_service/
|   |-- anomaly_service/
|   |-- api_gateway/
|   |-- finops_service/
|   |-- ingestion_service/
|   `-- rca_service/
|-- docs/
|-- docker-compose.yml
|-- Makefile
`-- requirements.txt
Run Locally
docker compose up --build

Validate the Compose configuration:

docker compose config

The project is designed for local development and experimentation without requiring a paid cloud environment.

CI

GitHub Actions validates the Python services and Docker Compose configuration on pushes and pull requests to main.

Author

Franklin Osuji

Cloud Infrastructure and DevOps Engineer

GitHub: https://github.com/franklinosuji2-afk
Portfolio: https://fc-dev.netlify.app/
