import ROOT

#download tree and load files inside (gives 7 files)
def getRootFiles(FileName,loopVariable):

    histFile = ROOT.TFile.Open(FileName,"READ")

    cms250to350hist = histFile.Get("250to350n from "+loopVariable+" values for cmses"+loopVariable)
    cms350to500hist = histFile.Get("350to500n from "+loopVariable+" values for cmses"+loopVariable)
    cms500to650hist = histFile.Get("500to650n from "+loopVariable+" values for cmses"+loopVariable)
    cms650to850hist = histFile.Get("650to850n from "+loopVariable+" values for cmses"+loopVariable)
    cms850to1100hist = histFile.Get("850to1100n from "+loopVariable+" values for cmses"+loopVariable)
    cms1100to1400hist = histFile.Get("1100to1400n from "+loopVariable+" values for cmses"+loopVariable)
    cms1400to1800hist = histFile.Get("1400to1800n from "+loopVariable+" values for cmses"+loopVariable)
    cms1800to2200hist = histFile.Get("1800to2200n from "+loopVariable+" values for cmses"+loopVariable)
    cmsover2200hist = histFile.Get("over2200n from "+loopVariable+" values for cmses"+loopVariable)

    cms250to350hist.SetDirectory(0)
    cms350to500hist.SetDirectory(0)
    cms500to650hist.SetDirectory(0)
    cms650to850hist.SetDirectory(0)
    cms850to1100hist.SetDirectory(0)
    cms1100to1400hist.SetDirectory(0)
    cms1400to1800hist.SetDirectory(0)
    cms1800to2200hist.SetDirectory(0)
    cmsover2200hist.SetDirectory(0)

    histFile.Close()
    print(FileName+" is loaded")
    return cms250to350hist,cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist

#save the files in one pdf (prints the pdf in directory)
def saveHistasPdf(FileName,PlotName,LoopVariable,directoryR,directoryP,title):
    getFileName = directoryR + FileName
    putFileName = directoryP + PlotName

    cms250to350hist,cms350to500hist,cms500to650hist,cms650to850hist,cms850to1100hist,cms1100to1400hist,cms1400to1800hist,cms1800to2200hist,cmsover2200hist = getRootFiles(getFileName,LoopVariable)

    canvas = ROOT.TCanvas("canvas")
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    canvas.Print(putFileName+"[")
    #create cms250to350hist pdf
    cms250to350hist.SetStats(0)
    cms250to350hist.SetLineColor(ROOT.kRed)
    cms250to350hist.SetLineWidth(2)
    cms250to350hist.GetYaxis().SetTitle("N")
    cms250to350hist.GetXaxis().SetTitle(title)
    cms250to350hist.SetTitle("cms250to350hist")
    cms250to350hist.Draw("h")
    legend1 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend1.SetLineWidth(0)
    legend1.AddEntry(cms250to350hist,"data")
    legend1.Draw("same")
    latex.DrawText(0.5,0.8,"250 < M_{jj} [GeV] < 350")
    canvas.Print(putFileName)
    print("created plot")
    #create cms350to500hist pdf
    cms350to500hist.SetStats(0)
    cms350to500hist.SetLineColor(ROOT.kRed)
    cms350to500hist.SetLineWidth(2)
    cms350to500hist.GetYaxis().SetTitle("N")
    cms350to500hist.GetXaxis().SetTitle(title)
    cms350to500hist.SetTitle("cms350to500hist")
    cms350to500hist.Draw("h")
    legend2 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend2.SetLineWidth(0)
    legend2.AddEntry(cms250to350hist,"data")
    legend2.Draw("same")
    latex.DrawText(0.5,0.8,"350 < M_{jj} [GeV] < 500")
    canvas.Print(putFileName)
    print("created plot")
    #create cms500to650hist pdf
    cms500to650hist.SetStats(0)
    cms500to650hist.SetLineColor(ROOT.kRed)
    cms500to650hist.SetLineWidth(2)
    cms500to650hist.GetYaxis().SetTitle("N")
    cms500to650hist.GetXaxis().SetTitle(title)
    cms500to650hist.SetTitle("cms500to650hist")
    cms500to650hist.Draw("h")
    legend3 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend3.SetLineWidth(0)
    legend3.AddEntry(cms250to350hist,"data")
    legend3.Draw("same")
    latex.DrawText(0.5,0.8,"500 < M_{jj} [GeV] < 650")
    canvas.Print(putFileName)
    print("created plot")
    #create cms650to850hist pdf
    cms650to850hist.SetStats(0)
    cms650to850hist.SetLineColor(ROOT.kRed)
    cms650to850hist.SetLineWidth(2)
    cms650to850hist.GetYaxis().SetTitle("N")
    cms650to850hist.GetXaxis().SetTitle(title)
    cms650to850hist.SetTitle("cms650to850hist")
    cms650to850hist.Draw("h")
    legend4 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend4.SetLineWidth(0)
    legend4.AddEntry(cms250to350hist,"data")
    legend4.Draw("same")
    latex.DrawText(0.5,0.8,"650 < M_{jj} [GeV] < 850")
    canvas.Print(putFileName)
    print("created plot")
    #create cms850to1100hist pdf
    cms850to1100hist.SetStats(0)
    cms850to1100hist.SetLineColor(ROOT.kRed)
    cms850to1100hist.SetLineWidth(2)
    cms850to1100hist.GetYaxis().SetTitle("N")
    cms850to1100hist.GetXaxis().SetTitle(title)
    cms850to1100hist.SetTitle("cms850to1100hist")
    cms850to1100hist.Draw("h")
    legend5 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend5.SetLineWidth(0)
    legend5.AddEntry(cms250to350hist,"data")
    legend5.Draw("same")
    latex.DrawText(0.5,0.8,"850 < M_{jj} [GeV] < 1100")
    canvas.Print(putFileName)
    print("created plot")
    #create cms1100to1400hist pdf
    cms1100to1400hist.SetStats(0)
    cms1100to1400hist.SetLineColor(ROOT.kRed)
    cms1100to1400hist.SetLineWidth(2)
    cms1100to1400hist.GetYaxis().SetTitle("N")
    cms1100to1400hist.GetXaxis().SetTitle(title)
    cms1100to1400hist.SetTitle("cms1100to1400hist")
    cms1100to1400hist.Draw("h")
    legend6 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend6.SetLineWidth(0)
    legend6.AddEntry(cms250to350hist,"data")
    legend6.Draw("same")
    latex.DrawText(0.5,0.8,"1100 < M_{jj} [GeV] < 1400")
    canvas.Print(putFileName)
    print("created plot")
    #create cms1400to1800hist pdf
    cms1400to1800hist.SetStats(0)
    cms1400to1800hist.SetLineColor(ROOT.kRed)
    cms1400to1800hist.SetLineWidth(2)
    cms1400to1800hist.GetYaxis().SetTitle("N")
    cms1400to1800hist.GetXaxis().SetTitle(title)
    cms1400to1800hist.SetTitle("cms1400to1800hist")
    cms1400to1800hist.Draw("h")
    legend7 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend7.SetLineWidth(0)
    legend7.AddEntry(cms250to350hist,"data")
    legend7.Draw("same")
    latex.DrawText(0.5,0.8,"1400 < M_{jj} [GeV] < 1800")
    canvas.Print(putFileName)
    print("created plot")
    #create cms1800to2200hist pdf
    cms1800to2200hist.SetStats(0)
    cms1800to2200hist.SetLineColor(ROOT.kRed)
    cms1800to2200hist.SetLineWidth(2)
    cms1800to2200hist.GetYaxis().SetTitle("N")
    cms1800to2200hist.GetXaxis().SetTitle(title)
    cms1800to2200hist.SetTitle("cms1800to2200hist")
    cms1800to2200hist.Draw("h")
    legend8 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend8.SetLineWidth(0)
    legend8.AddEntry(cms250to350hist,"data")
    legend8.Draw("same")
    latex.DrawText(0.5,0.8,"1800 < M_{jj} [GeV] < 2200")
    canvas.Print(putFileName)
    print("created plot")
    #create cmsover2200hist pdf
    cmsover2200hist.SetStats(0)
    cmsover2200hist.SetLineColor(ROOT.kRed)
    cmsover2200hist.SetLineWidth(2)
    cmsover2200hist.GetYaxis().SetTitle("N")
    cmsover2200hist.GetXaxis().SetTitle(title)
    cmsover2200hist.SetTitle("cmsover2200hist")
    cmsover2200hist.Draw("h")
    legend9 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend9.SetLineWidth(0)
    legend9.AddEntry(cms250to350hist,"data")
    legend9.Draw("same")
    latex.DrawText(0.5,0.8,"2200 < M_{jj} [GeV]")
    canvas.Print(putFileName)
    print("created plot")
    canvas.Print(putFileName+"]")
    print("pdf "+FileName+"is created")

#download tree and load files inside (gives 7 files) only for Mjj
def getMjjRootFiles(FileName):

    histFile = ROOT.TFile.Open(FileName,"READ")

    hist_over250 = histFile.Get("over250n from pt1 values for cmsesmjj")
    hist_over350 = histFile.Get("over350n from pt1 values for cmsesmjj")
    hist_over500 = histFile.Get("over500n from pt1 values for cmsesmjj")
    hist_over650 = histFile.Get("over650n from pt1 values for cmsesmjj")
    hist_over850 = histFile.Get("over850n from pt1 values for cmsesmjj")

    hist_over250.SetDirectory(0)
    hist_over350.SetDirectory(0)
    hist_over500.SetDirectory(0)
    hist_over650.SetDirectory(0)
    hist_over850.SetDirectory(0)

    histFile.Close()
    print(FileName+" is loaded")
    return hist_over250,hist_over350,hist_over500,hist_over650,hist_over850

#save the files in one pdf (prints the pdf in directory) only for mjj
def saveMjjHistasPdf(FileName,PlotName,directoryR,directoryP):
    getFileName = directoryR + FileName
    putFileName = directoryP + PlotName

    hist_over250,hist_over350,hist_over500,hist_over650,hist_over850 = getMjjRootFiles(getFileName)

    canvas = ROOT.TCanvas("canvas")
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    canvas.Print(putFileName+"[")
    #create hist_over250 pdf
    hist_over250.SetStats(0)
    hist_over250.SetLineColor(ROOT.kRed)
    hist_over250.SetLineWidth(2)
    hist_over250.GetYaxis().SetTitle("N")
    hist_over250.GetXaxis().SetTitle("M_{jj} [GeV]")
    hist_over250.SetTitle("hist_over250")
    hist_over250.Draw("h")
    legend1 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend1.SetLineWidth(0)
    legend1.AddEntry(hist_over250,"data")
    legend1.Draw("same")
    latex.DrawText(0.5,0.8,"250 < M_{jj} [GeV]")
    canvas.Print(putFileName)
    print("created plot")
    #create hist_over350 pdf
    hist_over350.SetStats(0)
    hist_over350.SetLineColor(ROOT.kRed)
    hist_over350.SetLineWidth(2)
    hist_over350.GetYaxis().SetTitle("N")
    hist_over350.GetXaxis().SetTitle("M_{jj} [GeV]")
    hist_over350.SetTitle("hist_over350")
    hist_over350.Draw("h")
    legend2 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend2.SetLineWidth(0)
    legend2.AddEntry(hist_over350,"data")
    legend2.Draw("same")
    latex.DrawText(0.5,0.8,"350 < M_{jj} [GeV]")
    canvas.Print(putFileName)
    print("created plot")
    #create hist_over500 pdf
    hist_over500.SetStats(0)
    hist_over500.SetLineColor(ROOT.kRed)
    hist_over500.SetLineWidth(2)
    hist_over500.GetYaxis().SetTitle("N")
    hist_over500.GetXaxis().SetTitle("M_{jj} [GeV]")
    hist_over500.SetTitle("hist_over500")
    hist_over500.Draw("h")
    legend3 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend3.SetLineWidth(0)
    legend3.AddEntry(hist_over500,"data")
    legend3.Draw("same")
    latex.DrawText(0.5,0.8,"500 < M_{jj}")
    canvas.Print(putFileName)
    print("created plot")
    #create hist_over650 pdf
    hist_over650.SetStats(0)
    hist_over650.SetLineColor(ROOT.kRed)
    hist_over650.SetLineWidth(2)
    hist_over650.GetYaxis().SetTitle("N")
    hist_over650.GetXaxis().SetTitle("M_{jj} [GeV]")
    hist_over650.SetTitle("hist_over650")
    hist_over650.Draw("h")
    legend4 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend4.SetLineWidth(0)
    legend4.AddEntry(hist_over650,"data")
    legend4.Draw("same")
    latex.DrawText(0.5,0.8,"650 < M_{jj} [GeV]")
    canvas.Print(putFileName)
    print("created plot")
    #create hist_over850 pdf
    hist_over850.SetStats(0)
    hist_over850.SetLineColor(ROOT.kRed)
    hist_over850.SetLineWidth(2)
    hist_over850.GetYaxis().SetTitle("N")
    hist_over850.GetXaxis().SetTitle("M_{jj} [GeV]")
    hist_over850.SetTitle("hist_over850")
    hist_over850.Draw("h")
    legend5 = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend5.SetLineWidth(0)
    legend5.AddEntry(hist_over850,"data")
    legend5.Draw("same")
    latex.DrawText(0.5,0.8,"850 < M_{jj} [GeV]")
    canvas.Print(putFileName)
    print("created plot")
    canvas.Print(putFileName+"]")
    print("pdf "+FileName+"is created")

#define director path for the pdf files
directoryRoot = "/nfs/dust/cms/user/mueckejo/bachelorthesis_mueckejo/angularkinematics2023B/histrootfiles/"
directoryPdf = "/nfs/dust/cms/user/mueckejo/bachelorthesis_mueckejo/angularkinematics2023B/histpdffiles/"

#Write pdf for pt1 Value
saveHistasPdf("pt1_histos_run2023B.root","pt1_histos_run2023B.pdf","pt1",directoryRoot,directoryPdf,"P_{T1} [GeV]")

#Write pdf for pt2 Value
saveHistasPdf("pt2_histos_run2023B.root","pt2_histos_run2023B.pdf","pt2",directoryRoot,directoryPdf,"P_{T2} [GeV]")

#Write pdf for y1 Value
saveHistasPdf("y1_histos_run2023B.root","y1_histos_run2023B.pdf","y1",directoryRoot,directoryPdf,"Y_{1}")

#Write pdf for y2 Value
saveHistasPdf("y2_histos_run2023B.root","y2_histos_run2023B.pdf","y2",directoryRoot,directoryPdf,"Y_{2}")

#Write pdf for yboost Value
saveHistasPdf("yboost_histos_run2023B.root","yboost_histos_run2023B.pdf","yboost",directoryRoot,directoryPdf,"Y_{boost}")

#Write pdf for chi Value
saveHistasPdf("chi_histos_run2023B.root","chi_histos_run2023B.pdf","chi",directoryRoot,directoryPdf,"Chi_{dijet}")

#Write pdf for mjj Value
saveMjjHistasPdf("mjj_histos_run2023B.root","mjj_histos_run2023B.pdf",directoryRoot,directoryPdf)
