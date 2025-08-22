#!/usr/bin/python
import argparse
import sys
aparser = argparse.ArgumentParser(description='A tool to help calculate hbA1C from average blood glucose and vice-versa.')
aparser.add_argument("--avg", type=float, default=None)
aparser.add_argument("--long-term", type=float, default=None)
aparser.add_argument("--dcct", default=False, action='store_true')
args=aparser.parse_args()
avg=args.avg
isdcct=args.dcct
longterm=args.long_term
if avg is None and longterm is None:
    print("At least one of --avg and --long-term values needs to be supplied.")
    sys.exit(-1)
if avg is not None and longterm is not None:
    print("Both --avg and --long-term cannot be supplied simultaneously.")
    sys.exit(-1)

if avg is not None:
    if isdcct:
        avg_mgdl = avg
        avg_ifcc = avg/18
        dcct=(avg_mgdl+46.7)/28.7
        hba1c=dcct*10.93-23.5
        print("Input average blood glucose: %d mg/dl (%0.1f mmol)")%(int(avg),avg_ifcc)
        print("The computed hbA1C value is %.1f%% (IFCC %d mmol/mol)"%(dcct,int(hba1c)))
    else:
        avg_mgdl = avg*18
        dcct=(avg_mgdl+46.7)/28.7
        hba1c=dcct*10.93-23.5
        print("Input average blood glucose: %0.1f mmol/l (%d mg/dl)")%(avg,int(avg_mgdl))
        print("The computed hbA1C value is %d mmol/mol(DCCT %.1f%%)"%(int(hba1c),dcct))
else:
    if isdcct:
        eag=(28.7*longterm)-46.7
        eag_ifcc = eag/18
        hba1c=longterm*10.93-23.5
        print("Input weighted blood glucose (hbA1C): %0.1f%% (IFCC %d mmol/mol)"%(longterm,int(hba1c))) 
        print("The computed average blood glucose value: %d mg/dl (%0.1f mmol)"%(int(eag),eag_ifcc))
    else:
        dcct=(longterm+23.5)/10.93
        avg=dcct*28.7-46.7
        avg_ifcc= avg/18
        print("Input weighted blood glucose (hbA1C): %d mmol/mol (DCCT %0.1f%%)"%(int(longterm),dcct))
        print("The computed average blood glucose value: %0.1f mmol (%d mg/dl)"%(avg_ifcc,int(avg)))
