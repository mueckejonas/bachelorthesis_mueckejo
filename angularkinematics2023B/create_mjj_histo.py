import ROOT
#import sys
import numpy as np

#if len(sys.argv) != 3:
#    print("USAGE: %s <input file> <output file>"%(sys.argv[0]))
#    sys.exit(1)

#inFileName = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
#outFileName = "mjj_histos_run2023B.root"
#treeFileName = "Events"

#print("Reading from",inFileName,"and writing to",outFileName)

def create_hists(fileName,plotName,treeName,evnum):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    hist_shown_variable = "mjj"

    hist_over250 = ROOT.TH1D("over250"+plotName+hist_shown_variable,"over250"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over250.Sumw2()

    hist_over350 = ROOT.TH1D("over350"+plotName+hist_shown_variable,"over350"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over350.Sumw2()

    hist_over500 = ROOT.TH1D("over500"+plotName+hist_shown_variable,"over500"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over500.Sumw2()

    hist_over650 = ROOT.TH1D("over650"+plotName+hist_shown_variable,"over650"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over650.Sumw2()

    hist_over850 = ROOT.TH1D("over850"+plotName+hist_shown_variable,"over850"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over850.Sumw2()

    event_number = evnum
    counter = 0

    for entry in tree:

        counter += 1
        if counter == event_number:
            break

        #calculate center of mass energy
        mjj = entry.mjj
        if mjj != -999.0:
            if 250 < mjj:
                hist_over250.Fill(mjj)
            elif 350 < mjj:
                hist_over350.Fill(mjj)
            elif 500 < mjj:
                hist_over500.Fill(mjj)
            elif 650 < mjj:
                hist_over650.Fill(mjj)
            elif 850 < mjj:
                hist_over850.Fill(mjj)

    hist_over250.SetDirectory(0)
    hist_over350.SetDirectory(0)
    hist_over500.SetDirectory(0)
    hist_over650.SetDirectory(0) 
    hist_over850.SetDirectory(0)
    inFile.Close()

    return hist_over250,hist_over350,hist_over500,hist_over650,hist_over850