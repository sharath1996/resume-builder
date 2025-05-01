# Protocol Simulators for BMS and wBMS  

## Overview  

### Purpose  

Accelerate software development and testing by eliminating dependencies on hardware availability for feature developement and validations.  

### Core Concept  

- **Wired BMS Simulation:** Models interactions between the host controller and daisy-chained SPI-based Battery Monitoring ICs (BMICs). Simulates real-time cell voltage, temperature, and diagnostic measurements to validate system behavior.  
- **Wireless BMS Simulation:** Emulates interactions between network managers and the host controller, incorporating cell measurement simulations and fault injection for wireless communication protocols.  
- **Test-Vector Generation:** Provides engineers with controlled test environments for protocol validation without requiring complex physical setups.  

## Technical Highlights  

### Wired BMS  

- **Multi-Device Simulation:** Supports up to 20 functionally safe BMICs with real-time measurement simulations.  
- **Hardware-In-the-Loop Interactions:** Enables controlled cell voltage, temperature, and pack current adjustments through MODBUS protocol over a PC interface.  
- **Dedicated Processing Unit:** Executed on dual-core STM32MF4 MCUs, ensuring performance isolation for real-time simulations.  
- **Fault Injection Framework:** Replicates fault scenarios as defined in BMIC safety manuals to enable rigorous validation of error-handling mechanisms.  

### Wireless BMS  

- **Network Virtualization:** Simulates wireless mesh networks with up to 50 nodes.  
- **Performance Metrics:** Models key communication parameters such as Packet Delivery Ratio (PDR) and Received Signal Strength Indicator (RSSI) for every device pair.  
- **Fault Simulation:** Implements network failures and degradation patterns conforming to ISO 26262 communication protocol standards.  
- **Hardware Abstraction Layer (HAL) Compatibility:** Designed as modular C libraries, enabling execution across diverse hardware targets such as ATSAMv71Q21B, ADRF8xx devices, and PC-based simulations.  
- **Automated Testing:** Python-based configuration utilities facilitate controlled fault injection scenarios for both BMICs and network communications.  

## Key Performance Indicators (KPIs)  

### **Scalability & Performance Metrics**  
- **System Load Handling Capacity**: Measure the number of simultaneous simulations supported without performance degradation.  
- **Simulation Execution Speed**: Time required to complete a full cycle of test case execution for wired and wireless BMS.  
- **Latency in Response Time**: Evaluate how quickly the simulator responds to configuration changes and fault injections.  

### **Accuracy & Validation Metrics**  
- **Simulation Fidelity**: Percentage of simulated data accuracy compared to real hardware measurements.  
- **Fault Injection Precision**: Success rate of induced faults correctly replicating real-world failure modes.  
- **Protocol Conformance Rate**: Alignment of simulated communications with ISO 26262 and BMIC safety manual specifications.  

### **Efficiency & Development Impact**  
- **Hardware Reduction Factor**: Quantify the reduction in physical hardware required for testing (e.g., 24 boards → 1 board for wired BMS).  
- **Setup Time Savings**: Reduction in time needed for engineers to configure testing environments compared to real hardware setups.  
- **Debugging Efficiency**: Measure time savings in troubleshooting network and hardware issues using the simulator vs. physical boards.  

### **Adoption & Usability Metrics**  
- **User Adoption Rate**: Track the percentage of engineering teams actively using the simulator for development and testing.  
- **Feedback Implementation Rate**: Percentage of user feedback incorporated into simulator updates.  
- **Training Time for Engineers**: Average time required for engineers to become proficient in using the simulator effectively.  

### **Reliability & System Robustness**  
- **Simulator Uptime**: Percentage of time the system runs without failures or crashes.  
- **Error Rate in Test Execution**: Measure cases where the simulation results diverge from expected outcomes.  
- **Data Integrity and Security Compliance**: Evaluate how well decentralized databases handle secure access control and prevent unauthorized data leaks.  

### **Impact on Product Development**  
- **Time-to-Market Reduction**: Quantify how much simulator usage accelerates the delivery of new software features.  
- **Inter-Team Collaboration Metrics**: Track improvements in the interaction between software and hardware engineering teams using simulation-driven workflows.  
- **Customer Feedback Incorporation Rate**: Measure how quickly early feedback loops influence product development cycles.  

## System Impact  

### Developer Benefits  

- **Optimized Development Workflow:** Eliminates hardware dependencies, allowing algorithm and protocol validation without physical setup.  
- **Hardware Reduction:** Consolidates extensive hardware requirements—replacing 24 physical boards with a single simulation unit for wired BMS and reducing 34 boards to one for wireless BMS testing.  
- **Efficient Debugging:** Mitigates setup complexities related to power supply configurations and interconnections.  
- **Comprehensive Fault Testing:** Introduces fault injection mechanisms unavailable in standard hardware, improving overall test coverage.  
- **Accelerated Product Delivery:** Reduces development cycles and time-to-market for software-defined battery management solutions.  
- **Cross-Disciplinary Collaboration:** Enables seamless synchronization between software and hardware design teams, minimizing design iterations and silicon tapeouts.  
- **Customer-Centric Development:** Provides early product feedback loops through engineering collaboration across teams and stakeholders.  

## Tools and Technologies  

### **Software Stack**  
- **Programming Languages:** C, Python  
- **Development Tools:** STM32Cube IDE, IAR Workbench, VSCode, Keil  

### **Hardware Platforms**  
- STM32F407, ADRF8xxx, ATSAMv71Q21B, PC-based simulators  

### **Libraries & Frameworks**  
- Streamlit, MODBUS, CAN, UART  
