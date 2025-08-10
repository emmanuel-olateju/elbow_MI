# elbow_MI

Stroke Motor-Imagery [Dataset](https://figshare.com/articles/dataset/EEG_datasets_of_stroke_patients/21679035/5)

Article [Link](https://www.nature.com/articles/s41597-023-02787-8)


## Pipeline
```mermaid
graph LR
A[Channel-Wise <br/> Epochs Detrending] 
B[STFT Spectrogram <br/> Computation]
C[Channel Selection <br/> C3, C4, Cz]

D1((Precision Logarithm <br/> log1p))
D2((Min-Max Scaling <br/> Channel Wise))
D3((Min-Max Scaling <br/> Spectrogram Wise))

E[FancyPCA data augmentation]
F[Image Formation: <br/> C3, C4, Cz as RGB]


A --> B --> C
    C --> D1
    C --> D2
    C --> D3
	D1 --> E --> F --> SPEC_CNN
    D2 --> E --> F --> SPEC_CNN_1
    D3 --> E --> F --> SPEC_CNN_2

class D1,D2,D3,E,F optional
classDef optional fill:#ffffff,stroke:#000000,stroke-dasharray: 5 5

 ```
