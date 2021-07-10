# Differential Privacy using K-Anonymity
## ✔️ To-do list
- [x] Run 6 methods on 6 datasets 
- [x] Add L-diversity, Classic Mondrian (no hierarchies), Datafly algorithm
- [x] Make NCP loss a separated module
- [x] Implement DM, CAVG metrics 
- [x] Implement classification models (basic classifier, clustering)
- [x] Run experiment on 6 datasets x 6 methods x 2 ML models
- [x] Finish report
- [ ] (Improvement) T-closeness method, Incognito Algorithm
- [ ] (Optional) Simple Deanonymize Attack


## 📖 Reports
Report edit link:
[![report](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)](https://www.overleaf.com/4786864492ypscdyrmpwzd)

## Folder Structure
- A dataset must comes with a .csv file contains features information and a hierarchy folder which contains predefined generalization hierarchies for its QID attributes. 
```
this repo
│   anonymize.py
|
└───data  
│   │
│   └───adult
│       │   adult.csv
│       └───hierarchies
│       │     adult_hierarchy_workclass.csv
│       │     ....
```

- Here is an example for a generalization hierarchy of the 'workclass' attribute from ADULT dataset, described in ```adult_hierarchy_workclass.csv```, which is a csv file using **";" as delimiter**
```
Private;Non-Government;*
Self-emp-not-inc;Non-Government;*
Self-emp-inc;Non-Government;*
Federal-gov;Government;*
Local-gov;Government;*
State-gov;Government;*
Without-pay;Unemployed;*
Never-worked;Unemployed;*
```

which describes this tree:

<div align="center"><img width="450" alt="screen" src="demo/adult_workclass.PNG"></div>

-------------------------------------------------------------

## 🌟 Executing
To anonymize dataset, run:
```
python anonymize.py --method=<model_type> --k=<k-anonymity> --dataset=<dataset_name>
```
- **model_type**: [mondrian | classic_mondrian | mondrian_ldiv | topdown | cluster | datafly]
- **dataset_name**: [adult | cahousing | cmc | mgm | informs | italia]

Results will be in ```results/{dataset}/{method}``` folder

To run evaluation metrics on every combination of algorithms, datasets and value k, run:
```
python visualize.py
```

Results will be in ```demo/{metrics.png, metrics_ml.png}``` 

## K-Anonymity examples

| Before anonymization | After anonymization with k = 2 |
|:-------------------------:|:-------------------------:|
|<img width="450" alt="screen" src="demo/italia_before.png"> | <img width="450" alt="screen" src="demo/italia_after.png"> |

## Evaluation Metrics
  
| Evaluate anonymization using information loss metrics |
|:-------------------------:|
|<img width="1000" height="600" alt="screen" src="demo/metrics.png"> |
|<img width="1000" height="600" alt="screen" src="demo/metrics2.png"> |
  

| Evaluate anonymization using classification models |
|:-------------------------:|
|<img width="1000" height="600" alt="screen" src="demo/metrics_ml.png"> |
|<img width="1000" height="600" alt="screen" src="demo/metrics_ml2.png"> |



## References:
- Basic Mondrian, Top-Down Greedy, Cluster-based (https://github.com/fhstp/k-AnonML)
- L-Diversity (https://github.com/Nuclearstar/K-Anonymity, https://github.com/qiyuangong/Mondrian_L_Diversity)
- Classic Mondrian (https://github.com/qiyuangong/Mondrian)
- Datafly Algorithm (https://github.com/nazilkbahar/python-datafly)
- Normalized Certainty Penalty from [Utility-Based Anonymization for Privacy Preservation with
Less Information Loss](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.450.6140&rep=rep1&type=pdf)
- Discernibility, Average Equivalent Class Size from [A Systematic Comparison and Evaluation
of k-Anonymization Algorithms
for Practitioners](http://www.tdp.cat/issues11/tdp.a169a14.pdf)
- [Privacy in a Mobile-Social World](https://courses.cs.duke.edu//fall12/compsci590.3/slides/lec3.pdf)
- Code and idea based on [k-Anonymity in Practice: How Generalisation and Suppression Affect Machine Learning Classifiers](https://arxiv.org/abs/2102.04763)
