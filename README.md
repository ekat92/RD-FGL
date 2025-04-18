# RD-FGL 2025 Code Supplement
[![arXiv](https://img.shields.io/badge/arXiv-2209.01697-b31b1b.svg?style=plastic)](https://arxiv.org/pdf/2209.01697)&nbsp;&nbsp;

Replication Materials for
> TH. Lee, E. Seregina (2025) "Combining Forecasts under Structural Breaks Using Graphical LASSO". ArXiv pre-print. doi.org/10.48550/arXiv.2209.01697.

## EMPIRICAL RESULTS 
[_we ran the simulations on ml.m5.4xlarge AWS instance (vCPU = 16, memory = 64 GiB)_]

"_IJF_empirical_RDFGL.ipynb_" and "_IJF_empirical_competing.ipynb_" provide the code to replicate the empirical exercise. The data for replication is located in DATA folder. 

**Data instructions for ECB SPF:**

 0) navigate to DATA -> ECB SPF data -> the corresponding target series of interest when making selection  
- "yhat.csv" contains forecasts, "forERR.csv" has forecast errors, "ytrue.csv" has true series. "breaks.csv" contains a break vector for state breaks(as defined in the paper). If you wish to create your own breaks vector please follow the suggestions of doing so in the paper
- In case you would like to update the data, we followed the following steps to obtain forecasts:
 1) download quarterly forecasts from the ECB SPF website (https://www.ecb.europa.eu/stats/ecb_surveys/survey_of_professional_forecasters/html/all_data.en.html).
Put the downloaded csv files in "Get Updated Data" -> "New folder")
 2) run "Excel.py" and "Excel2.py" to merge separate Excels from ECB SPF together
 3) the output of this procedure will be called "second_edit.csv" which collects all forecasts together. Make sure to transpose that matrix if you want to have forecasters in columns and time in rows.
 4) use the procedure described in the paper to get most frequent forecasters. This will produce new matrix of yhats. 
 To get updated forecast errors just subtract updated true series from updated yhats.

**Data instructions for FRED MD:**

0) navigate to DATA -> FRED MD data -> the corresponding target series of interest when making selection  
- "yhat.csv" contains forecasts, "forERR.csv" has forecast errors, "ytrue.csv" has true series. "breaks.csv" contains a break vector for state breaks (as defined in the paper). If you wish to create your own breaks vector please follow the suggestions of doing so in the paper. We also included csv for horizons h=2,3,4, denoted as "yhat2.csv", "forERR2.csv" etc  
- In case you would like to update the data:  
1) please navigate to notebook "IJF_empirical_competing.ipynb" -> run the cell titled "Updating FRED MD forecasts". This will create a new "data.csv" file in your working directory and create updated forecasts up to 4 steps ahead

## MONTE CARLO RESULTS (in the Supplementary Appendix)  
[_we ran the simulations on ml.r5.4xlarge AWS instance (vCPU = 16, memory = 128 GiB)_]  
"_IJF_simulations_weights.ipynb_" and "_IJF_simulations_msfe.ipynb_" provide the code to replicate Monte Carlo results in the Supplementary Appendix.
