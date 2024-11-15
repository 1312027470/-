from sklearn.decomposition import PCA
pca=PCA(n_components=0.95)
pca.fit(X)
Y=pca.transform(X)
tzxl=pca.components_
tz=pca.explained_variance_
gxl=pca.explained_variance_ratio_

