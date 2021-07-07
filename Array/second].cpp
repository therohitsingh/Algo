#include <iostream>
using namespace std;

int main(){


   int n;
   int f;
   int arr[100];
   cout<<"Enter the no. you want to enter:-";
   cin>>n;
    int m;
   cout<<"Enter the no. you want to search for:-";
   cin>>m;

   for(int i=0;i<n;i++){

       cout<<"Enter the no :-";
       cin>>arr[i];
   }
   f = 0;
   for (int j = 0; j < n; j++)
   {
      if(m==arr[j])
      {
          f = 1;
          break;
          
      }
      
    
      
   }
   if (f>=0)
   {
     cout<<"the searched element is found";

   }
   else
   {
     cout<<"Not found";
   }
   
   {
     /* code */
   }
   
   
}