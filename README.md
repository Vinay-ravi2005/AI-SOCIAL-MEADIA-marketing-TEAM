# Autonomous Multi-Agent Social Media Marketing Team Orchestrator

An enterprise-ready architectural prototype implementing an autonomous Agentic AI framework. The system splits abstract creative brand conceptualization into decoupled sub-problems assigned to dedicated Software Agents, compiled via a top-down Central Orchestrator.

## 🧠 Core System Architecture

Instead of standard rigid sequential programming, this system utilizes a distributed problem-solving layout:

1. **Central Workflow Orchestrator:** Acts as the supervisor system controller. It receives structural context parameters, schedules down-stream thread workloads, passes relational database payloads between agents, and manages error boundaries.
2. **Market Analyst Agent:** Specialized in contextual token grouping. It maps descriptive brand parameters against integrated keyword matrices to extract user intent and generate targeting profiles.
3. **Copywriter Agent:** Handles natural language formatting. It dynamically builds multi-channel string logs customized for distinct target networks (Instagram, X, LinkedIn) utilizing context data produced by Phase 1.
4. **Design Prompt Agent:** A text-to-vision mapping module. It extracts contextual brand semantic themes and maps them into descriptive hyper-detailed prompt matrices engineered for stable-diffusion visual pipelines.

## 🛠️ Local Deployment Guide

Follow these simple instructions to launch the application stack locally inside Visual Studio Code:

1. **Open Workspace Workspace**
   Launch VS Code, select `File > Open Folder`, and open this root directory.

2. **Establish Environment & Packages**
   Open the integrated VS Code terminal (`Ctrl + ~`) and install the pinned system requirements:
   ```bash
   pip install -r requirements.txt