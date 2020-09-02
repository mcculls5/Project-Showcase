# Protein Energy and Rigidity

In this research-oriented project, I worked in an interdisciplinary group of Biology and Computer Science students to explore potential metrics to predict the effects of single point protein substitution mutations. We modified an existing pipeline that generated energy-minimized mutant proteins *in silico*.

We investigated the use of protein structure data produced by the energy-minimization process as well as rigid atom clusters to create and test various metrics.

## Contents
As this project is related to classwork, some code must be omitted.
- **Final Report.pdf** : Describes the results of our exploration.
- **Project Description.pdf** : The initial description for the exploratory project. **NOTE**: This project is labeled as project 7.

- **Preprocess/** : Contains the python scripts that were used to initially clean and compile the data.
  - **aggregate_raw_em_step_data.py** : Aggregates the mutant energy minimization step data.
  - **aggregate_raw_ra_cluster_data.py** : Aggregates the mutant rigid atom cluster data.
  - **aggregate_raw_ra_constraint_data.py** : Aggregates the mutant constraint (bond) data.
  
- **EnergyMinimization/** : Contains the python scripts that computed various EM metrics.
  - **em_finalize_metric.py** : Computes the final normalized energy minimized metric using numpy, scipy, and pandas.
  - **em_metrics_from_aggregate.py** : Calculates many energy-step thresholds and metrics from the raw aggregated data.
  - **em_refine_metrics.py** : Normalizes metrics by incorporating metric calculations of the PDB wildtypes using numpy, scipy, and pandas.
  
- **Rigidity/** : Contains the python scripts that computed various Rigidity metrics.
  - **cluster_from_aggregate.py** : Normalizes the cluster count of mutants by subracting the wildtype's clusters
  - **clusterSizeOutlier.py** : Determines the number of outlier clusters by size
  - **outlierCountAnalysis.py** : Performs analysis on the outlier counts of mutants when grouped by various characteristics.

- **Visualization/** : Contains scripts and output of the data visualization exploration using heatmaps.
  - **output/** : Contains all generated heatmaps
  - **create_averageall_\*.py** : creates heatmaps with averaged metrics
  - **create_combined_heatmaps.py** : creates heatmaps for each PDB using both a compound EM and Rigidity metric
  - **create_single_\*.py** : creates heatmaps based only on the single point mutation data
  - **create_variance_\*.py** : creates heatmaps using a variance-based metric of single and double-point mutations
  - **createHeatmap.py** : Generates and saves the heatmap. Used by all other heatmap scripts
  