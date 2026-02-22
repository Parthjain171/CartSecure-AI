# 🛒 CartSecure AI
### Intelligent Retail Object Detection & Behavior Monitoring System

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Framework](https://img.shields.io/badge/FastAPI-API-green)
![Model](https://img.shields.io/badge/YOLOv8-ObjectDetection-red)
![Status](https://img.shields.io/badge/Status-Active-success)

CartSecure AI is a real-time computer vision system designed to enhance retail surveillance through advanced object detection and extensible behavior analysis capabilities.

Built using **YOLOv8** and **FastAPI**, the system detects retail-related objects from images and provides structured, production-ready JSON responses. The architecture is modular and intentionally designed to serve as a scalable foundation for advanced retail theft behavior analytics.

---

## 🚀 Project Vision

Modern retail environments require intelligent monitoring systems that can:

- Reduce inventory shrinkage
- Improve operational visibility
- Detect potentially suspicious activity
- Enable data-driven surveillance workflows

CartSecure AI provides the detection backbone required to power such intelligent retail systems.

---

## 🧠 Core Capabilities

### 🔍 1. Real-Time Object Detection

- Person detection
- Cart detection
- Bag detection
- Product detection
- Bounding box localization
- Confidence scoring
- Structured JSON outputs

Powered by **YOLOv8** for high-performance inference and optimized API integration.

---

### 🛒 2. Retail Scene Context Modeling

The system extracts structured information from retail scenes to enable higher-level analytics:

- Customer presence tracking
- Object proximity relationships
- Item-to-cart association
- Product interaction signals

This detection layer serves as the foundation for building behavior-aware retail systems.

---

### ⚠️ 3. Theft Behavior Analysis (Architectural Foundation)

While YOLO performs object detection, CartSecure AI is architected to support behavioral analytics through a modular expansion layer.

The system is designed to enable:

- Temporal interaction tracking
- Object disappearance logic (item no longer visible after interaction)
- Proximity-based monitoring
- Suspicious pattern flagging via rule-based logic

The current implementation provides the **detection backbone** required for:

- Concealment detection
- Loitering detection
- Item abandonment analysis
- Cart misuse monitoring

Behavior analytics can be extended by integrating multi-object tracking systems (e.g., DeepSORT or ByteTrack) and temporal reasoning modules.

This ensures the project remains:

- Technically accurate
- Architecturally scalable
- Industry-aligned
- Extensible without redesign

---

## 🏗️ Architecture Overview

```text
                ┌───────────────┐
                │    Client     │
                │ (Image Upload)│
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │   FastAPI     │
                │  REST Layer   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │  YOLOv8 Model │
                │  Inference    │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │ JSON Response │
                │ (Detections)  │
                └───────────────┘
