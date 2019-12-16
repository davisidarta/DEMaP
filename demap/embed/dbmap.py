from dbmap.diffusion import Run_Diffusion
from dbmap.dbmap import Run_dbMAP

def dbMAP(data):
    res = Run_Diffusion(data)
    diff = res['DiffusionComponents']
    result = Run_dbMAP(diff, min_dist = 1)
    return result
