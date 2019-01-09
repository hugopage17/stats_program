from data import Data
from time import sleep
from graph import Graph
from normal_distribution import NormalDistribution
from confidence_intervals import Confidence_Intervals as CI
import os

def main():
    data = Data()
    command = input()
    if (command[:2]) == 'cd':
        new_dir = command[5:]
        new_dir = new_dir.replace('"', "")
        os.chdir(new_dir)
        print(new_dir)
    elif (command[:8]) == 'run_data':
        data_set = command[11:]
        try:
            data.load_data(data_set)
        except:
            print('Data failed to load, please check your directory and try again')
        while data.is_loaded == True:
            sub_command = input()
            if sub_command == 'get_results':
                nd = NormalDistribution(data.num_list)
                ci_mean = CI.sample_mean(nd.mean, nd.std, nd.N)
            elif sub_command == 'graph':
                graph = Graph(data.x_axis, data.num_list)

while True:
    main()
