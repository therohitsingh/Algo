#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter the Element in array :-";
    cin>>n;

    int a[100];
    for (int i = 0; i < n; i++)
    {
       cout<<"Enter the element :-";
       cin>>a[i];
    }
    
    for (int i = n-1; i>=0; i--)
    {
        cout<<a[i];
    }
    
    
}