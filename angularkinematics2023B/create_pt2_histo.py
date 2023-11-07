import ROOT
#import sys
import numpy as np

#if len(sys.argv) != 3:
#    print("USAGE: %s <input file> <output file>"%(sys.argv[0]))
#    sys.exit(1)

#inFileName = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
#outFileName = "pt2_histos_run2023B.root"
#treeFileName = "Events"

#print("Reading from",inFileName,"and writing to",outFileName)

def create_hists(fileName,plotName,treeName,evnum):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    hist_shown_variable = "pt2"

    hist_250to350 = ROOT.TH1D("250to350"+plotName+hist_shown_variable,"250to350"+plotName+hist_shown_variable,50,0,2.e3)
    hist_250to350.Sumw2()

    hist_350to500 = ROOT.TH1D("350to500"+plotName+hist_shown_variable,"350to500"+plotName+hist_shown_variable,50,0,2.e3)
    hist_350to500.Sumw2()

    hist_500to650 = ROOT.TH1D("500to650"+plotName+hist_shown_variable,"500to650"+plotName+hist_shown_variable,50,0,2.e3)
    hist_500to650.Sumw2()

    hist_650to850 = ROOT.TH1D("650to850"+plotName+hist_shown_variable,"650to850"+plotName+hist_shown_variable,50,0,2.e3)
    hist_650to850.Sumw2()

    hist_850to1100 = ROOT.TH1D("850to1100"+plotName+hist_shown_variable,"850to1100"+plotName+hist_shown_variable,50,0,2.e3)
    hist_850to1100.Sumw2()

    hist_1100to1400 = ROOT.TH1D("1100to1400"+plotName+hist_shown_variable,"1100to1400"+plotName+hist_shown_variable,50,0,2.e3)
    hist_1100to1400.Sumw2()

    hist_1400to1800 = ROOT.TH1D("1400to1800"+plotName+hist_shown_variable,"1400to1800"+plotName+hist_shown_variable,50,0,2.e3)
    hist_1400to1800.Sumw2()

    hist_1800to2200 = ROOT.TH1D("1800to2200"+plotName+hist_shown_variable,"1800to2200"+plotName+hist_shown_variable,50,0,2.e3)
    hist_1800to2200.Sumw2()

    hist_over2200 = ROOT.TH1D("over2200"+plotName+hist_shown_variable,"over2200"+plotName+hist_shown_variable,50,0,2.e3)
    hist_over2200.Sumw2()

    event_number = evnum
    counter = 0

    for entry in tree:

        counter += 1
        if counter == event_number:
            break

        #calculate center of mass energy
        mjj = entry.mjj
        pt2 = entry.jetAK4_pt2
        if mjj != -999.0:
            if 250 < mjj < 350:
                hist_250to350.Fill(pt2)
            elif 350 < mjj < 500:
                hist_350to500.Fill(pt2)
            elif 500 < mjj < 650:
                hist_500to650.Fill(pt2)
            elif 650 < mjj < 850:
                hist_650to850.Fill(pt2)
            elif 850 < mjj < 1100:
                hist_850to1100.Fill(pt2)
            elif 1100 < mjj < 1400:
                hist_1100to1400.Fill(pt2)
            elif 1400 < mjj < 1800:
                hist_1400to1800.Fill(pt2)
            elif 1800 < mjj < 2200:
                hist_1800to2200.Fill(pt2)
            elif 2200 < mjj:
                hist_over2200.Fill(pt2)

    hist_250to350.SetDirectory(0)
    hist_350to500.SetDirectory(0)
    hist_500to650.SetDirectory(0)
    hist_650to850.SetDirectory(0) 
    hist_850to1100.SetDirectory(0)
    hist_1100to1400.SetDirectory(0)
    hist_1400to1800.SetDirectory(0)
    hist_1800to2200.SetDirectory(0)
    hist_over2200.SetDirectory(0)
    inFile.Close()

    return hist_250to350,hist_350to500,hist_500to650,hist_650to850,hist_850to1100,hist_1100to1400,hist_1400to1800,hist_1800to2200,hist_over2200
