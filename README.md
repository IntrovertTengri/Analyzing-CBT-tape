# Analyzing-CBT-tape
In this project simple KMeans clustering was used on README files from CBT tape for data exploration. In addition, simple model with zero shot classification was used to classify repos from CBT tape into 4 categories.

1. `CBTTextProcessing.py` - utilities file with helper functions to process texts
2. `GetREADMEs.ipynb` - notebook, where the code for getting README files and texts from the `About` section was written.
3. `ClusteringREADMEs.ipynb` - clusterization conducted on collected README files.
4. `TextClassifier.ipynb` - LLM Bart was used for classifying READMEs into 4 categories.
