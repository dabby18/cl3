#include<iostream>
#include<omp.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
#include<sstream>
using namespace std;
int n=10;								
int partition(int a[],int p, int r);				
void quicksort(int a[], int p, int r)
{
	int q;
	if(p<r){	
		q=partition(a,p,r);				
		#pragma omp parallel sections
		{
			#pragma omp section
			{
				quicksort(a,p,q-1);
			}

			#pragma omp section
			{
				quicksort(a,q+1,r);
			}
		}
	}
}

int partition(int a[],int p, int r)
{
	int i=p-1;
	int x=a[r];
	int temp;
	for(int j=p; j<=r-1; j++)
	{
		if(a[j]<=x){
			i++;
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
	temp=a[i+1];
	a[i+1]=a[r];
	a[r]=temp;

	cout<<"\n ";
	for(int j=0; j<n; j++){
		cout<<"\t "<<a[j];
	}
return i+1;
}

int main()
{
	int temp,t=1;
	char ch;
	stringstream ss;
	
	ifstream in("demo.xml");
	string line;
	int a[10]={0,0,0,0,0,0,0,0,0,0};

	while(getline(in,line)){
		if(line=="<values>")	
			continue;
		else if(line=="<count>")
		{
			getline(in,line);
			ss.str(line);		
			ss>>temp;
			n=temp;
			cout<<"\nNo. of elements in array : "<<n;
			continue;
		}
		else if(line=="</count>")
			continue;
		else if(line=="/values")
			break;		
		else if(line=="<elements>")		
		{
			for(int i=0; i<n; i++){
			stringstream ss1;
			ss1.str("");
				getline(in,line);
				ss1.str("");
				ss1.str(line);
				ss1>>a[i];
			}
			continue;
		}
		else if(line=="</elements>")
			continue;
		else break;
	}
	cout<<"\n Unsorted array :   ";
	for(int i=0; i<n; i++)
        {
		cout<<a[i]<<"\t";
	}
	cout<<"\n";
	quicksort(a,0,n-1);				
	cout<<"\n\n Sorted array :  ";
	for(int i=0; i<n; i++)
        {
		cout<<a[i]<<"\t";
	}
cout<<"\n\n\n";
return 0;
}
