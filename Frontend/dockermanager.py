import os
import json
import time
import docker
import requests
from displaymanager import DisplayManager
from pm4py.objects.log.importer.xes import importer as xes_importer


class DockerManager:
    def __init__(self, client = docker.from_env()):
        self.client = client
    
    
    def list_algorithms(self):
        url = "http://localhost:5000/v2/_catalog"
        algo_list_request = requests.get(url)
        print(algo_list_request.json())
        return algo_list_request.json()


    
    def run_algorithm(self, algo_name, log_name , direc_name):
        with open('config.json', 'r') as f:
            config = json.load(f)
        print("algo_name: ",algo_name)
        log_direc = xes_importer.apply(direc_name)
        volumes= [config["PATHS"]["VOLUME_PATH_MAC"]+algo_name]
        volume_bindings = {
                            config["PATHS"]["VOLUME_PATH_MAC"]+algo_name: {
                                'bind': '/'+algo_name,
                                'mode': 'rw',
                            },
        }

        host_config = self.client.api.create_host_config(
                            binds=volume_bindings
        )

        container = self.client.api.create_container(
                            image= algo_name,
                            volumes=volumes,
                            host_config=host_config,
                            command= log_name
        ) 

        try:
            response = self.client.api.start(container=container.get('Id'))
        except Exception as e:
            print("Error From Docker:{error}".format(error=e))
            print("Container Logs:\n"+container.logs())

        time.sleep(5)
        display_manager = DisplayManager()
        
        test_path =  config["PATHS"]["VOLUME_PATH_MAC"]+algo_name+"/output_data/"
        files_test_path = os.listdir(test_path)
        for files in files_test_path:
            print("filess in o/p",files)
            if ".pickle" in files:
                display_manager.display_dfg(algo_name, log_direc)
            elif ".pnml" in files:
                display_manager.display_petrinet(algo_name)

        


    