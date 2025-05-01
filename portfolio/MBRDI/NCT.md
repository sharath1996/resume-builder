# Network Conformance Testing

Test bench and test-automation for In Vehicle Communication of Powertrain network for Daimler Trucks and Buses

## Overview

- **What is the project all about?**  
  This project aims at creating a test-bench and test-automation for In-Vehicle Communication of Powertrain CAN network for Daimler Trucks and Buses

- **Project Objectives:**  

  - The primary objective is to achieve the complete testing of Network conformance Testing of Powertain CAN network.
  - The powertrain CAN network consists of multiple ECUs depending on the vehicle configuration and type of vehicle.

## Highlights

- **Simulation of Network for single ECUs**
  
  - As a initial approach, we simulate the messages from various other ECUs in the network, apart from the DUT in the network.
  - This approach will enable seamless testing of NCT of the ECUs in the network.
  - The test-automation is done using CAPL scripting.

- **Simulataneos testing of all networks**

  - This approach will help to perform the NCT (Network Conformance Tests) all the ECUs within the network.
  - Dedicated CAPL scripts are written to perform the NCT for each ECU in the network.
 
- **Achievements:**  

  - Achieved complete automation of NCT using CAPL scripting for 10 ECUs in 6 different configuraitons.
  - Created these as part of Jenkins pipeline for CI/CD integrations
  - Created a dedicated control circuit for power controlling of ECUs.
  

## Tools and Technologies

- **Programming Languages:** C, Python, CAPL
- **Development Tools:** Arduino, Atmel Studio, Keil, Matlab, Simulink 
- **Hardware/Platforms:** ATSAMV71Q21
- **Libraries/Frameworks:** I2C, UART, SPI, CAN, BLE, TCP