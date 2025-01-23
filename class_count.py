import pandas as pd

# CSV 파일 읽기
data = pd.read_csv('./FERPlus_Label_modified.csv')

# 각 클래스(label)의 개수 세기
class_counts = data['label'].value_counts().sort_index()

# 클래스 개수 출력
for label, count in class_counts.items():
    print(f"{label}: {count}")
