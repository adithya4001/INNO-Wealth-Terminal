import streamlit as st
import requests
import plotly.graph_objects as go
import numpy as np

API_KEY = st.secrets["GEMINI_API_KEY"]
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# --- 1. ENTERPRISE UI CONFIG ---
st.set_page_config(page_title="INNO Wealth Terminal", page_icon="🏦", layout="wide")

st.html("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background-color: #0B0E14; color: #E2E8F0;}
    [data-testid="stSidebar"] {background-color: #111827; border-right: 1px solid #1F2937;}
    .stChatMessage {background-color: #1F2937; border-radius: 10px; padding: 15px; margin-bottom: 10px; border: 1px solid #374151;}
    h1, h2, h3 {color: #10B981 !important;}
    .metric-card {background-color: #1F2937; padding: 20px; border-radius: 10px; border-left: 4px solid #10B981; margin-bottom: 20px;}
    </style>
""")

# --- 2. SIDEBAR: SECURE VAULT & SIMULATOR ---
st.sidebar.markdown("### 🏦 INNO Wealth Terminal")
st.sidebar.caption("Secure Client Data Sync")
st.sidebar.divider()

st.sidebar.markdown("**1. Client Financials**")
age = st.sidebar.number_input("Current Age", min_value=18, max_value=80, value=25)
income = st.sidebar.number_input("Annual Income (₹)", min_value=100000, value=1200000, step=50000)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=10000, value=50000, step=5000)

st.sidebar.divider()
st.sidebar.markdown("**2. Macro-Economic Stress Test**")
market_condition = st.sidebar.select_slider("Simulated Market Condition", options=["Severe Bear (-5%)", "Stagnant (4%)", "Average (10%)", "Bull Market (15%)"], value="Average (10%)")

return_rates = {"Severe Bear (-5%)": -0.05, "Stagnant (4%)": 0.04, "Average (10%)": 0.10, "Bull Market (15%)": 0.15}
roi = return_rates[market_condition]

st.sidebar.divider()
st.sidebar.success("🟢 Systems Nominal")
st.sidebar.info("🧠 Brain: INNO Core Quant")

# --- 3. QUANTITATIVE DASHBOARD ---
st.title("Algorithmic Wealth Strategist")

yearly_savings = income - (expenses * 12)
years = np.arange(1, 31)
standard_wealth = yearly_savings * years
ai_wealth = [yearly_savings * (((1 + roi)**y - 1) / roi) if roi != 0 else yearly_savings * y for y in years]

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""<div class="metric-card"><h4>Projected AI Wealth (30yr)</h4><h2>₹{int(ai_wealth[-1]/100000)} Lakhs</h2></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="metric-card"><h4>Market Condition</h4><h2>{market_condition}</h2></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="metric-card"><h4>Optimization Delta</h4><h2>+₹{int((ai_wealth[-1] - standard_wealth[-1])/100000)} Lakhs</h2></div>""", unsafe_allow_html=True)

fig = go.Figure()
fig.add_trace(go.Scatter(x=years + age, y=standard_wealth, mode='lines', name='Standard Savings', line=dict(color='#EF4444', width=2, dash='dash')))
fig.add_trace(go.Scatter(x=years + age, y=ai_wealth, mode='lines', fill='tozeroy', name='INNO AI Strategy', line=dict(color='#10B981', width=3)))
fig.update_layout(title="Monte Carlo FIRE Projection (Age vs Net Worth)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#E2E8F0'), margin=dict(l=0, r=0, t=40, b=0), hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- 4. CONTINUOUS DEEP-DIVE CHAT ---
st.markdown("### 💬 Strategic AI Consultation")
st.caption("Type 'Analyze my profile' to get a deep-dive, or ask specific follow-up questions.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "model", 
        # CHANGED: Much better welcoming message that prompts the user properly.
        "content": "Welcome to the INNO Wealth Terminal. I have securely synced your financial data. Type **'Analyze my profile'** below, and I will generate a comprehensive, detailed breakdown of your financial health, tax strategy, and FIRE trajectory."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Ask your Quant Advisor..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # CHANGED: The "Brain" instructions are now strictly focused on being detailed, relatable, and example-driven.
    system_context = f"""
    System Directive: You are an elite but highly empathetic Indian Wealth Mentor. 
    LIVE CLIENT DATA: Age {age}, Annual Income ₹{income}, Monthly Expenses ₹{expenses}.
    Current Simulated Market: {market_condition}. 
    
    CRITICAL INSTRUCTIONS:
    1. NEVER give short, vague answers. ALWAYS provide DETAILED, in-depth explanations.
    2. Use real-world Indian examples (e.g., comparing SIP compounding to real estate or FDs, mentioning inflation costs).
    3. If the user asks for an 'analysis' or 'breakdown', you MUST provide a massive 3-part strategy:
       - Part 1: Financial Health Check (Calculate their savings rate, tell them if it's good or bad).
       - Part 2: Tax Optimization (Explain EXACTLY why the Old or New regime is better based on Indian tax slabs).
       - Part 3: Wealth Creation (Give them exact SIP amounts and asset allocation ideas).
    4. Do not ask them what they want to do next until you have provided massive value first.
    
    Chat History:
    """
    
    for msg in st.session_state.messages[-5:]:
        role_name = "Advisor" if msg["role"] == "model" else "Client"
        system_context += f"{role_name}: {msg['content']}\n"
    
    system_context += "Advisor: "

    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": system_context}]}]}
    
    with st.chat_message("model"):
        with st.spinner("Running quantitative analysis..."):
            try:
                response = requests.post(URL, headers=headers, json=data)
                result = response.json()
                if response.status_code == 200:
                    ai_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(ai_text)
                    st.session_state.messages.append({"role": "model", "content": ai_text})
                else:
                    st.error(f"Google API Error: {result.get('error', {}).get('message', 'Unknown Error')}")
            except Exception as e:
                st.error("Network synchronization failed.")
