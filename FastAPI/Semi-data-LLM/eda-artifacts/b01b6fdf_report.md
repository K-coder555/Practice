# 반도체 공정 분석 보고서

## 1) 요약
이 보고서는 반도체 제조 공정의 다양한 단계에서 발생하는 센서 데이터의 분석 결과를 제공합니다. 총 16,998개의 데이터 행과 40개의 수치형 센서 데이터를 분석하였으며, 주요 변동 센서와 상관관계가 높은 센서를 식별하였습니다. 각 단계별로 주요 발견 사항을 정리하고, 이상치 및 그 원인에 대한 가설을 제시합니다. 또한, SPC 차트를 통해 수율 및 처리량에 미치는 영향을 분석하고, 단기 및 중기 조치를 권장합니다.

## 2) 데이터 및 방법론 (EDA 개요)
총 16,998개의 데이터 행과 40개의 수치형 센서 데이터를 분석하였습니다. 주요 변동 센서는 stage4_co2_deviation, stage2_density_deviation, stage3_flow_deviation 등이 있습니다. 상관계수 |r|>0.8 이상인 센서 쌍은 여러 단계에서 발견되었습니다 [Figure 1].

![](http://127.0.0.1:8005/eda-images/b01b6fdf_corr_heatmap.png)

## 3) 단계별 주요 발견 사항
### Stage 1
- 주요 변동 센서: stage1_humidity, stage1_flow_deviation 등
- 이상치: stage1_viscosity_deviation에서 71개의 이상치 발견

### Stage 2
- 주요 변동 센서: stage2_density_deviation, stage2_flow_deviation 등
- 상관관계: stage2_flow_deviation과 stage4_viscosity_deviation의 상관계수는 1.000 [Figure 39]

![](http://127.0.0.1:8005/eda-images/b01b6fdf_stage2_corr_heatmap.png)

### Stage 3
- 주요 변동 센서: stage3_flow_deviation, stage3_humidity 등
- 이상치: stage3_o2_deviation에서 63개의 이상치 발견

### Stage 4
- 주요 변동 센서: stage4_co2_deviation, stage4_viscosity_deviation 등
- 상관관계: stage4_o2_deviation과 stage5_flow_deviation의 상관계수는 1.000 [Figure 77]

![](http://127.0.0.1:8005/eda-images/b01b6fdf_stage4_corr_heatmap.png)

### Stage 5
- 주요 변동 센서: stage5_density_deviation, stage5_humidity 등
- 이상치: stage5_density_deviation에서 80개의 이상치 발견

## 4) 이상치 및 원인 가설
- Stage 1의 stage1_viscosity_deviation에서 71개의 이상치가 발견되었습니다.
- Stage 5의 stage5_density_deviation에서 80개의 이상치가 발견되었습니다.
- 이러한 이상치는 공정 조건의 변동성 또는 센서 오류로 인한 것일 수 있습니다.

## 5) SPC 및 수율/처리량에 미치는 영향
SPC 차트를 통해 각 단계의 주요 변동 센서에 대한 공정 제어를 분석하였습니다. 예를 들어, stage4_co2_deviation의 SPC 차트는 공정의 안정성을 평가하는 데 유용합니다 [Figure 92].

![](http://127.0.0.1:8005/eda-images/b01b6fdf_stage4_spc_stage4_co2_deviation.png)

## 6) 권장 조치
### 단기
- Stage 2의 stage2_flow_deviation과 stage4_viscosity_deviation의 상관관계를 활용하여 공정 제어 강화
- 이상치가 많은 센서에 대한 즉각적인 점검 및 교정

### 중기
- 상관관계가 높은 센서 쌍에 대한 지속적인 모니터링 및 공정 최적화
- 이상치 발생 빈도가 높은 센서에 대한 장기적인 개선 계획 수립

## 7) 다음 단계 및 모니터링 계획
- 상관관계가 높은 센서 쌍에 대한 주기적인 데이터 분석 및 보고
- 이상치 발생 빈도가 높은 센서에 대한 지속적인 모니터링 및 개선 조치 평가

이 보고서는 반도체 제조 공정의 효율성을 높이기 위한 데이터 기반의 통찰을 제공합니다. 각 단계별로 식별된 문제점과 개선 방안을 통해 공정의 안정성과 수율을 향상시킬 수 있을 것입니다.