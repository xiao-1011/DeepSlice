import brainrender
brainrender.SHADER_STYLE = "cartoon"
from brainrender.scene import Scene
import pandas as pd

def render_cells(cell_h5):
    cells = pd.read_hdf(cell_h5)
    print(cells)
    print(cells.shape)
    title = cell_h5[:-4] + 'rendered_cells'
    canvas = Scene(title = title, verbose=False)
    canvas.add_cells(cells)
    canvas.render()
    
