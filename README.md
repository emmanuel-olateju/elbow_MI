# elbow_MI

Stroke Motor-Imagery [Dataset](https://figshare.com/articles/dataset/EEG_datasets_of_stroke_patients/21679035/5)

Article [Link](https://www.nature.com/articles/s41597-023-02787-8)


## Pipeline
```mermaid
graph TD
A[Channel-Wise <br/> Epochs Detrending] 
B1[STFT Spectrogram <br/> Computation]
B2[8-30 Hz <br/> STFT Extraction]
B3[Min-Max Scaling <br/> STFT Epochs]
C1[Channel Selection <br/> C3, C4, Cz]
C2[STFT <br/> Bipolar Rereferencing <br/> C3, C4, Cz]
C3[Other Spatial <br/> Alternatives]

D[Feature Engineering]

A --> B1 --> B2 --> B3 --> C1
A --> B1 --> B2 --> B3 --> C2
A --> B1 --> B2 --> B3 --> C3
C1 --> D
C2 --> D
C3 --> D

D --> SPEC_CNN
D --> SPEC_CNN_1
D --> SPEC_CNN_2
```

#### Feature Engineering
```mermaid
graph TD
D[Feature Engineering]
D1[Precision <br/> Logarithm Log1p]
D2[Min-Max Scaling <br/> Channel Wise]
D3[Min-Max Scaling <br/> Instance Wise]
D4[Data Augmentation <br/> FancyPCA]
D5[Image Formation: <br/> C3, C4, Cz as RGB] 

D --> D1
D --> D2
D --> D3
D --> D4
D --> D5

class D1,D2,D3,D4,D5 optional
classDef optional fill:#ffffff,stroke:#000000,stroke-dasharray: 5 5
```