#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int F(int n) {
	int digitN = floor(log10(n) + 1);
	int M = 0, k = 1;
	for (int i = 0; i < digitN; i++) {
		M += 9 * k;
		k *= 10;
	}
	return M - n;
}

int main() {
	int T, N;
	cin >> T;
	vector<long long> ans;

	for (int i = 0; i < T; i++) {
		int maxi = 0;
		cin >> N;

		for (int j = 1; j <= N; j++)
			maxi = max(maxi, j * F(j));

		ans.push_back(maxi);
	}

	for (auto it = ans.begin(); it != ans.end(); it++)
		cout << *it << '\n';
}