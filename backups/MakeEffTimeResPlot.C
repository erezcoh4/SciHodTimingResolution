
int Npoints = 0;


Float_t e , t , width , HV , threshold ;
std::vector<Float_t>     efficiency , time_res ;
TString SiPM , scintillator;
std::vector<TString>      Labels;
TPlots * plot = new TPlots();




void MakeEffTimeResPlot(){
    
    TCanvas * c = plot->CreateCanvas("EffTimeRes");
    ifstream InFile;
    InFile.open("csv_data/measurements.csv");
    while (!InFile.eof()) {

        InFile >> scintillator >> width >> SiPM >> HV >> threshold >> e >> t ;
        Labels.push_back(Form("%s %.0fmm + %s",scintillator,width,SiPM));
        efficiency.push_back(e);
        time_res.push_back(t);
        Npoints++;
        
    }


    
    TGraph *gr = new TGraph(Npoints);
    TExec *ex = new TExec("ex","drawAVD();");
    gr->GetListOfFunctions()->Add(ex);

    for (Int_t i = 0; i < Npoints ;i++){
        
        gr->SetPoint(i,efficiency[i],time_res[i]);
        
    }
    
    gr->SetTitle(" ; #sigma(#frac{L+R}{2}) [ps] ; #epsilon [%]");
    gr->Draw("AP");
}



void drawAVD()
{
    TLatex *l;
    Double_t x,y;
   
    TGraph *g = (TGraph*)gPad->GetListOfPrimitives()->FindObject("Graph");

    for (Int_t i = 0; i < Npoints ;i++) {
        g -> GetPoint(i,x,y);
        l = new TLatex(x,y,Labels[i]);
        l->SetTextSize(0.025);
        l->SetTextFont(42);
        l->SetTextAlign(21);
        l->Draw();
    }
}
