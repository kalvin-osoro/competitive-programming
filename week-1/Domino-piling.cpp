
#include <iostream>
# include <math.h>
using namespace std;



int main(){

    double m, n;



    cout << "Enter m and n \n";
    cin >> m >> n;
    double area = m * n;
    cout << area<< endl;

    double num = floor(area/2);

    cout << num<<endl;

    //cout<< num;

    return 0;

}
