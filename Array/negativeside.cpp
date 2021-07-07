#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout<<"Enter the Element in array :-";
    cin>>n;
    int j;
    j=0;

    int a[100];
    for (int i = 0; i < n; i++)
    {
       cout<<"Enter the element :-";
       cin>>a[i];
    }
    
    for (int i = 0; i < n; i++)
    {
        if (a[i]<0)
        {
            
            swap(a[i],a[j]);
            j++;
            
        }
        
    }
    for (int i = 0; i < n; i++)
    {
       cout<<a[i];
    }
}    
    
