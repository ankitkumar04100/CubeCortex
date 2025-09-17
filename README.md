# CubeCortex: The AI Brain for Microservices on Kubernetes

> **CubeCortex** – An AI-powered orchestration layer for Kubernetes microservices, enabling intelligent monitoring, anomaly detection, recommendations, and self-healing in modern cloud-native systems.

---

## Table of Contents
1. [Inspiration](#inspiration)  
2. [What it does](#what-it-does)  
3. [How we built it](#how-we-built-it)  
4. [Challenges we ran into](#challenges-we-ran-into)  
5. [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)  
6. [What we learned](#what-we-learned)  
7. [What's next for CubeCortex](#whats-next-for-cubecortex)  
8. [Detailed Architecture](#detailed-architecture)  
9. [Features](#features)  
10. [Built With](#built-with)  
11. [App Status](#app-status)  
12. [Setup Guide](#setup-guide)  
13. [Usage](#usage)  
14. [Equations & AI Models](#equations--ai-models)  
15. [Hackathon Story Expansion](#hackathon-story-expansion)  
16. [Roadmap](#roadmap)  
17. [Glossary](#glossary)  
18. [References](#references)  

---

## Inspiration

The journey of **CubeCortex** started with a simple question:  
*"What if Kubernetes microservices could think for themselves?"*

Modern cloud-native apps rely on **Kubernetes** for orchestration, scaling, and fault tolerance. Yet, managing complex microservices at scale often requires **manual oversight**, frequent interventions, and deep DevOps expertise. Teams face challenges like:
- Detecting anomalies before outages occur.  
- Coordinating services across heterogeneous environments.  
- Managing autoscaling intelligently (not just CPU/memory triggers).  
- Ensuring resiliency when **unexpected spikes** or **security threats** hit.  

We drew inspiration from **the human brain** – where neurons (agents) work together, coordinate signals, and self-correct. Similarly, CubeCortex uses **AI agents as neurons** to intelligently orchestrate microservices in Kubernetes.  

---

## What it does

CubeCortex is an **AI-driven orchestration layer** for Kubernetes clusters that adds intelligence to microservices.  

Key functionalities:
- 🔍 **Smart Anomaly Detection** – Detects abnormal latency, request spikes, or unusual API call patterns.  
- 🧠 **AI Agents for Microservices** – Specialized agents (Recommendation, Fraud Detection, Chat Support) that interact with microservices.  
- 📊 **Self-healing Workflows** – Automatically restarts unhealthy pods, re-routes traffic, or scales replicas intelligently.  
- 🎯 **Context-aware Autoscaling** – Uses ML-based predictions instead of static resource thresholds.  
- 🔗 **Service Dependency Graph** – Visualizes and learns from interactions between microservices.  
- 🌐 **End-to-End Dashboard** – Unified view of health, recommendations, alerts, and AI insights.  

**Elevator Pitch (200 characters):**  
*"CubeCortex brings AI intelligence into Kubernetes microservices – enabling smarter scaling, anomaly detection, and self-healing clusters for cloud-native applications."*

---

## How we built it

CubeCortex is built as a **layered architecture**:

1. **Base Layer – Kubernetes (GKE)**  
   - Core cluster orchestrating microservices.  
   - We deployed Google’s **Online Boutique** as the base microservice application.  

2. **CubeCortex Agent Layer**  
   - AI agents built in **Python (FastAPI + PyTorch)** and **Node.js (Express)**.  
   - Agents run as independent microservices, deployed via Kubernetes manifests.  

3. **AI Models**  
   - Time-series forecasting for load prediction.  
   - Anomaly detection using autoencoders.  
   - Recommendation systems for service interactions.  

4. **Orchestration Middleware**  
   - Agents communicate through **gRPC + REST APIs**.  
   - Shared event bus using **Kafka / PubSub**.  

5. **Dashboard Layer**  
   - Built in **React + Tailwind + Chart.js**.  
   - Real-time metrics pulled from Prometheus + custom APIs.  

---

## Challenges we ran into

- ⚡ **Complexity of Orchestration** – Making AI agents interact with Kubernetes events in real time required deep integration with **Kubernetes API Server**.  
- 📈 **Scaling ML Models** – Deploying ML inference in production without latency bottlenecks was challenging.  
- 🔒 **Security & Isolation** – Ensuring that AI agents don’t over-control or create cascading failures.  
- 🧩 **Data Availability** – Simulating realistic traffic to train models for anomaly detection and predictions.  
- ⏱️ **Hackathon Time Constraint** – Balancing feature scope vs stability in limited time.  

---

## Accomplishments that we're proud of

- Successfully created a **working AI-driven microservices orchestration system**.  
- Deployed multiple AI agents into GKE and proved interoperability.  
- Designed a **clean dashboard** that shows real-time cluster intelligence.  
- Learned to optimize ML models for **cloud-native deployment**.  
- Contributed reusable YAML + agent code that others can build on.  

---

## What we learned

- The power of **AI + Kubernetes** synergy in cloud-native apps.  
- How **event-driven agents** can replace manual DevOps intervention.  
- Best practices in deploying ML inference services at scale.  
- Importance of **observability (Prometheus, Grafana)** when debugging complex systems.  
- That innovation isn’t just about technology – but about **making clusters more human-friendly**.  

---

## What's next for CubeCortex: The AI Brain for Microservices on Kubernetes

- 🔮 **Expand Agent Library** – Add more domain-specific AI agents (e.g., compliance, cost optimization, energy efficiency).  
- 📦 **Helm Chart for Easy Deployment** – Package CubeCortex for faster adoption.  
- ☁️ **Multi-Cloud Support** – Extend beyond GKE to EKS/AKS.  
- 🤝 **Open Source Community** – Invite contributors to add new AI agent modules.  
- 🧠 **Neural-Orchestrator 2.0** – Research reinforcement learning to enable **self-optimizing microservice meshes**.  

---

## Detailed Architecture

### High-level Design

```mermaid
graph TD
    A[User Requests] --> B[Online Boutique Microservices]
    B --> C[CubeCortex Event Bus]
    C --> D1[Anomaly Detection Agent]
    C --> D2[Recommendation Agent]
    C --> D3[Fraud Detection Agent]
    C --> D4[Support Chat Agent]
    D1 --> E[Dashboard + Alerts]
    D2 --> E
    D3 --> E
    D4 --> E
    E --> F[GKE API Server]
    F --> G[Kubernetes Pods/Nodes]


