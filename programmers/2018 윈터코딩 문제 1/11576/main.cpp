#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
	int answer = 0;
	string check = "";

	for (string tree : skill_trees) {
		for (int i = 0; i < tree.size(); ++i)
		{
			if (skill.find(tree.at(i)) != string::npos) {
				check += tree.at(i);
			}
		}

		cout << check << endl;

		if (check.size() == 0)
			answer++;

		if (skill.find(check) != string::npos) {
			if (skill.at(0) == check.at(0)) {
				answer++;
			}
		}

		check = "";
	}

	return answer;
}

int main()
{
	string skill = "CBD";
	vector<string> skill_trees = { "CQWEBD", "BACDE", "CBADF", "AECB", "BDA", "CD"};

	cout << solution(skill, skill_trees);
}