from .phate import PHATE
from .pca import PCA
from .dm import DM
from .mds import MDS
from .tsne import TSNE
from .tsne_on_dm import TSNE_on_DM
from .lle import LLE
from .isomap import Isomap
from .force_directed import Force_Directed_Layout
from .umap import UMAP
from .monocle import Monocle2
from .dbmap import dbMAP

all_methods = [
    dbMAP,
    PHATE,
    PCA,
    DM,
    MDS,
    TSNE,
    TSNE_on_DM,
    LLE,
    Isomap,
    Force_Directed_Layout,
    UMAP,
    Monocle2,
]

parallel_methods = [
    dbMAP,
    PHATE,
    PCA,
    DM,
    MDS,
    TSNE,
    TSNE_on_DM,
    LLE,
    Isomap,
    Force_Directed_Layout,
    UMAP,
]


non_parallel_methods = [Monocle2]
