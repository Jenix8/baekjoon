#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	//int comb[101][101];
	vector<vector<int>> comb;

	for (int i = 0; i <= N; i++) {
		vector<int> col;
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i)
				col.push_back(1);
			else
				col.push_back((comb[i - 1][j - 1] + comb[i - 1][j]) % 10007);
		}
		comb.push_back(col);
	}

	cout << comb[N][K] << endl;
	return 0;
}