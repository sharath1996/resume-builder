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

- **Data sources** The datasets are available in various forms and sources such as AWS, GCP and Sharepoints with different formats.
- **Unified data format** The datasets are then processed and converted to an unified data format and by extracting the meta data.
- **Data Preprocessing** The obtained data is then run through pre-processing pipeline which is responsible for the following
    - Detection of outliers using Interquartlike Range and Local outlier factor techniques.
    - Normalization of the measurement values according to min and max values defined in the datasheets for the respective measurement parameters.
    - Extraction of meta data on the noise figures that are present in the dataset.

### Cell Model

- **PINNS** - Physics informed neural networks are used because of the following:
    - The inputs to the cell model consists various cell parameters such as SoC, Current, Core Temperature, frequency of EIS, Sorrounding Temperature and so on.
    - The output of the cell model are Cell Voltage and Complex cell impedance.
    - Loss functions that are more accurate representation of under-lying electrical systems.
    - We used 3RC models with temperture dependencies to model the underlying physics equations for loss terms.
    - This ensured the accuracy of un-seen datasets that are used for training above the training range of the data.

- **Controlling the inputs**
    - By default the cell model outputs no-noise or no-disturbance data, 
    - Users can use dedicated control vectors, which are passed as time-series data to the controller which can induce the noise or disturbance according to the user inputs.
    - Once, induced the cell measurements will be super-imposed by disturbances creating the noisy or disturbed data which can then be used for testing and developement of BMS Algorithms

### Deployement

- **Continous model update** : The models are periodically trained with the latest data soruces, and each model are checkpointed in JFrog Artifactory.
- **CI/CD and MLOps Integration** : The Integrated models are then evaluated using test-train splits (70-30 split) and then using GitHub actions along with Jenkins to push the successfully trained models to JFrog Artifactory.
- **Latest model usage** : Developed a custom python package which can pull in the latest model that can be used for algorithm developement and testing.
- **Observability** : Along with the training, implemented a custom observability scripts and visualization dashboard on model's performance.

### Data Streaming

- **Battery Pack Simulation** 
    
    - For pack level simulation, we scale the model with multiple inputs and aggregate them together.
    - Each cell in pack can be controlled using various cell parameters using timeseries dataset.

- **Usage in PC enviornments**
    
    - The model weights are stored as .h5 files and are version controlled in JFrog Artifactory
    - All the toolchains such as matlab, simulink, python and any ML libraries which can process .h5 file(s) will be able to use this model seamlessly
    - Additionally for software developement and testing purposes, we have created an internal python packages which can load the model and provide the outputs as time-series data.

- **Usage in hardware environments**
    
    - Since, the BMS Algorithms are run on embedded environments, it is crucical to run and test the algorithms on host controllers or ECUs. 
    - To facilitate these kind of applications and testing, we have a data streaming mechanisms in place.
    - For every period of time, a  timeseries data streaming is done on real-time using TCP communication between PC and embedded environment.
    - A data streamer application is developed using STM32 Nucleo boards to support the real-time battery data streaming.


## System Impact  

### Developer Benefits  
- **Workflow Optimization:** 
    - Engineers need not to worry about the data processing pipelines as we have encapsulated the model with python packages
    - This model can be used in matlab, python and any machine learning tool chains.
    - This gives the freedom for engineers to create test-vectors of multiple cases without worrying much on the data acquisition and clearning aspects.

- **Hardware Reduction:** 
    
    - This simulator can be used to run on complete software environment enabling SIL and PIL testing
    - This simulator can be connected to actual target via data streamer enabling HIL testing.
    - Python package and GUIs enable the users to seamlessly control the cell measurements and enabling faster testing and developement.

## Tools and Technologies  

### **Software Stack**  
- **Programming Languages:** C, Python, Matlab
- **Development Tools:** VSCode, IAR Embedded Workbench, Keil, STM32cubeIDE,Matlab, Simulink, Simscape Electrical,

### **Hardware Platforms**  
- STM32 Nucleo Boards

### **Libraries & Frameworks**  
- TCP, UART, I2C, SPI, Pytorch, Tensorflow, Keras, Numpy, simscape