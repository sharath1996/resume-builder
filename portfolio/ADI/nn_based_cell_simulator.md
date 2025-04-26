# Cell Models using Physics Informed Neural networks

## Overview

### Purpose  

Data generator for battery algorithms and insights based  on EIS (Electro Impedance Spectroscopy) measurements for developement and testing

### Core Concept  
- **Aggregation of multiple data sources** : The measurement data comes from multiple sources such as lab measurments, simulated measurements, vehicle measurements and so on, we need to create a model or generator which can generate the EIS measurements for the given scenario and add disturbances in c controlled manner.
- **Physics informed Neural Network** : As compared to traditional neural network, we use Physics informed neural network, this ensures the output of the model produces valid output even for the regions that the models are not trained, this approach helps in generating the valid data points that are impossible to get in real-world measurements.
- **Faster simulation and hybrid deployment** : This approach also enabled us to dump the model into embedded devices using the libraries such as tensorflow lite and for the targets, which does not support tensorflow lite, we created a TCP socket communication channel which will enable us to get the data running from PC in real-time and feed into the BMS controller. This acts like the data is appearing from the actual hardware rather than the simulation system. 


## Technical Highlights  

### Data Collection pipeline
-   
- **Feature 2:** _Explain how it works and integrates with the system._  
- **Feature 3:** _Mention performance optimizations or constraints._  

### Physics Informed Neural Network

- **Feature 1:** _Describe the simulated or implemented aspect._  
- **Feature 2:** _Highlight how it enhances functionality._  
- **Feature 3:** _Include any standards or protocols it follows._  

### Deployement

- 
- 

## System Impact  

### Developer Benefits  
- **Workflow Optimization:** _Describe how engineers benefit._  
- **Hardware Reduction:** _Explain cost and complexity savings._  
- **Comprehensive Fault Testing:** _Highlight how validation is improved._  
- **Accelerated Product Delivery:** _Explain overall efficiency gains._  

## Tools and Technologies  

### **Software Stack**  
- **Programming Languages:** _List the key languages used._  
- **Development Tools:** _Mention IDEs, compilers, and related tools._  

### **Hardware Platforms**  
- _List any hardware or embedded systems involved._  

### **Libraries & Frameworks**  
- _Include relevant frameworks or APIs used._  