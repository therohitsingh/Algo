# include <iostream> 
using namespace std; 
  
void rotate(int arr[], int n) 
{ 
    int x = arr[n - 1];
    
    for (int i = n - 1; i > 0; i--) 
    arr[i] = arr[i - 1];  
    arr[0] = x; 
} 
  
 
int main()  
{ 
    int i; 
    int n ;
    cout<<"Enter the no. of Element :-";
    cin>>n;
    int arr[100];
  
    cout << "Given array is \n"; 
    for (i = 0; i < n; i++) 
        
        cout <<"Enter the element:-";
        cin>>arr[i]; 
  
    rotate(arr, n); 
  
    cout << "\nRotated array is\n"; 
    for (i = 0; i < n; i++) 
        cout << arr[i]; 
  
    return 0; 
} 