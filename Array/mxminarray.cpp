#include<iostream>
using namespace std;

int main()
{
    int n ;
    cout<<"Enter the no. of elements in array:-";
    cin>>n;
    int a[100];
    int max;
    int min;

    for (int i = 0; i < n; i++)
    {
        cout<<"Enter the element:-";
        cin>>a[i];
    }
    
    min = a[0];
    for (int i = 0; i < n; i++)
    {
        if (min > a[i])
        {
            min = a[i];
        }
        
    }
     
    max = a[0];
    for (int i = 0; i < n; i++)
    {
        if (max < a[i])
        {
            max = a[i];
        }
        
    }
    
    cout<<"The smallest element is :-"<<min<<endl;
    cout<<"The greatest element is:-"<<max<<endl;


}