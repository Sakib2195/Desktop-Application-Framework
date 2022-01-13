import sys
from fpdf import FPDF
from datetime import datetime
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay


log_file_name = sys.argv[1]
petrinet_file_name = sys.argv[2]

log_file_path = '/../token_based_replay/input_data/' + log_file_name

petrinet_file_path = '/../token_based_replay/input_data/' + petrinet_file_name

log = xes_importer.apply(log_file_path)

net, initial_marking, final_marking = pnml_importer.apply(petrinet_file_path)

replayed_traces = token_replay.apply(log, net, initial_marking, final_marking)
  
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B',size = 16)
pdf.cell(200, 10, txt = "Token based replay statistics", 
         ln = 1, align = 'C')

pdf.set_font("Arial", size = 14)
pdf.cell(200, 10, txt = "Log:{log} Petrinet:{petrinet}".format(log=log_file_name, petrinet=petrinet_file_name),
         ln = 2, align = 'C')

pdf.set_line_width(90.0)

for key, value in replayed_traces[0].items():
    width = len(str(key)) + len(str(value))
    print(width)
    if width < 90:
        pdf.cell(width, 10, txt = "{key} : {value}".format(key=key, value=value),
            ln = 2, align = 'L')
    else:
        
        text = str(key) + " : " + str(value)
        print(text)
        lines = round(width / 90, 0)
        print("lines {lines}".format(lines=lines))
        i = 0
        start = 0
        while i < lines:
            print("line number {no}".format(no=i))
            pdf.cell(90, 10, txt = text[start:start+90], ln = 2, align = 'L')
            start = start+90
            i=i+1

date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
pdf.output("/../token_based_replay/output_data/token_based_replay_stats_{date}.pdf".format(date=date))   