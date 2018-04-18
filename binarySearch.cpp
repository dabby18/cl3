#include<iostream>
using namespace std;
#include<algorithm>
int binarySearch(int *a, int low, int high, int key){
	if(low<=high){
		int mid = (low+high)/2;
		if(a[mid] == key)
			return mid+1;
		else if(a[mid] < key)
			low = mid + 1;
		else if(a[mid] > key)
			high = mid - 1;
			
		return binarySearch(a, low, high, key);
	}
	else return -1;
}

int main(){
	int n, key;
	cout<<"Enter Number of Elements: ";
	cin>>n;
	int a[n];
	for(int i = 0; i < n; i++){
		a[i] = rand() % 100;
	}
	
	cout<<"\nNumbers are: ";
	for(int i = 0; i < n; i++){
		cout<<a[i]<<" ";
	}
	
	sort(a, a+n);
	
	cout<<"\n\nSorted Numbers are: ";
	for(int i = 0; i < n; i++){
		cout<<a[i]<<" ";
	}
	
	cout<<"\n\nEnter key to search: ";
	cin>>key;
	int pos;
	pos = binarySearch(a, 0, n-1, key);
	
	if( pos != -1 )
		cout<<"Key "<<key<<" is found at position-> "<<pos<<endl;
	else
		cout<<"Key is not found!!\n";
	
	return 0;
}


/* OUTPUT

student@student:~$ g++ -o binarySearch binarySearch.cpp 
student@student:~$ ./binarySearch
Enter Number of Elements: 15

Numbers are: 83 86 77 15 93 35 86 92 49 21 62 27 90 59 63 

Sorted Numbers are: 15 21 27 35 49 59 62 63 77 83 86 86 90 92 93 

Enter key to search: 45
Key is not found!!
student@student:~$ ./binarySearch
Enter Number of Elements: 15

Numbers are: 83 86 77 15 93 35 86 92 49 21 62 27 90 59 63 

Sorted Numbers are: 15 21 27 35 49 59 62 63 77 83 86 86 90 92 93 

Enter key to search: 83
Key 83 is found at position-> 10
student@student:~$ ./binarySearch
Enter Number of Elements: 20

Numbers are: 83 86 77 15 93 35 86 92 49 21 62 27 90 59 63 26 40 26 72 36 

Sorted Numbers are: 15 21 26 26 27 35 36 40 49 59 62 63 72 77 83 86 86 90 92 93 

Enter key to search: 49
Key 49 is found at position-> 9
student@student:~$ 

*/
