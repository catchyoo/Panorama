# Automatic stitching of two images(Panorama)

### 비주얼 오토메트리 중간시험 과제

1. 서강대학교 이미지를 촬영하여 1024*1024 크기로 resize.

2. 입력 이미지 Grayscale로 변환.

3. 이미지 간의 매칭을 위해 필요한 특징점(Keypoints & Descriptors) 추출.

4. 이미지 간의 매칭을 수행하기 위해 BruteForce Matcher 사용.

5. 매칭된 Keypoints 거리에 따라 정렬하여 Good Match 추출.

6. Good Match 로부터 Homography 행렬 계산. 이때 Outliers 고려하여 RANSAC 알고리즘 사용.

7. Homography 행렬 통해 파노라마 이미지 생성. 
