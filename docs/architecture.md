# CubeCortex – Architecture Diagram

This document explains the high-level architecture of **CubeCortex: The AI Brain for Microservices on Kubernetes**.

---

## High-Level Architecture

![Architecture Diagram](./architecture.png)

---

## Mermaid Source (Editable)

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
