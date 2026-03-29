# INNO-Wealth-Terminal
Executive Summary
In India, elite quantitative financial advisory is historically restricted to High-Net-Worth Individuals (HNIs). The average young professional leaks lakhs of rupees annually to inefficient tax regimes, inflation, and poor asset allocation due to a lack of affordable, continuous financial guidance.

INNO Wealth Terminal solves this by democratizing quantitative wealth management. We engineered a hybrid system combining a deterministic macro-economic modelling engine with a continuous, stateful Generative AI cognitive interface. It is not a static form or a generic chatbot—it is a dynamic, memory-retaining financial strategist that recalculates 30-year FIRE trajectories, optimizes taxes, and adapts to life events in real-time.

Key Features (Hackathon Objectives Achieved)
FIRE Path Planner: Calculates a 30-year Monte Carlo trajectory comparing standard cash hoarding against AI-optimized SIP routing, visualized via interactive Plotly dashboards.

Money Health Score: Executes an instant "Financial Health Check," calculating savings rates, emergency fund deficits, and portfolio health based on live inputs.

Tax Wizard: Mathematically compares the Indian Old vs. New Tax Regimes based on specific income brackets to output a localized optimization strategy minimizing tax drag.

Life Event Advisor: Retains conversational context. Inject life events dynamically (e.g., "I just got married and got a ₹5L bonus"), and the AI instantly recalculates the overarching strategy.

System Architecture & Innovation:
The true innovation of the INNO Wealth Terminal is the separation of Deterministic Math and Generative Reasoning. We use a Python engine for the heavy lifting of compounding math, and Google Gemini for strategic reasoning.
Technology Stack
Frontend/UI: Streamlit with custom CSS (Dark-mode Bloomberg-style terminal).

Data Visualization: Plotly Graph Objects (Interactive, no-reload rendering).

Mathematical Engine: NumPy & Pandas (Handles 30-year compounding arrays instantly).

LLM Integration: Google Gemini 2.5 Flash via REST API (Chosen for massive context window, near-zero latency, and superior reasoning).

What Makes It Unique?:
Macro-Economic Stress Testing: Simulates 30-year trajectories under Severe Bear (-5%) or Bull (+15%) markets using a live slider.

Stateful Conversational Memory: Users can challenge the math, ask "Why?", or pivot their strategy without losing context.

Strict Persona Engineering: Gemini is heavily prompted to act as an elite Indian quant analyst, delivering structured, localized blueprints (SIPs, FDs, tax brackets) instead of generic advice.

Business Impact:
To validate the model while maintaining privacy compliance, we engineered a Python-based Monte Carlo Economic Simulation Model using Log-Normal distributions to create a synthetic dataset of 50 Indian middle-class professionals.

The Impact Analytics (via Power BI):

Identified Leakage: Discovered ₹2.22 Million in immediate, actionable tax savings simply by autonomously routing users to their mathematically optimal tax regime.

Market Scale: Can serve as a foundational advisory layer for neo-banks or brokerages (Zerodha, Groww), delivering hyper-personalized financial literacy at zero marginal cost.
