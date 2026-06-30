# GCPSolutionArchitect: Multi-Agent Cloud Design Framework

GCPSolutionArchitect is a robust, multi-agent conversational system built with **Microsoft AutoGen (v0.2+)** designed to architect enterprise-grade Google Cloud Platform (GCP) solutions. The system leverages hosted open-weights models from the **NVIDIA NIM API** to provide expert-level architectural guidance, automated infrastructure visualization, and security validation.

## 🚀 Overview

The framework orchestrates a team of specialized agents:
- **GCP_Architect**: Designs multi-region layouts and advanced networking (Shared VPC, VPC Service Controls).
- **GCP_Engineer**: Implements the design by generating visual diagrams and performing security scans.
- **GCP_Auditor**: Ensures compliance with GDPR, validates encryption, and provides cost estimates.
- **User_Proxy**: Coordinates the workflow, executes tools, and compiles the final design report.

## 🛠️ Components

### 1. `gcp_diagram_builder.py`
A modular helper that uses `matplotlib` and `networkx` to build a visual, multi-tiered diagram of GCP components. It automatically organizes infrastructure into tiers (Edge, Load Balancer, GKE, Data, Security, etc.) for clarity.

### 2. `nvidia_autogen_orchestrator.py`
The main orchestration script that:
- Connects to NVIDIA NIM API (base URL: `https://integrate.api.nvidia.com/v1`).
- Defines custom tools for diagramming and network scanning.
- Manages a structured `GroupChat` workflow.
- Generates `gcp_enterprise_architecture.md` as the final output.

## 📋 Prerequisites

- **Python 3.10+**
- **NVIDIA Developer Account**: Obtain an API key from [NVIDIA Build](https://build.nvidia.com).
- **Dependencies**:
  ```bash
  pip install pyautogen matplotlib networkx
  ```

## ⚙️ Configuration

Set your NVIDIA API key as an environment variable:
```bash
export NVIDIA_API_KEY="your_nvapi_key_here"
```

## 🏃 Usage

Run the orchestrator to initiate the design process:
```bash
python nvidia_autogen_orchestrator.py
```

### Target Requirement
By default, the system designs a **secure, multi-tenant global banking data streaming framework** with the following constraints:
- 50,000 requests per second.
- GKE Autopilot infrastructure.
- Strict ledger encryption.
- <50ms data access latency.
- Regional data privacy compliance.

## 📤 Outputs

- **`gcp_architecture.png`**: A visual representation of the designed infrastructure.
- **`gcp_enterprise_architecture.md`**: A comprehensive design report containing the conversation logs, architectural decisions, security findings, and cost projections.

## 🔒 Security Features

The **GCP_Engineer** agent executes a local port scan (`network_scan_validator`) to ensure that common entry points (e.g., SSH, HTTP, RDP) are properly secured in a Zero-Trust baseline configuration.

## ⚖️ License
This project is provided for educational and demonstration purposes. Ensure compliance with GCP best practices and regional regulations before production deployment.
