#importing ROOT
import ROOT
from decimal import Decimal
import math
import numpy as np

#defining root input file paths and root output file path
inFileName1 = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
outFileName1 = "AnalyzeData.root"

#create and fill the hist with input data to calculate Center Mass
def create_Masshist(inFile_Name,tree_name,hist_name):
    inFile = ROOT.TFile.Open(inFile_Name,"READ")
    tree = inFile.Get(tree_name)

    hist = ROOT.TH1D(hist_name,"data_"+hist_name,500,0,2.e6)
    hist.Sumw2()

    counter = 0

    for entry in tree:
        counter += 1
        if counter == 100000:
            break
        pt1 = entry.jetAK4_pt1
        pt2 = entry.jetAK4_pt2
        y1 = entry.jetAK4_y1
        y2 = entry.jetAK4_y2
        
        if pt1 and pt2 and y1 and y2 != -999.0:
            hist.Fill(2*pt1*pt2*np.exp(abs(y1-y2)))

    hist.SetDirectory(0)
    inFile.Close()
    return hist

#create and fill the hist with input data to calculate Angular Distribution
def create_Angularhist(inFile_Name,tree_name,hist_name):
    inFile = ROOT.TFile.Open(inFile_Name,"READ")
    tree = inFile.Get(tree_name)

    hist = ROOT.TH1D(hist_name,"data_"+hist_name,500,0,10)
    hist.Sumw2()

    #sigma in femtobarn
    sigma = 222839

    counter = 0

    for entry in tree:
        counter += 1
        if counter == 100000:
            break
        y1 = entry.jetAK4_y1
        y2 = entry.jetAK4_y2
        if y1 and y2 != -999.0:
            X_dijet = np.exp(abs(y1-y2))
            hist.Fill(1/((1-np.cos(X_dijet))**2))

    hist.SetDirectory(0)
    inFile.Close()
    return hist

#create hists
file1_hist = create_Masshist(inFileName1,"Events","CenterMass_hist")
file2_hist = create_Angularhist(inFileName1,"Events","AngulasDistrubution_hist")

#writing the output root file
outHistFile = ROOT.TFile.Open(outFileName1,"RECREATE")
outHistFile.cd()
file1_hist.Write()
file2_hist.Write()
outHistFile.Close()

