from .phate import PHATE
from .pca import PCA
from .dm import DM
from .mds import MDS
from .mds_on_dm import MDS_on_DM
from .tsne import TSNE
from .tsne_on_dm import TSNE_on_DM
from .lle import LLE
from .isomap import Isomap
from .force_directed import Force_Directed_Layout
from .umap import UMAP
from .dbmap import dbMAP
from .dm_adap import DM_Adaptive



all_methods = [
    PHATE,
    PCA,
    DM,
    MDS,
    MDS_on_DM,
    TSNE,
    TSNE_on_DM,
    LLE,
    Isomap,
    Force_Directed_Layout,
    UMAP
]

parallel_methods = [
    PHATE,
    PCA,
    DM,
    MDS,
    MDS_on_DM,
    TSNE,
    TSNE_on_DM,
    LLE,
    Isomap,
    Force_Directed_Layout,
    UMAP,
]

