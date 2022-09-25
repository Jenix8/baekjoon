#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int main() {
	int N, M, tx, ty;
	cin >> N >> M;
	long NoC[301][301];
	memset(NoC, 0, sizeof(NoC));
	for (int i = 0; i < N; i++) {
		cin >> tx >> ty;
		NoC[tx][ty] = max(M - tx - ty, 0);
	}

	for (int i = 0; i <= 300; i++) {
		for (int j = 0; j <= 300; j++) {
			NoC[i][j] += max((i > 0) ? NoC[i - 1][j] : 0, (j > 0) ? NoC[i][j - 1] : 0);
		}
	}

	cout << NoC[300][300] << '\n';

	return 0;
}
