# INNO-Wealth-Terminal

In India, quantitative advice for high-end finances has traditionally been available only to High Net Worth Individuals (HNIs). Young professionals in the country lose hundreds of thousands of rupees every year because of an inefficient tax environment, inflation, and poor portfolio management caused by the absence of continuous financial counseling.

Our solution to this problem is INNO Wealth Terminal, which offers democratic access to quantitative finance management. We have designed a novel hybrid approach by coupling a deterministic macroeconomic modeler with a generative AI-driven cognitive interface with memory retention. It is neither a fixed document nor just another generic chatbot but a living memory-rich financial counselor which recalculates 30-year financial independence plans, taxes optimization, and life event planning.

FIRE Path Planner: 
Generates a 30-year Monte Carlo analysis plan comparing traditional cash savings and optimal SIP investments via AI, plotted using Plotly dashboards.

Money Health Score: 
Conducts an "instant" Financial Health Check and analyzes savings rates, cash deficit in emergency funds, and investment portfolio efficiency.

Tax Wizard: 
Uses mathematical calculation of India's Old vs. New Tax Regime to optimize your local taxation by considering different brackets of incomes.

Life Event Advisor: 
Maintains conversation context. Enter a life event (e.g., "Got married and received a ₹5L bonus"), and immediately receive an updated strategy overview.

Architecture & Innovation:
The real game-changer of the INNO Wealth Terminal is the disconnection between Deterministic Math Engine and Generative Reasoning Module. Compounding calculations run in Python, and strategy reasoning is done by Google Gemini LLM.


Tech Stack Utilized:

Frontend/UI: 
Streamlit with custom CSS (Dark Mode/Bloomberg-style terminal).

Data Visualizations:
Plotly Go (Interactive, zero reload graphs).

Deterministic Math Engine: 
NumPy & Pandas (Instant computation for 30-year compounding arrays).

Large Language Model Engine: 
Google Gemini 2.5 (Used due to its large context window size and low-latency reasoning).

Uniqueness Factors:
Macro Economic Stress Testing: 30-year simulations with severe Bear (-5%) or Bull (+15%) market environments using the live slider feature.

Stateful Conversational Capability: 
The user can contest the calculation, ask "Why" or change their mind midstream.

Strict Persona Construction: 
Gemini is strongly encouraged to play his role of the best quant analyst from India with localized structured plans (SIPs, FDs, tax brackets), rather than giving general tips.

Effect on Business:
For testing the accuracy of the model while abiding by privacy policy, a simulated model was built based on Log-Normal distribution in the form of a Python Economic Monte Carlo simulation with 50 Indian middle class working individuals.
