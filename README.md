![github-header-image-5](https://user-images.githubusercontent.com/96799559/169658516-0d78a0e2-ca15-4849-96de-6e201e858896.png)


## Project Description 
Course: MMAI 5040 Business Applications of Artificial Intelligence 

Netflix Rooms is a machine learning recommender system that clusters users based on shared interests and demographics. We leveraged `K-Means`, `Principle Component Analysis` (PCA), and `t-distributed stochastic neighbourhood embedding` (t-SNE) to form the clusters and `Decision Trees` for interpretation. Afterwards, we created a “Community Persona” for the cluster with the strongest differences to provide the user with an example of how this recommender system could work once deployed. 

Netflix Rooms’ objective is to connect similar users together through this proposed virtual movie theater experience to provide an element of human-connection to streaming. The aim is to improve the well-being of Netflix users, while also providing the company with a clear return on investment and a competitive edge. 

To see our full project proposal, refer to the [following](https://github.com/bintualkassoum/netflix-rooms-project/blob/main/Netflix%20Rooms%20Project%20Proposal.pdf).

## Installation 
![](https://img.shields.io/badge/Library-Google%20Colab-informational?style=flat&logo=googlecolab&logoColor=white&color=F25757)
![](https://img.shields.io/badge/Library-Numpy-informational?style=flat&logo=numpy&logoColor=white&color=F25757)
![](https://img.shields.io/badge/Library-Pandas-informational?style=flat&logo=pandas&logoColor=white&color=F25757)

No additional packages need to be installed, as we used `Pandas` and `Numpy`, both of which are pre-installed on Google Colab. 

For additional information regarding package and library installations via Google Colab, please see [here](https://colab.research.google.com/github/bebi103a/bebi103a.github.io/blob/master/lessons/03/packages_and_modules.ipynb).

## K-Means Model

### Implementation
```
from sklearn.cluster import KMeans

KM_clusters = KMeans(n_clusters=20, init='k-means++').fit(XC) 
KM_clustered = XC.copy()
KM_clustered = pd.DataFrame(KM_clustered)
KM_clustered.loc[:,'Cluster'] = KM_clusters.labels_ 
```
<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928392-b16768c9-df55-4454-ab28-55e6b6b12b89.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928393-d8ade16b-bbaa-4ac0-99d7-6fecddefbe03.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

### PCA Fitting 
```
from sklearn.decomposition import PCA 

WCSS = []
for i in range(1, 21): 
  kmeans_pca = KMeans(n_clusters = i, init = 'k-means++', random_state=42)
  kmeans_pca.fit(scores_pca)
  WCSS.append(kmeans_pca.inertia_)
  ```
<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928398-a3ec9929-d55c-40a6-ad03-3785c4f2388d.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928394-7253d814-cec2-490b-b8ce-bba762136b00.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

### PCA Implementation 
```
kmeans_pca = KMeans(n_clusters=20, init = 'k-means++', random_state=42)
kmeans_pca.fit(scores_pca)
```
<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928395-d0e405da-1b6e-4858-be92-9ecc2811113b.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

### t-SNE Implementation
```
from sklearn.manifold import TSNE

tsne = TSNE(verbose=1, perplexity=50) 
X_embedded = tsne.fit_transform(X_scaled.to_numpy())
```
<p align="center">
<img align="middle" src="https://user-images.githubusercontent.com/96799559/169928396-6e32ac36-b421-42cb-a490-753fd07a3ea8.jpg" width="500" length="250" />
<!-- <figcaption>Samples from SDEBNN-learned predictive prior and posterior density distributions.</figcaption> -->
</p>

### Decision Tree Cluster Analysis
```
from sklearn import tree

clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)
```

## Product Design 
![](https://img.shields.io/badge/Library-Balsamiq-informational?style=flat&logoColor=white&color=F25757)
![](https://img.shields.io/badge/Library-MS%20Power%20Point-informational?style=flat&logo=numpy&logoColor=white&color=F25757)

## Deployment 

## What I Learned 

## Credits 
[Agnel Mamachan](https://github.com/AgnelMamachan)

[Krystaleah R](https://github.com/KrystaleahR)

[Pooja Ganiga](https://github.com/poojaganiga)

[Somiya Jena](https://github.com/somiyajena98)

[Yiman Zhou](https://github.com/yimanzhou)

[Zhiyi Wang](https://www.linkedin.com/in/zhiyi-zw-0331/)

## Helpful Resources 
Google Colaboratory. (n.d.). packages_and_modules.ipynb. Google Colaboratory (Colab). Retrieved May 21, 2022, from https://colab.research.google.com/github/bebi103a/bebi103a.github.io/blob/master/lessons/03/packages_and_modules.ipynb
