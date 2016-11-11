// create a visual plot from all Tiko' measurements during May-Aug 2016
#include </Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/myIncludes.h>

TAnalysis * ana = new TAnalysis();
TPlots * plot = new TPlots();



// main functionality: create timing-resolution plots...
void MeasuredTimeResSummer2016(){

    const int N = 3;
    double x[N] , y[N];
    ifstream f("csv_data/measurements.csv");
    
    
    
    ana -> ReadGraphFromFile("csv_data/measurements.csv", N , x , y );
    
    for (int i = 0 ; i < N ; i++) {
        SHOW(x[N]);
        SHOW(y[N]);
    }
    
}