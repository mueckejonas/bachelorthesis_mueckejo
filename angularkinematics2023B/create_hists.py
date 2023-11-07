import ROOT
import numpy as np
import create_pt1_histo
import create_pt2_histo
import create_y1_histo
import create_y2_histo
import create_yboost_histo
import create_Xdijet_histo
import create_mjj_histo

inFileName = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
treeFileName = "Events"
eventsnumber = 1000000
rootFileDirection = "/nfs/dust/cms/user/mueckejo/bachelorthesis_mueckejo/angularkinematics2023B/histrootfiles/"

def create_pt1_hists():
    outFileName = rootFileDirection+"pt1_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_pt1_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("pt1histscreated")

def create_pt2_hists():
    outFileName = rootFileDirection+"pt2_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_pt2_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("pt2histscreated")

def create_y1_hists():
    outFileName = rootFileDirection+"y1_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_y1_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("y1histscreated")

def create_y2_hists():
    outFileName = rootFileDirection+"y2_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_y2_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("y2histscreated")

def create_yboost_hists():
    outFileName = rootFileDirection+"yboost_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_yboost_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("yboosthistscreated")

def create_Xdijet_hists():
    outFileName = rootFileDirection+"Xdijet_histos_run2023B.root"
    cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = create_Xdijet_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cms250to350hist.Write()
    cms350to500hist.Write()
    cms500to650hist.Write()
    cms650to850hist.Write()
    cms850to1100hist.Write()
    cms1100to1400hist.Write()
    cms1400to1800hist.Write()
    cms1800to2200hist.Write()
    cmsover2200hist.Write()
    outHistFile.Close()
    print("xdijethistscreated")

def create_mjj_hists():
    outFileName = rootFileDirection+"mjj_histos_run2023B.root"
    cmsover250hist, cmsover350hist,cmsover500hist,cmsover650hist,cmsover850hist = create_mjj_histo.create_hists(inFileName,outFileName,treeFileName,eventsnumber)

    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    cmsover250hist.Write()
    cmsover350hist.Write()
    cmsover500hist.Write()
    cmsover650hist.Write()
    cmsover850hist.Write()
    outHistFile.Close()
    print("mjjhistscreated")

create_pt1_hists()
create_pt2_hists()
create_y1_hists()
create_y2_hists()
create_yboost_hists()
create_Xdijet_hists()
create_mjj_hists()






