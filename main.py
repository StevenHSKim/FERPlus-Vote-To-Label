import pandas as pd

# CSV 파일 읽기
# FERPlus 데이터셋의 수정된 라벨 파일(FERPlus_Label_modified.csv)을 읽어옵니다.
data = pd.read_csv('path/to/FERPlus_Label_modified.csv')

# 'Usage', 'unknown', 'NF' 열 삭제
# 데이터셋에서 분석 및 라벨링에 불필요한 열을 제거합니다.
data = data.drop(columns=['Usage', 'unknown', 'NF'])

# 모든 값이 0인 행 삭제
# 'Image name' 열을 제외한 나머지 감정 점수 열에서 모든 값이 0인 행(잘못된 데이터)을 제거합니다.
data = data[(data.iloc[:, 1:] != 0).any(axis=1)]

# 각 행의 최대값 인덱스를 label로 추가
# 각 행에서 감정 점수의 최대값을 찾아 해당 감정의 인덱스를 'label' 열에 추가합니다.
# 예: [4, 0, 3, 0, 0, 0, 0, 0] → 최대값 4의 인덱스(0)를 'label'로 저장.
data['label'] = data.iloc[:, 1:].apply(lambda row: row.values.argmax(), axis=1)

# 필요한 열만 선택
# 최종 데이터에서 'Image name'(이미지 파일 이름)과 'label'(최종 라벨) 열만 남깁니다.
data = data[['Image name', 'label']]

# 결과 저장
# 전처리된 데이터를 'modified_file.csv'로 저장합니다. 기존 인덱스는 저장하지 않습니다.
data.to_csv('FERPlus_Label_modified.csv', index=False)
