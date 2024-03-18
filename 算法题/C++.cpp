#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

int main() {
    vector<int> nums;
    string input;
    int num;

    cout << "请输入整数数组元素（用空格分隔，输入回车表示输入完成）：" << endl;
    getline(cin, input); // 读取一行输入

    istringstream iss(input);
    while (iss >> num) {
        nums.push_back(num);
    }

    int result = singleNumber(nums);
    cout << "只出现一次的元素是：" << result << endl;

    return 0;
}
