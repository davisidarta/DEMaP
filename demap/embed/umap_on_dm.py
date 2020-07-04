from .umap import UMAP
from .dm import DM


def UMAP_on_DM(data, **kwargs):
    return UMAP(DM(data, **kwargs))
