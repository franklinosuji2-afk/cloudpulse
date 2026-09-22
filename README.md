# CloudPulse

CloudPulse is a local-first cloud observability and FinOps platform for collecting infrastructure telemetry, detecting anomalies, analyzing operational events, and exposing operational metrics through containerized Python services.

The project brings together observability, anomaly detection, FinOps analysis, root-cause analysis, and AI-assisted operations into a modular platform designed for local development and experimentation.

---

## Overview

CloudPulse is built around a service-oriented architecture where individual components handle specific operational responsibilities.

The platform focuses on:

- Infrastructure telemetry ingestion
- Operational metrics
- Statistical anomaly detection
- Root-cause analysis workflows
- Infrastructure cost analysis
- Operational event processing
- AI-assisted analysis
- Containerized service deployment
- Local-first development
- CI validation

---

## Architecture

```text
                         Infrastructure / Client
                                  |
                                  v
                         +----------------+
                         |   API Gateway  |
                         +-------+--------+
                                 |
              +------------------+------------------+
              |                  |                  |
              v                  v                  v
       Ingestion Service   Anomaly Service    Event Processing
              |                  |                  |
              |                  v                  |
              |          Anomaly Detection           |
              |                                      |
              +------------------+-------------------+
                                 |
              +------------------+------------------+
              |                  |                  |
              v                  v                  v
        FinOps Service       RCA Service        AI Service
              |                  |                  |
              +------------------+------------------+
                                 |
                                 v
                          Operational Data
                                 |
                    +------------+------------+
                    |                         |
                    v                         v
               PostgreSQL             Prometheus Metrics
Service Architecture

CloudPulse is composed of independent services, each responsible for a specific operational capability.

Ingestion Service

Receives infrastructure telemetry and operational events for processing by the platform.

Anomaly Service

Analyzes incoming data and identifies observations that deviate from an established statistical baseline.

RCA Service

Provides root-cause analysis workflows for investigating operational events and potential infrastructure issues.

FinOps Service

Processes infrastructure cost information and provides a foundation for cost-oriented analysis.

API Gateway

Provides HTTP endpoints through which clients and other services interact with CloudPulse.

AI Service

Provides AI-assisted operational analysis capabilities.

Technology Stack
Application
Python
FastAPI
REST APIs
Infrastructure
Docker
Docker Compose
PostgreSQL
Observability
Prometheus-compatible metrics
Operational telemetry
Metrics endpoints
Analytics
Statistical anomaly detection
Root-cause analysis workflows
FinOps analysis
AI-assisted analysis
Automation
GitHub Actions
Automated validation
Containerized development
Anomaly Detection

CloudPulse uses a standardized statistical score for basic anomaly detection:

z = |(x - mean) / standard_deviation|

The absolute z-score represents how far an observation is from the historical mean in standard-deviation units.

Higher absolute values indicate observations that differ more strongly from the established baseline.

This provides a simple statistical foundation for identifying potentially anomalous infrastructure or operational behavior.

API

The API Gateway exposes endpoints for interacting with CloudPulse capabilities.

Endpoint	Purpose
/	Service health and platform information
/collect	Collect infrastructure telemetry
/metrics	Expose operational metrics
/detect	Run anomaly detection
/event	Submit an operational event
/analyze	Run operational analysis

The exact request and response schemas are defined by the implementation of the individual services.

Observability Workflow

A typical telemetry workflow is:

Infrastructure Data
       |
       v
Ingestion Service
       |
       v
Operational Processing
       |
       +------------------+
       |                  |
       v                  v
Anomaly Detection      Metrics
       |                  |
       v                  v
   RCA / Analysis     Prometheus
       |
       v
AI-Assisted Analysis

This architecture demonstrates how telemetry can flow through ingestion, detection, analysis, and observability components.

FinOps Workflow

CloudPulse also introduces infrastructure cost analysis into the operational workflow.

Infrastructure Cost Data
          |
          v
     FinOps Service
          |
          v
   Cost Analysis
          |
          v
Operational Insights

The goal is to connect infrastructure operations with cost visibility rather than treating observability and FinOps as completely separate concerns.

Project Structure
cloudpulse/
|
|-- services/
|   |
|   |-- ai_service/
|   |
|   |-- anomaly_service/
|   |
|   |-- api_gateway/
|   |
|   |-- finops_service/
|   |
|   |-- ingestion_service/
|   |
|   `-- rca_service/
|
|-- docs/
|
|-- docker-compose.yml
|
|-- Makefile
|
`-- requirements.txt

The service-oriented structure allows individual components to evolve independently while remaining part of a single operational platform.

Local Development

CloudPulse is designed as a local-first platform.

This allows the architecture to be developed and tested without requiring continuously running paid cloud infrastructure.

Prerequisites

Typical local requirements include:

Docker
Docker Compose
Python
Git
Start the Platform
docker compose up --build
Validate Docker Compose Configuration
docker compose config
Stop the Platform
docker compose down
Containerized Architecture

Docker Compose provides the local orchestration layer for running the CloudPulse services.

                    Docker Compose
                          |
        +-----------------+-----------------+
        |        |        |        |        |
        v        v        v        v        v
       API    Ingestion  Anomaly   FinOps    RCA
        |        |        |        |        |
        +--------+--------+--------+--------+
                          |
                          v
                     PostgreSQL

The architecture is intentionally designed to make the individual services reproducible in a local environment.

CI

CloudPulse uses GitHub Actions to validate changes to the project.

The CI workflow validates:

Python service compilation
Docker Compose configuration
Repository changes

The workflow runs on pushes and pull requests targeting main.

Workflow:

Git Push / Pull Request
          |
          v
     GitHub Actions
          |
          +------------------+
          |                  |
          v                  v
   Python Validation    Docker Compose
                         Validation
Engineering Practices

CloudPulse demonstrates practical experience with:

Service-oriented architecture
Python backend development
FastAPI
Docker
Docker Compose
PostgreSQL
Infrastructure telemetry
Observability
Metrics
Statistical anomaly detection
Root-cause analysis concepts
FinOps engineering concepts
AI-assisted operations
CI/CD automation
Local-first cloud engineering
SRE and Platform Engineering Focus

CloudPulse is particularly focused on operational engineering concepts such as:

Observability

Collecting telemetry and exposing operational metrics for infrastructure visibility.

Anomaly Detection

Identifying unusual behavior through statistical analysis.

Incident Analysis

Supporting operational event analysis and root-cause investigation.

FinOps

Connecting infrastructure operations with cost analysis.

Automation

Using containerization and CI/CD to make operational workflows reproducible.

Local-First Engineering

Providing a realistic cloud-oriented development environment without requiring paid cloud resources for normal development.

Design Goals

CloudPulse was designed around several engineering goals:

Telemetry
    |
    v
Detection
    |
    v
Analysis
    |
    +---------> Root Cause Analysis
    |
    +---------> FinOps Insights
    |
    +---------> AI-Assisted Analysis
    |
    v
Operational Visibility

The broader objective is to demonstrate how observability, automation, FinOps, and operational intelligence can be combined into a single platform engineering workflow.

Future Enhancements

Potential extensions include:

Expanded anomaly detection algorithms
Alerting and notification workflows
SLO and SLA tracking
Prometheus alert rules
Grafana dashboards
Distributed tracing
Advanced FinOps reporting
Automated incident correlation
Expanded AI-assisted RCA
Kubernetes deployment
GitOps-based deployment
OpenTelemetry integration
Security and Configuration

Credentials and sensitive configuration should not be committed to the repository.

Environment-specific configuration should be provided through appropriate environment variables, Docker secrets, Kubernetes secrets, or external secret-management systems.

Author

Franklin Osuji

Cloud Infrastructure and DevOps Engineer

GitHub:
https://github.com/franklinosuji2-afk

Portfolio:
https://fc-dev.netlify.app/

Project Focus

Cloud Observability | SRE | FinOps | DevOps | Platform Engineering | Python | FastAPI | Docker | PostgreSQL | Anomaly Detection
