#include <string>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";

	map<string, int> count;
	for (int i = 0; i < participant.size(); ++i) {
		count.insert(pair<string, int>(participant[i], 0));
	}

	participant.insert(participant.end(), completion.begin(), completion.end());
	map<string, int>::iterator it;
	for (int i = 0; i < participant.size(); ++i) {
		it = count.find(participant[i]);
		if (it != count.end()) {
			it->second += 1;
		}
	}

	for (it = count.begin(); it != count.end(); ++it) {
		if (it->second % 2 != 0) {
			answer = it->first;
		}
	}

	return answer;
}

int main() {
	vector<string> input1, input2;
	input1.push_back("leo");
	input1.push_back("kiki");
	input1.push_back("eden");

	input2.push_back("kiki");
	input2.push_back("eden");

	cout << solution(input1, input2) << endl;
}

/* 참고할 만한 코드
string solution(vector<string> participant, vector<string> completion) {
	string answer = "";
	sort(participant.begin(), participant.end());
	sort(completion.begin(), completion.end());
	for(int i=0;i<completion.size();i++)
	{
		if(participant[i] != completion[i])
			return participant[i];
	}
	return participant[participant.size() - 1];
}
*/