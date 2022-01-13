import sys
from datetime import datetime
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter


file_name = sys.argv[1]
file_path = '/../alpha_miner/input_data/' + file_name

print(file_path)

log = xes_importer.apply(file_path)       

net, initial_marking, final_marking = alpha_miner.apply(log)

date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

pnml_exporter.apply(net=net, initial_marking=initial_marking, output_filename="/../alpha_miner/output_data/output_petrinet_{date}.pnml".format(date=date), final_marking=final_marking)