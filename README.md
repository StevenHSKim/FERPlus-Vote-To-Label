# FERPlus_Vote_To_Label
Code to modify annotation files for the [FERPlus](https://github.com/microsoft/FERPlus) dataset

## 설명
- The FERPlus dataset retains the original images from the [FER2013](https://www.kaggle.com/datasets/msambare/fer2013) dataset while including the voting results of 10 annotators for each image
- The label CSV file in the original dataset contains the voting results from 10 annotators
- To assign a single expression label to each image, the emotion with the highest number of votes was chosen as the label.

Method 1) Select First
- In the case of a tie for the highest vote count, the label was determined by the earliest position in the label order (0: Neutral, 1: Happiness, 2: Surprise, 3: Sadness, 4: Anger, 5: Disgust, 6: Fear, 7: Contempt).
  - Example: For a vote distribution of 4,0,0,4,2,0,0,0, the label is determined as Neutral.
- This approach results in an increased number of Neutral labels in the class distribution.

Method 2) Select Last
- In the case of a tie for the highest vote count, the label was determined by the latest position in the label order (0: Neutral, 1: Happiness, 2: Surprise, 3: Sadness, 4: Anger, 5: Disgust, 6: Fear, 7: Contempt).
  - Example: For a vote distribution of 4,0,0,4,2,0,0,0, the label is determined as Sadness.
- This approach results in a decreased number of Neutral labels in the class distribution.


## Execution
run main.py
```
python main.py --method select_last
```


## Example Transformation
- Before
```
Usage,Image name,neutral,happiness,surprise,sadness,anger,disgust,fear,contempt,unknown,NF
Training,fer0000000.png,4,0,0,1,3,2,0,0,0,0
Training,fer0000001.png,6,0,1,1,0,0,0,0,2,0
Training,fer0000002.png,5,0,0,3,1,0,0,0,1,0
Training,fer0000003.png,4,0,0,4,1,0,0,0,1,0
Training,fer0000004.png,9,0,0,1,0,0,0,0,0,0
```

- After
```
Image name,label
fer0000000.png,0
fer0000001.png,0
fer0000002.png,0
fer0000003.png,0
fer0000004.png,0
```


## Final Dataset Composition

| **Dataset** | **Method** | **#Images** | **#Neutral** | **#Happiness** | **#Surprise** | **#Sadness** | **#Anger** | **#Disgust** | **#Fear** | **#Contempt** |
| :---------: | :--------: | :---------: | :----------: | :------------: | :-----------: | :----------: | :--------: | :----------: | :-------: | :-----------: |
| FERPlus     | Select First | 35711       | 13013        | 9367           | 4493          | 4415         | 3124       | 253          | 825       | 221           |
| FERPlus     | Select Last  | 35711       | 11909        | 9361           | 4452          | 4903         | 3343       | 351          | 1062      | 330           |

<br>

<img width="1144" alt="image" src="https://github.com/user-attachments/assets/b5e7f71c-b3cb-4030-9e9f-a094c991cd66" />


