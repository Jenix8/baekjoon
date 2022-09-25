#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class team {
public:
	team() {}
	~team() {}
	void printTeam() {
		cout << teamNum << " " << ansNum << " " << total << '\n';
	}
	bool operator>(const team& other) const {
		if (this->ansNum > other.ansNum)
			return true;
		else if (this->ansNum < other.ansNum)
			return false;

		if (this->total < other.total)
			return true;
		else if (this->total > other.total)
			return false;

		return this->teamNum < other.teamNum;
	}

	int teamNum = 0;
	bool correct[15] = { 0, };
	int time[15] = { 0, };
	int total = 0, ansNum = 0;
};

int main() {
	int n, m, q;
	cin >> n >> m >> q;
	int ti, te, pr;
	string stat;
	
	vector<team> v(n);

	for (int i = 0; i < n; i++)
		v[i].teamNum = i + 1;

	for (int i = 0; i < q; i++) {
		cin >> ti >> te >> pr >> stat;

		if (v[te - 1].correct[pr - 1] == 0) {
			if (stat == "AC") {
				v[te - 1].correct[pr - 1] = 1;
				v[te - 1].ansNum++;
				v[te - 1].time[pr - 1] += ti;
			}
			else if (stat == "WA" || stat == "TLE" || stat == "RE") {
				v[te - 1].time[pr - 1] += 20;
			}
		}
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			v[i].total += v[i].correct[j] * v[i].time[j];

	sort(v.begin(), v.end(), greater<team>());

	for (int i = 0; i < n; i++)
		v[i].printTeam();

	return 0;
}