#include <iostream>
#include <vector>
#include <chrono>
using namespace std;


void solution_one(vector<int> nums){
    for(int i = 0; i < nums.size(); i++) {
        int result = 0; 
        for(int j = 0; j < nums.size(); j++){
            if(j != i){
                result += nums[j];
            }
        }
        cout << "Result " << result << " " << endl; 
    }
}


int main(){
    vector<int> numbers = {1, 2, 3, 4, 5, 6};

    auto start = std::chrono::steady_clock::now();

    solution_one(numbers);

    auto finish = std::chrono::steady_clock::now();

    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(finish - start);


    cout << "\n\nTotal time to execute: " << elapsed.count() << endl; 



}
