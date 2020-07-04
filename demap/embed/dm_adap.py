import dbmap as dm

def DM_Adaptive(data, knn=15):
    diff = dm.diffusion.Diffusor(n_neighbors=knn).fit(data)
    db = diff.transform(data)

    return db
