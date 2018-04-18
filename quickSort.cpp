#include<iostream>
using namespace std;
#include<stdlib.h>
#include<stdio.h>
#include<omp.h>
#define MAX 20


class QuickSort{
public:
	void quickSort(int *a, int p, int r);
	int partition(int *a, int p, int r);
};

void QuickSort:: quickSort(int *a, int p, int r){
	if(p < r){
		int q = partition(a, p, r);
		omp_set_nested(1);
		#pragma omp parallel sections
		{
			#pragma omp section
			{
				printf("\nThread %d is executing from index %d to %d", omp_get_thread_num(), p, q-1);
				quickSort(a, p, q-1);
			}
			#pragma omp section
			{
				printf("\nThread %d is executing from index %d to %d", omp_get_thread_num(), q+1, r);
				quickSort(a, q+1, r);
			}
		}
	}
}

int QuickSort:: partition(int *a, int p, int r){
	int pivot = a[r];
	int i = p-1;
	for(int j = p; j < r; j++){
		if(a[j] <= pivot){
			i++;
			int temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
	}
	
	int temp = a[i+1];
	a[i+1] = a[r];
	a[r] = temp;
	
	return (i+1);
}

int main(){
	int a[MAX];
	for(int i = 0; i < MAX; i++)
		a[i] = rand()%100;

	cout<<"Initial Sequence: ";
	for(int i = 0; i < MAX; i++)
		cout<<a[i]<<"\t";
	cout<<endl;
	QuickSort q;
	
	double start = omp_get_wtime();
	q.quickSort(a, 0, MAX-1);
	double finish = omp_get_wtime();
	
	cout<<"\n\nSorted Sequence: ";
	for(int i = 0; i < MAX; i++)
		cout<<a[i]<<"\t";
	cout<<"\n\nExecution Time: "<<finish-start<<endl;

	return 0;
}
