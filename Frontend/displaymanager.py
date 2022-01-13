import pickle
import json
import glob
import os
import webbrowser
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.visualization.dfg import visualizer as dfg_visualization


class DisplayManager:
    
    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.config = config
    

    def display_petrinet(self, algo_name ):
        file_path = glob.glob(self.config["PATHS"]["VOLUME_PATH_MAC"]+algo_name+"/output_data/*.pnml")
        net, initial_marking, final_marking = pnml_importer.apply(file_path[0])
        gviz = pn_visualizer.apply(net, initial_marking, final_marking)
        pn_visualizer.view(gviz)
    
    def display_dfg(self , algo_name , log_direc ):
        file_path = glob.glob(self.config["PATHS"]["VOLUME_PATH_MAC"]+algo_name+"/output_data/*.pickle")
        with open(file_path[0], 'rb') as inputfile:
            print("input file",inputfile)
            output = pickle.load(inputfile)
            parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "png"}
            gviz = dfg_visualization.apply(output, log=log_direc, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
            dfg_visualization.view(gviz)

    def display_pdf(self,algo_name):
        file_path = glob.glob(self.config["PATHS"]["VOLUME_PATH_MAC"]+algo_name+"/output_data/*.pdf")
        webbrowser.open(r'file:///{file_name}'.format(file_name=file_path[0]))
        
