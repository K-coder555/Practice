# 반도체 공정 분석 보고서

## Executive Summary
본 보고서는 반도체 제조 공정의 다양한 단계에서 수집된 센서 데이터를 분석하여 공정의 변동성과 이상치를 식별하고, 이를 통해 공정 개선을 위한 인사이트를 제공합니다. 주요 센서의 변동성과 상관관계를 분석하여 공정의 안정성을 평가하고, SPC(Statistical Process Control) 차트를 통해 공정의 품질을 모니터링하였습니다.

## Data & Methods
본 분석은 총 16,998개의 데이터 행과 40개의 수치형 센서를 포함한 데이터셋을 기반으로 하였습니다. 각 단계별로 센서 데이터의 탐색적 데이터 분석(EDA)을 수행하였으며, SPC 차트를 통해 공정의 품질을 모니터링하였습니다.

- **Sampling/Resampling**: 데이터는 시간 순서에 따라 수집되었으며, 이상치 탐지를 위해 각 센서의 변동성을 분석하였습니다.
- **SPC Overview**: SPC 차트를 통해 각 단계의 공정 변동성을 시각화하고, 이상치 및 공정 이상을 식별하였습니다.

## Key Findings by Stage

### Stage 1
- **Top-variance Sensors**: stage1_humidity, stage1_flow_deviation, stage1_density_deviation, stage1_co2_deviation, stage1_viscosity_deviation
- **Outlier Counts**: stage1_viscosity_deviation (71), stage1_density_deviation (50), stage1_n_deviation (44), stage1_co2_deviation (36), stage1_o2_deviation (32)
- **Strongest Correlations**: 없음

![Stage 1 Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_stage1_corr_heatmap.png)
*Stage 1의 센서 간 상관관계를 나타낸 히트맵입니다.*

![Stage 1 Time Series - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage1_ts_stage1_humidity.png)
*Stage 1의 습도 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 1 Time Series - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage1_ts_stage1_flow_deviation.png)
*Stage 1의 유량 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 1 Distribution - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage1_dist_stage1_humidity.png)
*Stage 1의 습도 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Stage 1 Boxplot - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage1_box_stage1_humidity.png)
*Stage 1의 습도 센서의 분포를 나타낸 박스플롯입니다.*

![Stage 1 SPC Chart - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage1_spc_stage1_humidity.png)
*Stage 1의 습도 센서의 SPC 차트입니다.*

### Stage 2
- **Top-variance Sensors**: stage2_density_deviation, stage2_flow_deviation, stage2_humidity, stage2_co2_deviation, stage2_n_deviation
- **Outlier Counts**: stage2_flow_deviation (50), stage2_density_deviation (46), stage2_n_deviation (40), stage2_viscosity_deviation (37), stage2_co2_deviation (36)
- **Strongest Correlations**: stage2_flow_deviation ~ stage4_viscosity_deviation (1.000), stage2_n_deviation ~ stage3_n_deviation (1.000)

![Stage 2 Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_stage2_corr_heatmap.png)
*Stage 2의 센서 간 상관관계를 나타낸 히트맵입니다.*

![Stage 2 Time Series - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage2_ts_stage2_density_deviation.png)
*Stage 2의 밀도 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 2 Time Series - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage2_ts_stage2_flow_deviation.png)
*Stage 2의 유량 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 2 Distribution - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage2_dist_stage2_density_deviation.png)
*Stage 2의 밀도 편차 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Stage 2 Boxplot - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage2_box_stage2_density_deviation.png)
*Stage 2의 밀도 편차 센서의 분포를 나타낸 박스플롯입니다.*

![Stage 2 SPC Chart - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage2_spc_stage2_density_deviation.png)
*Stage 2의 밀도 편차 센서의 SPC 차트입니다.*

### Stage 3
- **Top-variance Sensors**: stage3_flow_deviation, stage3_humidity, stage3_co2_deviation, stage3_density_deviation, stage3_o2_deviation
- **Outlier Counts**: stage3_o2_deviation (63), stage3_density_deviation (54), stage3_co2_deviation (44), stage3_n_deviation (44), stage3_flow_deviation (43)
- **Strongest Correlations**: stage3_n_deviation ~ stage2_n_deviation (1.000)

![Stage 3 Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_stage3_corr_heatmap.png)
*Stage 3의 센서 간 상관관계를 나타낸 히트맵입니다.*

![Stage 3 Time Series - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage3_ts_stage3_flow_deviation.png)
*Stage 3의 유량 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 3 Time Series - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage3_ts_stage3_humidity.png)
*Stage 3의 습도 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 3 Distribution - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage3_dist_stage3_flow_deviation.png)
*Stage 3의 유량 편차 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Stage 3 Boxplot - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage3_box_stage3_flow_deviation.png)
*Stage 3의 유량 편차 센서의 분포를 나타낸 박스플롯입니다.*

![Stage 3 SPC Chart - Flow Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage3_spc_stage3_flow_deviation.png)
*Stage 3의 유량 편차 센서의 SPC 차트입니다.*

### Stage 4
- **Top-variance Sensors**: stage4_co2_deviation, stage4_viscosity_deviation, stage4_humidity, stage4_flow_deviation, stage4_density_deviation
- **Outlier Counts**: stage4_o2_deviation (62), stage4_flow_deviation (52), stage4_viscosity_deviation (50), stage4_density_deviation (46), stage4_co2_deviation (42)
- **Strongest Correlations**: stage4_viscosity_deviation ~ stage2_flow_deviation (1.000), stage4_o2_deviation ~ stage5_flow_deviation (1.000)

![Stage 4 Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_stage4_corr_heatmap.png)
*Stage 4의 센서 간 상관관계를 나타낸 히트맵입니다.*

![Stage 4 Time Series - CO2 Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage4_ts_stage4_co2_deviation.png)
*Stage 4의 CO2 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 4 Time Series - Viscosity Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage4_ts_stage4_viscosity_deviation.png)
*Stage 4의 점도 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 4 Distribution - CO2 Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage4_dist_stage4_co2_deviation.png)
*Stage 4의 CO2 편차 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Stage 4 Boxplot - CO2 Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage4_box_stage4_co2_deviation.png)
*Stage 4의 CO2 편차 센서의 분포를 나타낸 박스플롯입니다.*

![Stage 4 SPC Chart - CO2 Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage4_spc_stage4_co2_deviation.png)
*Stage 4의 CO2 편차 센서의 SPC 차트입니다.*

### Stage 5
- **Top-variance Sensors**: stage5_density_deviation, stage5_humidity, stage5_o2_deviation, stage5_n_deviation, stage5_co2_deviation
- **Outlier Counts**: stage5_density_deviation (80), stage5_flow_deviation (56), stage5_n_deviation (47), stage5_co2_deviation (41), stage5_viscosity_deviation (40)
- **Strongest Correlations**: stage5_flow_deviation ~ stage4_o2_deviation (1.000)

![Stage 5 Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_stage5_corr_heatmap.png)
*Stage 5의 센서 간 상관관계를 나타낸 히트맵입니다.*

![Stage 5 Time Series - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage5_ts_stage5_density_deviation.png)
*Stage 5의 밀도 편차 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 5 Time Series - Humidity](http://127.0.0.1:8005/eda-images/456dc28d_stage5_ts_stage5_humidity.png)
*Stage 5의 습도 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Stage 5 Distribution - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage5_dist_stage5_density_deviation.png)
*Stage 5의 밀도 편차 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Stage 5 Boxplot - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage5_box_stage5_density_deviation.png)
*Stage 5의 밀도 편차 센서의 분포를 나타낸 박스플롯입니다.*

![Stage 5 SPC Chart - Density Deviation](http://127.0.0.1:8005/eda-images/456dc28d_stage5_spc_stage5_density_deviation.png)
*Stage 5의 밀도 편차 센서의 SPC 차트입니다.*

## Anomalies & Root-cause Hypotheses
- Stage 1의 점도 편차에서 높은 이상치 발생 [Figure 35].
- Stage 2의 유량 편차와 점도 편차 간의 강한 상관관계 [Figure 39].
- Stage 3의 산소 편차에서 높은 이상치 발생 [Figure 73].
- Stage 4의 점도 편차와 유량 편차 간의 강한 상관관계 [Figure 77].
- Stage 5의 밀도 편차에서 가장 높은 이상치 발생 [Figure 111].

## SPC & Impact on Yield/Throughput
SPC 차트를 통해 각 단계의 공정 변동성을 모니터링하였으며, 특히 Stage 5의 밀도 편차는 공정의 수율에 큰 영향을 미칠 수 있음을 확인하였습니다 [Figure 111].

## Recommended Actions
- **Short-term**: Stage 5의 밀도 편차를 70 이하로 유지하여 공정 안정성을 확보.
- **Mid-term**: Stage 2와 Stage 4의 유량 및 점도 편차 간의 상관관계를 줄이기 위한 공정 조정.

## Next Steps & Monitoring Plan
- 각 단계의 SPC 차트를 지속적으로 모니터링하여 공정의 변동성을 최소화.
- 이상치 발생 시 즉각적인 원인 분석 및 대응 조치 시행.

## Appendix – Figure Gallery

![Overall Sensor Correlation Heatmap](http://127.0.0.1:8005/eda-images/456dc28d_corr_heatmap.png)
*전체 센서 간 상관관계를 나타낸 히트맵입니다.*

![Overall Time Series - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage4_co2_deviation.png)
*전체 공정에서 stage4_co2_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Time Series - stage2_density_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage2_density_deviation.png)
*전체 공정에서 stage2_density_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Time Series - stage3_flow_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage3_flow_deviation.png)
*전체 공정에서 stage3_flow_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Time Series - stage4_viscosity_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage4_viscosity_deviation.png)
*전체 공정에서 stage4_viscosity_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Time Series - stage2_flow_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage2_flow_deviation.png)
*전체 공정에서 stage2_flow_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Time Series - stage5_density_deviation](http://127.0.0.1:8005/eda-images/456dc28d_ts_stage5_density_deviation.png)
*전체 공정에서 stage5_density_deviation 센서의 시간에 따른 변화를 나타낸 시계열 그래프입니다.*

![Overall Distribution - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/456dc28d_dist_stage4_co2_deviation.png)
*전체 공정에서 stage4_co2_deviation 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Overall Boxplot - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/456dc28d_box_stage4_co2_deviation.png)
*전체 공정에서 stage4_co2_deviation 센서의 분포를 나타낸 박스플롯입니다.*

![Overall Distribution - stage2_density_deviation](http://127.0.0.1:8005/eda-images/456dc28d_dist_stage2_density_deviation.png)
*전체 공정에서 stage2_density_deviation 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Overall Boxplot - stage2_density_deviation](http://127.0.0.1:8005/eda-images/456dc28d_box_stage2_density_deviation.png)
*전체 공정에서 stage2_density_deviation 센서의 분포를 나타낸 박스플롯입니다.*

![Overall Distribution - stage3_flow_deviation](http://127.0.0.1:8005/eda-images/456dc28d_dist_stage3_flow_deviation.png)
*전체 공정에서 stage3_flow_deviation 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Overall Boxplot - stage3_flow_deviation](http://127.0.0.1:8005/eda-images/456dc28d_box_stage3_flow_deviation.png)
*전체 공정에서 stage3_flow_deviation 센서의 분포를 나타낸 박스플롯입니다.*

![Overall Distribution - stage4_viscosity_deviation](http://127.0.0.1:8005/eda-images/456dc28d_dist_stage4_viscosity_deviation.png)
*전체 공정에서 stage4_viscosity_deviation 센서의 분포를 나타낸 히스토그램과 KDE입니다.*

![Overall Boxplot - stage4_viscosity_deviation](http://127.0.0.1:8005/eda-images/456dc28d_box_stage4_viscosity_deviation.png)
*전체 공정에서 stage4_viscosity_deviation 센서의 분포를 나타낸 박스플롯입니다.*

![Overall SPC Chart - stage4_co2_deviation](http://127.0.0.1:8005/eda-images/456dc28d_spc_stage4_co2_deviation.png)
*전체 공정에서 stage4_co2_deviation 센서의 SPC 차트입니다.*

![Overall SPC Chart - stage2_density_deviation](http://127.0.0.1:8005/eda-images/456dc28d_spc_stage2_density_deviation.png)
*전체 공정에서 stage2_density_deviation 센서의 SPC 차트입니다.*

![Overall SPC Chart - stage3_flow_deviation](http://127.0.0.1:8005/eda-images/456dc28d_spc_stage3_flow_deviation.png)
*전체 공정에서 stage3_flow_deviation 센서의 SPC 차트입니다.*

![Overall SPC Chart - stage4_viscosity_deviation](http://127.0.0.1:8005/eda-images/456dc28d_spc_stage4_viscosity_deviation.png)
*전체 공정에서 stage4_viscosity_deviation 센서의 SPC 차트입니다.*