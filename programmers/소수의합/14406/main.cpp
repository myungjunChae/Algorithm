#include <iostream>
#include <vector>
using namespace std;

long long solution(int N) {
	long long answer = 0;
	vector<bool> arr;

	for (int i = 0; i <= N; ++i) {
		arr.push_back(true);
	}
	arr.at(0) = false;
	arr.at(1) = false;

	for (int i = 2; (i*i) <= N; ++i) {
		if (arr.at(i)) {
			for (int j = i + i; j <= N; j += i) {
				arr.at(j) = false;
			}
		}
	}

	for (int i = 2; i <= N; ++i) {
		if (arr[i] == true) {
			cout << i << " ";
			answer += i;
		}
	}

	return answer;
}

int main() {
	int input;
	cin >> input;
	cout << solution(input) << endl;
}
