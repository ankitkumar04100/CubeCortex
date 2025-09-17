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
8. [Features](#features)  
9. [Built With](#built-with)  
10. [App Status](#app-status)   
11. [Usage](#usage)  
12. [Equations & AI Models](#equations--ai-models)  
13. [Hackathon Story Expansion](#hackathon-story-expansion)  
14. [Roadmap](#roadmap)  
15. [Glossary](#glossary)  
16. [References](#references)
17. [Detailed Architecture](#detailed-architecture) 


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

## Features

- ✅ AI-powered anomaly detection in microservice traffic  
- ✅ Context-aware autoscaling  
- ✅ Fraud detection pipeline  
- ✅ Recommendation engine for customer interactions  
- ✅ AI-powered support chatbot  
- ✅ Interactive dashboard with real-time insights  

---

## Built With

Python, FastAPI, PyTorch, Node.js, Express, React, TailwindCSS, Chart.js, Kubernetes, GKE, Docker, Prometheus, Grafana, Kafka, Pub/Sub, GitHub Actions, Helm  

---

## App Status

**Prototype / Beta** – Core functionality is working, with scope for future expansion.  

---

## 12. Usage

Once CubeCortex is deployed, developers and operators can interact with the system as if they are managing a "thinking Kubernetes cluster."  

### Steps to Use:
1. **Access the Dashboard**  
   - Retrieve the LoadBalancer IP from GKE.  
   - Open it in the browser to view real-time health, alerts, and AI-driven recommendations.  

2. **Run Load Tests**  
   - Use tools like `Locust` or `k6` to simulate user traffic.  
   - Observe CubeCortex agents adaptively scaling services and detecting anomalies.  

3. **Interact with Agents**  
   - Send simulated API calls for fraud detection or recommendations.  
   - Use the AI-powered chatbot agent for support simulation.  

4. **Monitor Logs & Metrics**  
   - View agent logs in Kubernetes:  
     ```bash
     kubectl logs <agent-pod-name>
     ```
   - Metrics available through **Prometheus + Grafana dashboards**.  

CubeCortex effectively transforms microservice operations from **manual DevOps intervention** to **autonomous AI-driven orchestration**.  

---

## 13. Equations & AI Models

CubeCortex integrates mathematical and machine learning models to make predictions and decisions.  

### 🔍 Anomaly Detection (Autoencoder Loss Function)
We trained autoencoders on normal microservice traffic. Any significant deviation is flagged as an anomaly.  

\[
L(x,\hat{x}) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{x}_i)^2
\]

Where:  
- \( x \) = input (observed traffic pattern)  
- \( \hat{x} \) = reconstructed (predicted normal pattern)  

---

### 📈 Load Prediction (ARIMA / Time Series)
Used to forecast demand and scale pods **before spikes occur**.  

\[
y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + ... + \epsilon_t
\]

Where:  
- \( y_t \) = predicted load at time *t*  
- \( \phi \) = autoregressive parameters  
- \( \epsilon_t \) = error term  

---

### 🎯 Recommendation Scoring (Dot Product Similarity)
Used in the **Recommendation Agent** for customer/product personalization.  

\[
Score(u, i) = \vec{U}_u \cdot \vec{I}_i
\]

Where:  
- \( \vec{U}_u \) = user feature vector  
- \( \vec{I}_i \) = item/service feature vector  

---

## 14. Hackathon Story Expansion

### 💡 Inspiration
We wanted to bridge **Kubernetes reliability** with **AI adaptability**. Like a brain, CubeCortex uses agents as "neurons," analyzing signals and making corrective actions.  

### 🛠️ What it does
CubeCortex upgrades an existing **Online Boutique microservice app** with:  
- Real-time anomaly detection  
- AI-driven autoscaling  
- Fraud prevention pipelines  
- Recommendation systems  
- AI chatbot for customer support  

### ⚙️ How we built it
- Deployed **Online Boutique** on **GKE**.  
- Built AI agents in **Python (FastAPI, PyTorch)** and **Node.js**.  
- Integrated **Kafka** as the event bus.  
- Connected metrics pipelines with **Prometheus + Grafana**.  
- Developed an interactive **React + Tailwind dashboard**.  

### 🚧 Challenges
- Handling **real-time inference latency**.  
- Preventing **AI over-control** of Kubernetes.  
- Simulating **realistic fraud/traffic data** for training.  
- Hackathon **time constraints** with ambitious scope.  

### 🏆 Accomplishments
- A **working prototype** where AI agents act like neurons orchestrating microservices.  
- Built reusable **Helm charts & manifests**.  
- Delivered an **intuitive dashboard** for non-experts.  

---

## 15. Roadmap

- 📦 **Helm Chart Release** – Package CubeCortex for simple installs.  
- 🧠 **Reinforcement Learning Agents** – Self-optimizing microservices orchestration.  
- 🔒 **Security Agents** – Detect and mitigate zero-day attacks.  
- ☁️ **Multi-cloud Expansion** – Deployable on AWS EKS & Azure AKS.  
- 🌍 **Sustainability** – Energy-efficient autoscaling with carbon-aware scheduling.  
- 🤝 **Community Contributions** – Open-source modules for new AI agents.  

---

## 16. Glossary

- **GKE** – Google Kubernetes Engine; managed Kubernetes service.  
- **Microservices** – Independent, loosely coupled services working together.  
- **AI Agent** – A specialized service that makes autonomous decisions using ML.  
- **Autoscaling** – Dynamic adjustment of pods based on workload demand.  
- **Event Bus** – Middleware for decoupled communication (Kafka / PubSub).  
- **Anomaly Detection** – Identifying unusual behavior deviating from the baseline.  

---

## 17. References

- [Google Cloud Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo)  
- [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos)  
- [Kubernetes Documentation](https://kubernetes.io/docs)  
- [GKE Turns 10 Hackathon – Official Portal](https://gkehacks.devpost.com)  

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


