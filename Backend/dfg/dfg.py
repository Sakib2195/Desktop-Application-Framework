import sys
import pickle
from datetime import datetime
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery



file_name = sys.argv[1]
file_path = '/../dfg/input_data/' + file_name
print(file_path)

log = xes_importer.apply(file_path)

dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

with open("/../dfg/output_data/output_dfg_{date}.pickle".format(date=date), 'wb') as outputfile:
    pickle.dump(dfg, outputfile)