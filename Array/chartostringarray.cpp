#include<bits/stdc++.h>
using namespace std;

int main(){

string s ;
cout<<"Enter the string you want :-";
cin>>s;

int n = s.length();

char carr[n+1];

strcpy(carr,s.c_str());
for (int i = 0; i < n; i++)
{
   cout<<carr[i];
}

return 0;

}