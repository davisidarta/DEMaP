import pandas as pd
import dbmap as dm

def dbMAP(data, knn=15, n_jobs=10):
    diff = dm.diffusion.Diffusor(n_neighbors=knn, alpha=0, ann_dist='cosine_sparse').fit(data)
    db = diff.transform(data)
    db = pd.DataFrame(db, dtype='numpy.float64')
    res = dm.umapper.UMAP(db, n_jobs=n_jobs, n_neighbors=knn, nmslib_metric='cosine')
    
    return res

