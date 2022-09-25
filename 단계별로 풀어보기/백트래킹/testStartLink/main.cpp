#include <iostream>
using namespace std;

int N, M;
int saved[200000][20];
int v[20];
int c = 0;

void print(int depth, int last) {
	if (depth == M) {
		for (int i = 0; i < M; i++)
			saved[c][i] = v[i];
		c++;
	}

	for (int i = 1; i <= N; i++) {
		if (i > last) {
			v[depth] = i;
			print(depth + 1, i);
			v[depth] = 0;
		}
	}
}

bool comp(int t[20], int c[20], int n) {
	for (int i = 0; i < n; i++) {
		if (t[i] != c[i])
			return false;
	}
	return true;
}

int main() {
	cin >> N >> M;
	print(0, 0);

	//for (int i = 0; i < c; i++) {
	//	for (int j = 0; j < M; j++)
	//		cout << saved[i][j] << ' ';
	//	cout << '\n';
	//}

	int test[20], given[20];
	for (int i = 0; i < N; i++)
		test[i] = i + 1;

	for (int i = 0; i < c / 2; i++) {
		int a = 0, b = 0, idx = 0;

		for (int k = 1; k <= N; k++) {
			if (saved[i][a] == k) {
				given[idx++] = k;
				a++;
			}
			else if (saved[c - i - 1][b] == k) {
				given[idx++] = k;
				b++;
			}
		}

		if (!comp(test, given, N)) {
			cout << i << "th break\n";

			for (int j = 0; j < N; j++)
				cout << given[j] << ' ';
			cout << '\n';

			break;
		}
	}
}