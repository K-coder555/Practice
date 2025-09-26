```markdown
# 반도체 공정 분석 보고서

## 1. 요약
본 보고서는 반도체 제조 공정의 다양한 단계에서 발생하는 센서 데이터의 변동성과 상관관계를 분석한 결과를 제시합니다. 주요 발견 사항으로는 stage2와 stage4의 센서 간 강한 상관관계가 있으며, 특히 stage2_flow_deviation과 stage4_viscosity_deviation의 상관계수는 1.000으로 나타났습니다 [Figure 1]. 또한, stage5_density_deviation 센서에서 가장 많은 이상치가 발견되었습니다.

![](http://127.0.0.1:8005/eda-images/83a069d6_corr_heatmap.png)
*Figure 1: 전체 센서 간 상관관계 히트맵. 강한 상관관계가 여러 센서 쌍에서 관찰됩니다.*

## 2. 데이터 및 방법론
본 분석은 총 16,998개의 데이터 행과 40개의 수치형 센서를 포함한 데이터셋을 기반으로 수행되었습니다. 각 단계별로 센서의 변동성과 이상치를 파악하기 위해 탐색적 데이터 분석(EDA)과 통계적 공정 관리(SPC)를 적용하였습니다.

## 3. 단계별 주요 발견 사항

### Stage 1
- **최대 변동 센서**: stage1_humidity, stage1_flow_deviation, stage1_density_deviation
- **이상치 수**: stage1_viscosity_deviation (71), stage1_density_deviation (50)
- **강한 상관관계**: 없음

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_corr_heatmap.png)
*Figure 20: Stage 1 센서 간 상관관계 히트맵.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_ts_stage1_humidity.png)
*Figure 21: Stage 1의 습도 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_ts_stage1_flow_deviation.png)
*Figure 22: Stage 1의 유량 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_dist_stage1_humidity.png)
*Figure 27: Stage 1의 습도 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_box_stage1_humidity.png)
*Figure 28: Stage 1의 습도 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage1_spc_stage1_humidity.png)
*Figure 35: Stage 1의 습도 센서의 SPC 차트.*

### Stage 2
- **최대 변동 센서**: stage2_density_deviation, stage2_flow_deviation
- **이상치 수**: stage2_flow_deviation (50), stage2_density_deviation (46)
- **강한 상관관계**: stage2_flow_deviation ~ stage4_viscosity_deviation (1.000)

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_corr_heatmap.png)
*Figure 39: Stage 2 센서 간 상관관계 히트맵.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_ts_stage2_density_deviation.png)
*Figure 40: Stage 2의 밀도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_ts_stage2_flow_deviation.png)
*Figure 41: Stage 2의 유량 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_dist_stage2_density_deviation.png)
*Figure 46: Stage 2의 밀도 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_box_stage2_density_deviation.png)
*Figure 47: Stage 2의 밀도 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage2_spc_stage2_density_deviation.png)
*Figure 54: Stage 2의 밀도 편차 센서의 SPC 차트.*

### Stage 3
- **최대 변동 센서**: stage3_flow_deviation, stage3_humidity
- **이상치 수**: stage3_o2_deviation (63), stage3_density_deviation (54)
- **강한 상관관계**: 없음

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_corr_heatmap.png)
*Figure 58: Stage 3 센서 간 상관관계 히트맵.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_ts_stage3_flow_deviation.png)
*Figure 59: Stage 3의 유량 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_ts_stage3_humidity.png)
*Figure 60: Stage 3의 습도 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_dist_stage3_flow_deviation.png)
*Figure 65: Stage 3의 유량 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_box_stage3_flow_deviation.png)
*Figure 66: Stage 3의 유량 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage3_spc_stage3_flow_deviation.png)
*Figure 73: Stage 3의 유량 편차 센서의 SPC 차트.*

### Stage 4
- **최대 변동 센서**: stage4_co2_deviation, stage4_viscosity_deviation
- **이상치 수**: stage4_o2_deviation (62), stage4_flow_deviation (52)
- **강한 상관관계**: stage4_viscosity_deviation ~ stage2_flow_deviation (1.000)

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_corr_heatmap.png)
*Figure 77: Stage 4 센서 간 상관관계 히트맵.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_ts_stage4_co2_deviation.png)
*Figure 78: Stage 4의 CO2 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_ts_stage4_viscosity_deviation.png)
*Figure 79: Stage 4의 점도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_dist_stage4_co2_deviation.png)
*Figure 84: Stage 4의 CO2 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_box_stage4_co2_deviation.png)
*Figure 85: Stage 4의 CO2 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage4_spc_stage4_co2_deviation.png)
*Figure 92: Stage 4의 CO2 편차 센서의 SPC 차트.*

### Stage 5
- **최대 변동 센서**: stage5_density_deviation, stage5_humidity
- **이상치 수**: stage5_density_deviation (80), stage5_flow_deviation (56)
- **강한 상관관계**: stage5_flow_deviation ~ stage4_o2_deviation (1.000)

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_corr_heatmap.png)
*Figure 96: Stage 5 센서 간 상관관계 히트맵.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_ts_stage5_density_deviation.png)
*Figure 97: Stage 5의 밀도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_ts_stage5_humidity.png)
*Figure 98: Stage 5의 습도 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_dist_stage5_density_deviation.png)
*Figure 103: Stage 5의 밀도 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_box_stage5_density_deviation.png)
*Figure 104: Stage 5의 밀도 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_stage5_spc_stage5_density_deviation.png)
*Figure 111: Stage 5의 밀도 편차 센서의 SPC 차트.*

## 4. 이상치 및 근본 원인 가설
Stage 5에서 가장 많은 이상치가 발견되었으며, 이는 stage5_density_deviation 센서에서 주로 발생했습니다. 이는 공정 중 밀도 편차가 큰 영향을 미쳤을 가능성이 있습니다 [Figure 103].

## 5. SPC 및 수율/처리량에 미치는 영향
SPC 분석 결과, 여러 단계에서 공정 한계를 초과하는 경우가 발견되었습니다. 특히 stage4와 stage5에서의 편차가 수율에 부정적인 영향을 미칠 수 있습니다 [Figure 92, Figure 111].

## 6. 권장 조치
- **단기**: stage5_density_deviation 센서의 편차를 5% 이내로 유지하도록 조정.
- **중기**: stage2와 stage4의 강한 상관관계를 고려하여 공정 조정.

## 7. 다음 단계 및 모니터링 계획
- **모니터링 센서**: stage5_density_deviation, stage4_viscosity_deviation
- **제어 한계**: 편차 5% 이내 유지
- **갱신 주기**: 매주 데이터 갱신 및 분석

## 8. 부록 – 그림 갤러리
![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage4_co2_deviation.png)
*Figure 2: Stage 4의 CO2 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage2_density_deviation.png)
*Figure 3: Stage 2의 밀도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage3_flow_deviation.png)
*Figure 4: Stage 3의 유량 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage4_viscosity_deviation.png)
*Figure 5: Stage 4의 점도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage2_flow_deviation.png)
*Figure 6: Stage 2의 유량 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_ts_stage5_density_deviation.png)
*Figure 7: Stage 5의 밀도 편차 센서의 시간에 따른 변화.*

![](http://127.0.0.1:8005/eda-images/83a069d6_dist_stage4_co2_deviation.png)
*Figure 8: Stage 4의 CO2 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_box_stage4_co2_deviation.png)
*Figure 9: Stage 4의 CO2 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_dist_stage2_density_deviation.png)
*Figure 10: Stage 2의 밀도 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_box_stage2_density_deviation.png)
*Figure 11: Stage 2의 밀도 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_dist_stage3_flow_deviation.png)
*Figure 12: Stage 3의 유량 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_box_stage3_flow_deviation.png)
*Figure 13: Stage 3의 유량 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_dist_stage4_viscosity_deviation.png)
*Figure 14: Stage 4의 점도 편차 센서의 분포.*

![](http://127.0.0.1:8005/eda-images/83a069d6_box_stage4_viscosity_deviation.png)
*Figure 15: Stage 4의 점도 편차 센서의 박스플롯.*

![](http://127.0.0.1:8005/eda-images/83a069d6_spc_stage4_co2_deviation.png)
*Figure 16: Stage 4의 CO2 편차 센서의 SPC 차트.*

![](http://127.0.0.1:8005/eda-images/83a069d6_spc_stage2_density_deviation.png)
*Figure 17: Stage 2의 밀도 편차 센서의 SPC 차트.*

![](http://127.0.0.1:8005/eda-images/83a069d6_spc_stage3_flow_deviation.png)
*Figure 18: Stage 3의 유량 편차 센서의 SPC 차트.*

![](http://127.0.0.1:8005/eda-images/83a069d6_spc_stage4_viscosity_deviation.png)
*Figure 19: Stage 4의 점도 편차 센서의 SPC 차트.*
```
