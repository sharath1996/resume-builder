# Static Multicore Scheduler for Daimler Trucks Electric Powertrain Controller ECUs

Static OS scheduler to efficiently manage software components across multi-core eCPC ECUs for Daimler Trucks.

## Overview

- **What is the project all about?**  
  This project involves the development of a static OS scheduler that optimizes the execution of various software components on multi-core eCPC ECUs in Daimler Trucks.

- **Project Objectives:**  

  - Minimize wait times and achieve parallelism by analyzing dependencies and execution times of software components.  
  - Generate a robust, MISRA-compliant scheduler code, ensuring reduced deadlocks and effective multi-core utilization.  

## Highlights

- **Dependency Analysis and Execution Time Measurement:**  

  - **Shared Variables Mapping:** Used map files to allocate shared variables into dedicated memory sections.  
  - **Consumers and Producers Mapping:** Created dependency graphs based on producers and consumers of shared variables.  
  - **Execution Time Estimation:** Measured average and maximum execution times of software components using Vector timing architect and data from previous schedulers.  

- **Graph-Based Scheduling and Automation:**  

  - **Dependency Graph:** Developed a graph representation of execution sequences to reduce wait times and prevent deadlocks.  
  - **Visualization:** Used the yED tool for graph visualization, enabling developers to make adjustments interactively.  
  - **Code Generation:** Parsed the graph to generate MISRA-compliant C code for the scheduler, complete with Polyspace checks and unit-test code to meet MCDC and code-coverage standards.  

- **Advanced Optimization Techniques:**  

  - Applied reinforcement learning and graph reduction techniques to expedite the scheduling process, improving efficiency for developers.  

## Impact

- **Developer/Tester Benefits:**  

  - Automated generation of optimized scheduling code, eliminating manual dependency tracking.  
  - Reduced development time through advanced tools and techniques for visualization and automation.  
  - Ensured robustness of generated scheduler code via strict adherence to guidelines (MISRA, Polyspace, etc.).  

## Tools and Technologies

- **Programming Languages:** C, Python  
- **Development Tools:** Arduino, Atmel Studio, Keil, Matlab, Simulink, CANape, CANoe  
- **Hardware/Platforms:** ATSAMV71Q21  
- **Libraries/Frameworks:** I2C, UART, SPI, CAN, BLE, TCP