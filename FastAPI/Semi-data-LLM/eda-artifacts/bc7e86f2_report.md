# 반도체 공정 분석 보고서

## 1. 요약
본 보고서는 반도체 제조 공정에서 수집된 16,998개의 데이터 행과 40개의 수치형 센서를 분석하여 주요 변동성과 이상치를 식별하고, 공정 제어 및 수율에 미치는 영향을 평가합니다. 주요 발견 사항으로는 stage4_co2_deviation, stage2_density_deviation, stage3_flow_deviation, stage4_viscosity_deviation, stage2_flow_deviation, stage5_density_deviation 센서에서 높은 변동성이 관찰되었습니다. 또한, 여러 센서 간의 강한 상관관계가 확인되었습니다 [Figure 1].

## 2. 데이터 및 방법론
데이터 탐색적 분석(EDA)을 통해 센서 간 상관관계 및 이상치를 식별하였습니다. 상관관계 분석 결과, stage2_flow_deviation과 stage4_viscosity_deviation, stage2_n_deviation과 stage3_n_deviation 등에서 강한 상관관계가 발견되었습니다 [Figure 1].

![](http://127.0.0.1:8005/eda-images/bc7e86f2_corr_heatmap.png)

## 3. 공정/그룹별 주요 발견
- **Stage 4**: stage4_co2_deviation 및 stage4_viscosity_deviation에서 높은 변동성과 이상치가 관찰되었습니다 [Figure 2, Figure 5].
- **Stage 2**: stage2_density_deviation과 stage2_flow_deviation에서 변동성이 두드러졌습니다 [Figure 3, Figure 6].
- **Stage 3**: stage3_flow_deviation에서 변동성이 높았습니다 [Figure 4].

## 4. 이상치 및 근본 원인 가설
이상치 분석 결과, stage5_density_deviation에서 80건의 이상치가 발견되었으며, 이는 공정의 불안정성을 시사합니다. stage1_viscosity_deviation, stage3_o2_deviation 등에서도 다수의 이상치가 확인되었습니다. 이러한 이상치는 공정 조건의 변동성에 기인할 가능성이 높습니다.

## 5. SPC 및 수율/처리량에 미치는 영향
공정 능력 지수(SPC) 분석 결과, stage4_co2_deviation과 stage2_density_deviation에서 공정 제어 한계를 초과하는 경우가 관찰되었습니다 [Figure 16, Figure 17]. 이는 수율 및 처리량에 부정적인 영향을 미칠 수 있습니다.

## 6. 권장 조치
- **단기**: stage4_co2_deviation과 stage2_density_deviation의 변동성을 줄이기 위해 공정 조건을 엄격히 모니터링하고, 이상치 발생 시 즉각적인 조치를 취해야 합니다.
- **중기**: 센서 간 상관관계를 고려하여 공정 최적화를 위한 추가적인 분석을 수행해야 합니다. 예를 들어, stage2_flow_deviation과 stage4_viscosity_deviation의 상관관계를 활용한 공정 개선이 필요합니다.

## 7. 다음 단계 및 모니터링 계획
향후 분석에서는 이상치 발생 원인을 보다 구체적으로 규명하고, 공정 최적화를 위한 시뮬레이션을 진행할 계획입니다. 또한, 실시간 모니터링 시스템을 구축하여 공정 변동성을 지속적으로 관리할 것입니다.

![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage4_co2_deviation.png)
![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage2_density_deviation.png)
![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage3_flow_deviation.png)
![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage4_viscosity_deviation.png)
![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage2_flow_deviation.png)
![](http://127.0.0.1:8005/eda-images/bc7e86f2_ts_stage5_density_deviation.png)