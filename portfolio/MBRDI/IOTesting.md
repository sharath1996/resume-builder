# IO Testing for Common Powertrain Controller ECUs

Test bench and test-automation for various IOs in Common Powertrain Controller ECUs for Daimler Trucks and Buses

## Overview

- **What is the project all about?**  
  This project aims at creating a test-bench and test-automation of various IOs connected to CPC ECUs of Daimler Trucks and Buses.

- **Project Objectives:**  

  - The primary objective is to achieve the complete testing of IOs including the fault injections without waiting for complete HIL setup.
  - Also, the solution should be modular and compact so that each developers and testers can have individual setups.

## Highlights

- **Various IOs and Simulation strategies**  

  - **General Purpose Inputs and Outputs** : Simulated using digital IOs of ATSAMV71 boards.
  - **Servo motor position input** : Simulated using digital potentiometers and DAC ICs to simulate the various voltages which are mapped to positions.
  - **PWM Inputs** : Simulated using PWM outputs of ATSAMV71Q21 boards.
  - **PWM Outputs** : Captured using PWM inputs of ATSAMV71Q21 boards.
  - **CAN Message Simulation** : Simulation of CAN messages according to the .dbc files.

- **Control strategy** 

  - Built a custom python package to trigger and capture the IO status via test-bench.
  - Test bench consists of a ATSAMv71 board with IO capture and control pins.
  - These pins are then connected to ECU via dedicated IO harness.
  - All the IO controls can be controlled via python package, thus enabling the automation in seamless way.

- **Test Framework**

  - Test framework is developed using CAPL and CANoe
  - Test framework automatically logs the result along with the test-reports.
 
- **Achievements:**  

  - Achieved complete automation of IO controls using python packages and eliminated the need for dedicated HIL setup.

## Impact

- **Developer/Tester Benefits:**  
  - With the help of python packages and compact test-benches developers and testers were able to test the SW Components which accesses the IOs within no time.
  - The setup is very compact and singleboard solution, which fits perfectly with wiring harness of the ECUs, hence it reduces the time and dependencies on complex HIL setups.
  - With the help of python support for Matlab, this also enabled the developers who are used on Model Based developement to quickly control and test the IOs from Matlab.
  

## Tools and Technologies

- **Programming Languages:** C, Python, CAPL
- **Development Tools:** Arduino, Atmel Studio, Keil, Matlab, Simulink, CANape
- **Hardware/Platforms:** ATSAMV71Q21
- **Libraries/Frameworks:** I2C, UART, SPI, CAN, BLE, TCP