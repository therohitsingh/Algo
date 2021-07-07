#include<iostream>
using namespace std;

int main(){

   int n;
   int arr[100];
   cout<<"Enter the no. you want to enter:-";
   cin>>n;

   for(int i=0;i<n;i++){

       cout<<"Enter the no :-";
       cin>>arr[i];
   }
   for(int i = 0;i<n;i++){

       cout<<arr[i];
   }



}