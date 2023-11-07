import ROOT
import numpy as np

inFileName = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
treeFileName = "Events"
eventsnumber = 1000000
rootFileDirection = "/nfs/dust/cms/user/mueckejo/bachelorthesis_mueckejo/angularkinematics2023B/histrootfiles/"

print("starting the program")

#function loads the data and creates arrays (return 7 numpy arrays)
def load_data(fileName,treeName,evnum):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    event_number = evnum
    counter = 0

    pt1_values = np.empty(evnum)
    pt2_values = np.empty(evnum)
    y1_values = np.empty(evnum)
    y2_values = np.empty(evnum)
    yboost_values = np.empty(evnum)
    chi_values = np.empty(evnum)
    mjj_values = np.empty(evnum)


    for entry in tree:

        pt1 = entry.jetAK4_pt1
        pt2 = entry.jetAK4_pt1
        y1 = entry.jetAK4_y1
        y2 = entry.jetAK4_y2
        chi = entry.chi
        yboost = entry.yboost
        mjj = entry.mjj
        if mjj and pt1 and pt2 and y1 and y2 and chi and yboost != -999.0:
            pt1_values[counter] = pt1
            pt2_values[counter] = pt2
            y1_values[counter] = y1
            y2_values[counter] = y2
            yboost_values[counter] = yboost
            chi_values[counter] = chi
            mjj_values[counter] = mjj
        
        counter += 1
        if counter == event_number:
            break
            
    inFile.Close()
    return pt1_values,pt2_values,y1_values,y2_values,yboost_values,chi_values,mjj_values

#function takes hists as input and write them to a file
def write_hists(toutFileName,cms250to350hist, cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist):
    outHistFile = ROOT.TFile.Open(toutFileName,"RECREATE")
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
    print(toutFileName+"created")

#function takes data as numpy array and create histograms for different center of mass energies (saves the hist in root outfilename)
def create_hists(data,plotName,outFileName,loopingvariable,mjj,minimumrange,maximumrange,binnummer):

    hist_250to350 = ROOT.TH1D("250to350"+plotName+loopingvariable,"250to350"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_250to350.Sumw2()

    hist_350to500 = ROOT.TH1D("350to500"+plotName+loopingvariable,"350to500"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_350to500.Sumw2()

    hist_500to650 = ROOT.TH1D("500to650"+plotName+loopingvariable,"500to650"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_500to650.Sumw2()

    hist_650to850 = ROOT.TH1D("650to850"+plotName+loopingvariable,"650to850"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_650to850.Sumw2()

    hist_850to1100 = ROOT.TH1D("850to1100"+plotName+loopingvariable,"850to1100"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_850to1100.Sumw2()

    hist_1100to1400 = ROOT.TH1D("1100to1400"+plotName+loopingvariable,"1100to1400"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_1100to1400.Sumw2()

    hist_1400to1800 = ROOT.TH1D("1400to1800"+plotName+loopingvariable,"1400to1800"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_1400to1800.Sumw2()

    hist_1800to2200 = ROOT.TH1D("1800to2200"+plotName+loopingvariable,"1800to2200"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_1800to2200.Sumw2()

    hist_over2200 = ROOT.TH1D("over2200"+plotName+loopingvariable,"over2200"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over2200.Sumw2()

    for i in range(0,data.size):
        if 250 < mjj[i] < 350:
            hist_250to350.Fill(data[i])
        elif 350 < mjj[i] < 500:
            hist_350to500.Fill(data[i])
        elif 500 < mjj[i] < 650:
            hist_500to650.Fill(data[i])
        elif 650 < mjj[i] < 850:
            hist_650to850.Fill(data[i])
        elif 850 < mjj[i] < 1100:
            hist_850to1100.Fill(data[i])
        elif 1100 < mjj[i] < 1400:
            hist_1100to1400.Fill(data[i])
        elif 1400 < mjj[i] < 1800:
            hist_1400to1800.Fill(data[i])
        elif 1800 < mjj[i] < 2200:
            hist_1800to2200.Fill(data[i])
        elif 2200 < mjj[i]:
            hist_over2200.Fill(data[i])

    hist_250to350.SetDirectory(0)
    hist_350to500.SetDirectory(0)
    hist_500to650.SetDirectory(0)
    hist_650to850.SetDirectory(0) 
    hist_850to1100.SetDirectory(0)
    hist_1100to1400.SetDirectory(0)
    hist_1400to1800.SetDirectory(0)
    hist_1800to2200.SetDirectory(0)
    hist_over2200.SetDirectory(0)

    write_hists(outFileName,hist_250to350,hist_350to500,hist_500to650,hist_650to850,hist_850to1100,hist_1100to1400,hist_1400to1800,hist_1800to2200,hist_over2200)

#function takes only mjj hsit as input and write them to a file
def write_mjj_hist(toutFileName,cmsover250hist, cmsover350hist,cmsover500hist,cmsover650hist,cmsover850hist):
    
    outHistFile = ROOT.TFile.Open(toutFileName,"RECREATE")
    outHistFile.cd()
    cmsover250hist.Write()
    cmsover350hist.Write()
    cmsover500hist.Write()
    cmsover650hist.Write()
    cmsover850hist.Write()
    outHistFile.Close()
    print("mjjhistscreated")

#function takes data as numpy array and only creates the mjj histogram for different values (save the hsit in root outfilename)
def create_mjj_hists(data,plotName,outFileName,loopingvariable,minimumrange,maximumrange,binnummer):

    hist_over250 = ROOT.TH1D("over250"+plotName+loopingvariable,"over250"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over250.Sumw2()

    hist_over350 = ROOT.TH1D("over350"+plotName+loopingvariable,"over350"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over350.Sumw2()

    hist_over500 = ROOT.TH1D("over500"+plotName+loopingvariable,"over500"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over500.Sumw2()

    hist_over650 = ROOT.TH1D("over650"+plotName+loopingvariable,"over650"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over650.Sumw2()

    hist_over850 = ROOT.TH1D("over850"+plotName+loopingvariable,"over850"+plotName+loopingvariable,binnummer,minimumrange,maximumrange)
    hist_over850.Sumw2()

    for i in range(0,data.size):

        if 850 < data[i]:
            hist_over850.Fill(data[i])
        elif 650 < data[i]:
            hist_over650.Fill(data[i])
        elif 500 < data[i]:
            hist_over500.Fill(data[i])
        elif 350 < data[i]:
            hist_over350.Fill(data[i])
        elif 250 < data[i]:
            hist_over250.Fill(data[i])

    hist_over250.SetDirectory(0)
    hist_over350.SetDirectory(0)
    hist_over500.SetDirectory(0)
    hist_over650.SetDirectory(0) 
    hist_over850.SetDirectory(0)

    write_mjj_hist(outFileName,hist_over250,hist_over350,hist_over500,hist_over650,hist_over850)

#load the histogram data
pt1_values,pt2_values,y1_values,y2_values,yboost_values,chi_values,mjj_values = load_data(inFileName,treeFileName,eventsnumber)
print("Data succesfully loaded")

#function create and write the hists pt1
create_hists(pt1_values,"n from pt1 values for cmses",rootFileDirection+"pt1_histos_run2023B.root","pt1",mjj_values,0,1600,20)

#function create and write the hists pt2
create_hists(pt2_values,"n from pt2 values for cmses",rootFileDirection+"pt2_histos_run2023B.root","pt2",mjj_values,0,1600,20)

#function create and write the hists y1
create_hists(y1_values,"n from y1 values for cmses",rootFileDirection+"y1_histos_run2023B.root","y1",mjj_values,-6,6,50)

#function create and write the hists y2
create_hists(y2_values,"n from y2 values for cmses",rootFileDirection+"y2_histos_run2023B.root","y2",mjj_values,-6,6,50)

#function create and write the hists yboost
create_hists(yboost_values,"n from yboost values for cmses",rootFileDirection+"yboost_histos_run2023B.root","yboost",mjj_values,0,2,20)

#function create and write the hists chi
create_hists(chi_values,"n from chi values for cmses",rootFileDirection+"chi_histos_run2023B.root","chi",mjj_values,0,20,20)

#function create and write the hists mjj
create_mjj_hists(mjj_values,"n from pt1 values for cmses",rootFileDirection+"mjj_histos_run2023B.root","mjj",200,5000,10)

print("finish to create and save all histograms")