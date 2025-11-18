## Real-Time Options Trading Engine
Author: Jnandeep Dev Sarma

Contact: jnandeepdevsarma@gmail.com

# Project Summary

A high-performance automated options execution system built for disciplined, speed-critical derivatives trading.
The engine integrates real-time market feeds, autonomous strike selection, Greeks-based risk modeling, volatility-aware trade execution, and a strict safety framework that prevents emotional/manual errors.

This project showcases professional-grade architecture, production-ready engineering, and deep domain expertise across trading, automation, and system design.

# Core Highlights

1. Automated Real-Time Execution

- Built fully in Python using multi-threading + websocket-driven price feeds.
- Reacts to live market conditions within milliseconds.
- Automatically executes CE/PE trades based on validated breakout/reversal signals.
- Supports iceberg order slicing, smart BO/TSL placement, and dynamic SL/TP recalibration.

2. Dynamic Risk Engine
- Computes optimal position size using:
- Capital allocation %
- Max loss cap
- RR ratio
- Target profit %
- SL/TP levels are derived using Greeks (Delta/Gamma etc) and historical volatility.
- Automatically adjusts SL/TP during event-driven volatility spikes.

3. Autonomous Strike Selection
- Evaluates CE/PE strikes using:
- Greeks (Δ, Γ, Θ)
- IV pockets
- Volatility zones
- Liquidity filters
- Picks the best strike dynamically before execution.

4. Safety & Discipline Framework
Prevents:
- SL tampering
- Emotional overrides
- Revenge trading
- Hard-coded risk boundaries enforce trader discipline.

5. Full GUI for Control
Tkinter-based dashboard includes:
- Live price/Greece panel
- Execution toggle
- Capital & risk settings
- Trade logs and diagnostics
- Built for clarity and quick interaction during live sessions.

6. Modular Architecture
Each subsystem is isolated for clean testing, debugging, and scaling:
- Signal Engine
- Strike Selector
- Risk Engine
- Safety Framework
- Execution Layer
- GUI Layer
- Logging/Monitoring Layer

# Repository Structure

```bash
real-time-options-trading-engine/
│
├─ README.md
├─ 01_Live_Execution_Demo.pdf
├─ 02_Risk_Engine_Overview.pdf
│
├─ docs/
│   ├─ architecture_diagram.png
│   ├─ data_flow_diagram.png
│   ├─ strike_selection_logic.pdf
│   └─ safety_framework_rules.pdf
│
├─ sample_data/
│   ├─ sanitized_tick_stream.csv
│   ├─ sanitized_option_chain.csv
│   └─ sanitized_greeks_feed.csv
│
├─ code_snippets/
│   ├─ execution_layer_example.py
│   ├─ strike_selection_example.py
│   ├─ gui_sample.py
│   ├─ safety_framework_example.py
│   ├─ requirements.txt
│   └─ config_sample.yaml
│
├─ gui_screenshots/
│   ├─ dashboard_live.png
│   └─ risk_panel.png
│
└─ videos/
    └─ live_execution_demo.mp4
```

# Architecture Diagram (Text-Based)

 ```mermaid
---
config:
  theme: "redux-dark"
---
flowchart TD

    A["Live Websocket Feed<br/>(Price + Greeks Data)"]
    A --> B["Market Data Processor<br/>(Tick + Greeks Handler)"]

    %% Split into two engines
    B --> C["Signal Engine<br/>- S/R breaks<br/>- Reversals"]
    B --> D["Strike Selection Engine<br/>- CE/PE scoring<br/>- OI/Greeks filters"]

    %% Merge paths
    C --> E["Risk Engine<br/>- SL/TP (Greeks-based)<br/>- Capital allocation<br/>- RR + Max-loss logic"]
    D --> E

    E --> F["Safety Framework<br/>- Cooldown timer<br/>- SL tamper prevention<br/>- Runaway trade lockout"]

    F --> G["Execution Layer<br/>- Iceberg slicing<br/>- BO/TSL automation<br/>- Order verification"]

    G --> H["Broker API"]

    H --> I["Logging & Monitoring<br/>GUI + CSV + Console Logs"]
```

# Documentation Included


Inside the /docs folder:

architecture_diagram.png
- Complete visual architecture of the entire pipeline.

data_flow_diagram.png
- Step-by-step flow from realtime feed → engine → execution → logs.

strike_selection_logic.pdf
- Math + logic behind selecting the right CE/PE strike.

safety_framework_rules.pdf
- All trading discipline rules implemented internally.

# Sample Data Provided

sanitized_tick_stream.csv
- Sample websocket tick data used for backtesting engine behavior.

sanitized_option_chain.csv
- Sample CE/PE chain with LTP, bid, ask, OI data.

sanitized_greeks_feed.csv
- Delta, Gamma, Theta data used in Greek-based SL/TP logic.

# Code Snippets

execution_layer_example.py
- Order placement + iceberg slicing + safety + risk checks.

strike_selection_example.py
- CE/PE selection logic using volatility + Greeks.

gui_sample.py
- Tkinter UI demonstrating live engine monitoring.

safety_framework_example.py
- Implementation of FOMO blocks, cooldowns, lockouts.

requirements.txt
- Dependencies (Fyers API, Pandas, Numpy, Tkinter, etc.)

config_sample.yaml
- Editable parameters for full engine customization.

# Screenshots & Videos

Inside /gui_screenshots and /videos:
- Real live dashboard
- Order flow windows
- Risk panel
- Demo videos showing the engine running in real time
