# FERPlus_Vote_To_Label
[FERPlus](https://github.com/microsoft/FERPlus) 데이터셋의 주석 파일을 수정하는 코드

## 설명
- FERPlus 데이터셋은 기존 [FER2013](https://www.kaggle.com/datasets/msambare/fer2013) 데이터셋의 이미지를 그대로 유지하면서, 각 이미지에 대해 10명의 주석자가 감정을 투표한 결과를 추가로 포함한 데이터셋임
- 원본 데이터셋의 label csv파일은 10명의 주석자의 투표 결과의 형태로 이루어져 있음.
- 하나의 이미지에 하나의 expression label을 설정하기 위해, 가장 많은 투표 결과를 받은 한 개의 감정을 label로 채택하였음.


### 방법 1)
- 이때 최고 투표 결과가 동점인 경우 label 순서(0:Neutral, 1:Happiness, 2:Surprise, 3:Sadness, 4:Anger, 5:Disgust, 6:Fear, 7:Contempt)에서 앞쪽에 위치한 것으로 결정하였음(예: 4,0,0,4,2,0,0,0 인 경우 Neutral로 결정).
- 이에 따라 클래스 분포에서 Neutral이 많아지게 됨.

###방법 2)
- 최고 투표 결과가 동점인 경우 label 순서(0:Neutral, 1:Happiness, 2:Surprise, 3:Sadness, 4:Anger, 5:Disgust, 6:Fear, 7:Contempt)에서 뒤쪽에 위치한 것으로 결정하였음(예: 4,0,0,4,2,0,0,0 인 경우 Sadness로 결정).
- 이에 따라 클래스 분포에서 Neutral이 적어지게 됨.

## 변환 예시
- 변경 전
```
Usage,Image name,neutral,happiness,surprise,sadness,anger,disgust,fear,contempt,unknown,NF
Training,fer0000000.png,4,0,0,1,3,2,0,0,0,0
Training,fer0000001.png,6,0,1,1,0,0,0,0,2,0
Training,fer0000002.png,5,0,0,3,1,0,0,0,1,0
Training,fer0000003.png,4,0,0,4,1,0,0,0,1,0
Training,fer0000004.png,9,0,0,1,0,0,0,0,0,0
Training,fer0000005.png,6,0,0,1,0,0,1,1,1,0
Training,fer0000006.png,2,0,0,8,0,0,0,0,0,0
Training,fer0000007.png,0,10,0,0,0,0,0,0,0,0
Training,fer0000008.png,0,10,0,0,0,0,0,0,0,0
Training,fer0000009.png,0,0,6,0,0,0,4,0,0,0
```

- 변경 후
```
Image name,label
fer0000000.png,0
fer0000001.png,0
fer0000002.png,0
fer0000003.png,0
fer0000004.png,0
fer0000005.png,0
fer0000006.png,3
fer0000007.png,1
fer0000008.png,1
fer0000009.png,2
```

## 최종 데이터셋 구성

| **Dataset** | **Method** | **#Images** | **#Neutral** | **#Happiness** | **#Surprise** | **#Sadness** | **#Anger** | **#Disgust** | **#Fear** | **#Contempt** |
| :---------: | :--------: | :---------: | :----------: | :------------: | :-----------: | :----------: | :--------: | :----------: | :-------: | :-----------: |
| FERPlus     | 방법 1     | 35711       | 13013        | 9367           | 4493          | 4415         | 3124       | 253          | 825       | 221           |
| FERPlus     | 방법 2     | 35711       | 11909        | 9361           | 4452          | 4903         | 3343       | 351          | 1062      | 330           |



<img src="" width="1000">
