# Hands-On-Machine-Learning 개념정리

## Part 1 Machine Learning

### 1. 한눈에 보는 머신러닝

- 머신러닝(Machine Learning):

  데이터로부터 학습할 수 있는 시스템 만드는 것

  명시적 프로그래밍 없이 컴퓨터가  학습하는 능력을 갖추게 하는 분야<br><br>

  

- 데이터 마이닝(data mining):

  겉으로 보이지 않는 패턴 발견<br><br>

  

- 머신러닝 시스템의 종류

  지도학습

  비지도학습 -> (준지도, 강화학습)<br>

  <br>

1. 지도학습

   - 훈련데이터에 원하는 답 포함

     ex)분류: 스팸필터(0:스팸이다. 1:스팸이아니다.)

     ex)회귀: 예측변수인(주행거리, 연식, 브랜드)를 사용해 중고차 가격 예측<br>

     <br>

   - 지도 학습 알고리즘

     k-최근접 이웃(K-nearest neighbors) : 

     가장 가까운 이웃 찾아줌<br><br>

     선형회귀(linear Regression) : 

     종족변수 y와 한개이상 독립변수 x와의 상관관계를 모델링 하는 회귀분석 기법<br><br>

     로지스틱 회귀(Logistic Regression) :

     데이터의 범주를 0 ~ 1사이로 예측 후 그 비율로 분류<br>

     범주 확률을 0.5로 설정시 0.5이상이면 스팸, 미만이면 스팸X<br>

     <br>

     서포트 벡터 머신(Support Vector Machine)(SVM) : 

     분류를 위한 기준선 정의<br>

     <br>

     결정트리(decision tree)와 랜덤 포레스트(random forest) :

     스무고개(예/아니오 -> 날수있으면(새) 없으면 (펭귄))

     랜덤포레스트는 결정트리로 인기투표하는 형식<br>

     <br>

     신경망(neural networks)

     

     

