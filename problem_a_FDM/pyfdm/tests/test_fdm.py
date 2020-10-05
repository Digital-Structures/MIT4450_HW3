from os.path import abspath, dirname, join
import json

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pyfdm import compute_fdm

def test_fdm():
    here = abspath(dirname(__file__))
    data_file_path = join(here, 'fdm_init_data.json')
    with open(data_file_path) as json_file:
        data = json.load(json_file)
    
    node_coord = data['node_coord']
    edges = data['edge_node_ids']
    loads = data['nodal_loads']
    force_densities = data['force_densities']
    fixed = data['fixed_node_ids']
    
    fdm_node_coord = compute_fdm(node_coord, edges, loads, force_densities, fixed)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for n_ids in edges:
        ax.plot([fdm_node_coord[n_ids[0]][0], fdm_node_coord[n_ids[1]][0]], 
                [fdm_node_coord[n_ids[0]][1], fdm_node_coord[n_ids[1]][1]],
                zs=[fdm_node_coord[n_ids[0]][2], fdm_node_coord[n_ids[1]][2]],
                color='blue')

    plt.show()

if __name__ == '__main__':
    test_fdm()