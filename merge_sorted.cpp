#include <iostream>
#include <vector>

std::vector<int> mergeSortedArrays(const std::vector<int>& arr1, const std::vector<int>& arr2) {
    std::vector<int> mergedArray;
    int i = 0, j = 0;

    while (i < arr1.size() && j < arr2.size()) {
        if (arr1[i] <= arr2[j]) {
            mergedArray.push_back(arr1[i]);
            ++i;
        } else {
            mergedArray.push_back(arr2[j]);
            ++j;
        }
    }

    // Append remaining elements from arr1
    while (i < arr1.size()) {
        mergedArray.push_back(arr1[i]);
        ++i;
    }

    // Append remaining elements from arr2
    while (j < arr2.size()) {
        mergedArray.push_back(arr2[j]);
        ++j;
    }

    return mergedArray;
}

int main() {
    std::vector<int> arr1 = {1, 3, 5, 7, 9};
    std::vector<int> arr2 = {2, 4, 6, 8, 10};

    std::vector<int> merged = mergeSortedArrays(arr1, arr2);

    std::cout << "Merged Sorted Array: ";
    for (int num : merged) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
