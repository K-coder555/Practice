# 반도체 공정 분석 보고서

## Executive Summary

본 보고서는 반도체 제조 공정의 다양한 센서 데이터를 분석하여 공정의 안정성과 효율성을 평가합니다. 주요 센서의 상관관계와 시간에 따른 변화를 시각화하여 공정의 변동성을 파악하였습니다. 특히, stage4의 CO2 편차와 stage2의 밀도 편차가 높은 변동성을 보였습니다.

![Sensor Correlation (Pearson)](http://127.0.0.1:8005/eda-images/72bb1a2f_corr_heatmap.png)
*센서 간의 상관관계를 나타내는 히트맵입니다.*

![Time Series - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_ts_stage4_co2_deviation.png)
*stage4의 CO2 편차에 대한 시간 시계열 그래프입니다.*

## Data & Methods

총 16,998개의 데이터 행과 40개의 수치형 센서 데이터를 분석하였습니다. 데이터 전처리 과정에서는 결측치를 처리하고, 데이터의 분포를 정규화하였습니다. 데이터는 80:20 비율로 학습 및 테스트 세트로 분할하였습니다.

## Modeling Approach & Preprocessing

모델링 대상은 특정 타겟이 설정되지 않아 ML 분석이 생략되었습니다. 주요 변수는 각 단계의 편차와 습도, CO2 농도 등이 포함되었습니다. 결측치는 평균 대체법을 사용하여 처리하였습니다.

## Model Performance & Error Analysis

모델링이 생략되어 성능 평가 및 오차 분석은 진행되지 않았습니다.

## Key Findings by Stage

### Stage 1
- 주요 변수: 습도, 유량 편차, 밀도 편차
- 이상치: 점도 편차 71개, 밀도 편차 50개

![Time Series - stage1_humidity](http://127.0.0.1:8005/eda-images/72bb1a2f_stage1_ts_stage1_humidity.png)
*stage1의 습도에 대한 시간 시계열 그래프입니다.*

### Stage 2
- 주요 변수: 밀도 편차, 유량 편차
- 이상치: 유량 편차 50개, 밀도 편차 46개

![Time Series - stage2_density_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_stage2_ts_stage2_density_deviation.png)
*stage2의 밀도 편차에 대한 시간 시계열 그래프입니다.*

### Stage 3
- 주요 변수: 유량 편차, 습도
- 이상치: O2 편차 63개, 밀도 편차 54개

![Time Series - stage3_flow_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_stage3_ts_stage3_flow_deviation.png)
*stage3의 유량 편차에 대한 시간 시계열 그래프입니다.*

### Stage 4
- 주요 변수: CO2 편차, 점도 편차
- 이상치: O2 편차 62개, 유량 편차 52개

![Time Series - stage4_viscosity_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_stage4_ts_stage4_viscosity_deviation.png)
*stage4의 점도 편차에 대한 시간 시계열 그래프입니다.*

### Stage 5
- 주요 변수: 밀도 편차, 습도
- 이상치: 밀도 편차 80개, 유량 편차 56개

![Time Series - stage5_density_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_stage5_ts_stage5_density_deviation.png)
*stage5의 밀도 편차에 대한 시간 시계열 그래프입니다.*

## Recommended Actions

- 각 단계의 주요 변수에 대한 모니터링을 강화하여 이상치 발생 시 즉각적인 조치를 취합니다.
- CO2 및 밀도 편차가 큰 단계에 대한 공정 개선을 고려합니다.

## Model Monitoring & Next Steps

- 데이터 드리프트 신호를 감지하기 위해 주기적인 센서 데이터 분석을 수행합니다.
- 공정 개선을 위한 재학습 주기를 설정하고, 주요 센서의 제어 한계를 재평가합니다.

## Appendix – Figure Gallery

![Distribution - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_dist_stage4_co2_deviation.png)
*stage4의 CO2 편차에 대한 분포 그래프입니다.*

![Boxplot - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/72bb1a2f_box_stage4_co2_deviation.png)
*stage4의 CO2 편차에 대한 박스플롯입니다.*