#include<bits/stdc++.h>
using namespace std;
int main()
{
    char str[100],p[100];
    int i,x=0;
    cout<<"string : ";
    gets(str);
    int n=strlen(str);
    for(i=n,j;i>=0;i--)
    {
        p[x]=str[i];
        
    }
    
    if(str[i]==p[x])
    {
        cout<<"Palindrome";
    }
    else
    {
        cout<<"not palindrome";
    }
    

    

}