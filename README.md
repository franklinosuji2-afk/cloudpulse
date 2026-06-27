# CloudPulse Intelligent Observability Platform

CloudPulse is a microservices-based observability platform that simulates **real-time metric ingestion**, **anomaly detection**, and **root cause analysis (RCA)** for distributed cloud systems.

Built to demonstrate modern **DevOps**, **SRE**, and **Cloud Engineering** practices, CloudPulse helps identify abnormal system behavior and correlate incidents with operational events such as deployments or traffic spikes.

---

## 🚀 Why CloudPulse?

Modern distributed systems generate massive volumes of telemetry data.  
The challenge is no longer collecting metrics it is **understanding anomalies fast enough to prevent downtime**.

CloudPulse addresses this by providing:

- **Real-time metric collection**
- **Statistical anomaly detection**
- **Root cause correlation**
- **Event-driven incident analysis**
- **Production-style microservice architecture**

This project simulates how modern SRE teams monitor critical workloads such as checkout systems, payment APIs, and customer-facing services.

---

# 🏗 Architecture

```text
                  ┌────────────────────┐
                  │ Metric Generator   │
                  │ (CPU Usage Stream) │
                  └─────────┬──────────┘
                            │
                            ▼
                ┌──────────────────────┐
                │ Ingestion Service    │
                │ FastAPI + SQLAlchemy │
                └─────────┬────────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ PostgreSQL DB    │
                 │ Metrics Storage  │
                 └──────┬─────┬─────┘
                        │     │
              ┌─────────┘     └─────────┐
              ▼                         ▼
   ┌──────────────────┐       ┌─────────────────┐
   │ Anomaly Service  │       │ RCA Service     │
   │ Statistical AI   │       │ Event Correlator│
   └──────────────────┘       └─────────────────┘
```

---

# ⚙️ Services

## 1. Ingestion Service

Responsible for collecting and storing telemetry data.

### Responsibilities
- Generate CPU usage metrics
- Persist metrics to PostgreSQL
- Expose collected metrics via REST API

### Endpoints

#### Health Check
```bash
GET /
```

Response:

```json
{
  "service": "ingestion-service",
  "status": "healthy"
}
```

---

#### Collect Metric
```bash
POST /collect
```

Stores a simulated CPU metric.

Response:

```json
{
  "status": "metric stored"
}
```

---

#### Fetch Metrics
```bash
GET /metrics
```

Returns stored metrics.

---

---

## 2. Anomaly Detection Service

Performs statistical analysis on recent telemetry.

### Detection Algorithm

CloudPulse uses a **rolling window Z-score model**.

Formula:

```text
z = |(x - μ) / σ|
```

Where:

- **x** = latest metric
- **μ** = rolling mean
- **σ** = standard deviation

Severity thresholds:

| Z-Score | Severity |
|---------|----------|
| < 2     | Normal   |
| 2–3     | Warning  |
| > 3     | Critical |

---

### Endpoints

#### Health Check
```bash
GET /
```

#### Detect Anomalies
```bash
GET /detect
```

Example:

```json
{
  "latest_value": 243.4,
  "mean_window": 53.8,
  "std_dev": 15.4,
  "z_score": 12.3,
  "severity": "critical"
}
```

When an anomaly is detected, an event is sent to the RCA service.

---

## 3. RCA Service (Root Cause Analysis)

Correlates anomalies with operational events.

### Supported Events

- Deployment
- Traffic Spike
- Manual Incident Marker
- Anomaly Detection Trigger

### Endpoints

#### Health Check
```bash
GET /
```

Response:

```json
{
  "service": "rca-service"
}
```

---

#### Record Event
```bash
POST /event?event_type=traffic_spike&service=checkout-service
```

Response:

```json
{
  "status": "event recorded"
}
```

---

#### Analyze Incident
```bash
GET /analyze
```

Example response:

```json
{
  "root_cause": "checkout-service deployment",
  "confidence": 1.0,
  "evidence": [
    "service match",
    "deployment event"
  ]
}
```

---

# 🧠 Root Cause Correlation Logic

CloudPulse correlates:

- Recent anomalies
- Service-level events
- Operational changes

Example reasoning:

1. CPU spikes detected  
2. Deployment event recorded  
3. Same service affected  
4. RCA infers deployment as probable cause  

This mimics real-world incident response workflows.

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python |
| API Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Containerization | Docker |
| API Server | Uvicorn |
| Detection Logic | Statistical Z-score |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/franklinosuji2-afk/cloudpulse.git
cd cloudpulse
```

---

## Create Virtual Environment

### Windows

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start PostgreSQL

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

# ▶ Running Services

## Ingestion Service

```bash
python -m uvicorn services.ingestion_service.app:app --port 8000
```

---

## Anomaly Service

```bash
python -m uvicorn services.anomaly_service.app:app --port 8001
```

---

## RCA Service

```bash
python -m uvicorn services.rca_service.app:app --port 8002
```

---

# 🧪 Demo Workflow

### Step 1 - Generate Metrics

```powershell
1..30 | ForEach-Object {
    Invoke-RestMethod -Method POST http://127.0.0.1:8000/collect
}
```

---

### Step 2 - Detect Anomaly

```powershell
Invoke-RestMethod http://127.0.0.1:8001/detect
```

Example:

```json
{
  "severity": "critical",
  "z_score": 8.14
}
```

---

### Step 3 - Record Event

```powershell
Invoke-RestMethod -Method POST `
-Uri "http://127.0.0.1:8002/event?event_type=traffic_spike&service=checkout-service"
```

---

### Step 4 - Run RCA

```powershell
Invoke-RestMethod http://127.0.0.1:8002/analyze
```

Example:

```json
{
  "root_cause": "checkout-service traffic spike",
  "confidence": 0.85
}
```

---

# 🔥 Key Engineering Concepts Demonstrated

- Microservice architecture
- Event-driven design
- Statistical anomaly detection
- Incident correlation
- Observability pipelines
- Production-like service isolation
- API-first architecture
- Failure resilience

---

# 🚧 Future Improvements

Planned upgrades:

- Prometheus integration
- Grafana dashboards
- Kubernetes deployment
- Kafka event streaming
- Machine learning anomaly detection
- Slack / PagerDuty alerting
- CI/CD pipeline
- Terraform infrastructure provisioning

---

# 💡 Use Cases

CloudPulse can simulate monitoring for:

- E-commerce checkout systems
- Payment gateways
- SaaS platforms
- Banking transaction services
- Cloud-native applications

---

# 👨‍💻 Author

## Franklin Chinonso Osuji

AWS-Certified Cloud & DevOps Engineer focused on:

- Cloud Infrastructure
- Automation
- Reliability Engineering
- Scalable Production Systems

GitHub:  
https://github.com/franklinosuji2-afk

LinkedIn:  
(https://www.linkedin.com/in/franklin-osuji-a96003321/)

---

# 📄 License

MIT License

---

## Final Thought

> Great infrastructure should be invisible it just works, allowing engineers to focus on building products rather than fighting systems.

CloudPulse was built to reflect that philosophy.



