#include <iostream>
using namespace std;

int getCount(int arr[],int s, int e,  int pivot) {
    int count = 0;
    
    for(int i = s; i < e; i++) {
        if (arr[i] < pivot)
            count++;
    }

    return count;

}

int partition(int *arr, int s, int e) {
    // pivot ele
    int pivot = arr[s];

    // number of elements smaller than pivot element
    int count = getCount(arr,s, e, pivot);

    // correct position of pivot index
    int pivotIndex = s + count;

    swap(arr[pivotIndex], arr[s]);

    int i = s, j = e;

    while (i < pivotIndex && j > pivotIndex) {
        if (arr[i] < arr[pivotIndex]){
            i++;
        }
        
        else if (arr[j] > arr[pivotIndex]) {
            j--;
        }

        if (arr[i] > arr[pivotIndex] && arr[j] < arr[pivotIndex]) 
            swap(arr[i++], arr[j--]);
    }

    return pivotIndex;

}

void quickSort(int* arr, int s, int e) {
    if (s >= e){
        return;
    }

    int p = partition(arr, s, e);

    quickSort(arr, s, p - 1);
    quickSort(arr, p + 1, e);
}

int main () {

    int arr[10] = {234,432,234,231,12,432,1324,5432,234,453};
    
    int s = 0, e = 10 - 1;

    quickSort(arr,s , e );

    for(int i = 0; i < 10; i++){
        cout << arr[i] << " ";
    }

    return 0;
}
