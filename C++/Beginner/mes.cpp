// Caio Cesar 30/11/23
// BEE 1052

#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
    map<int, string> meses = {{1, "January"}, {2, "February"}, {3, "March"}, {4, "April"}, {5, "May"}, 
                            {6, "June"}, {7, "July"}, {8, "August"}, {9, "September"}, {10, "October"}, 
                            {11, "November"}, {12, "December"}};
    int mes;

    cin >> mes;

    map<int, string>::iterator i;
    for(i = meses.begin(); i != meses.end(); i++){
        if(i->first == mes){
            cout << i->second << endl;
        }
    }

    return 0;
}