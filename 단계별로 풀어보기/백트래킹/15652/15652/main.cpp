#include <iostream>
using namespace std;

int N, M;
int v[9];

void print(int depth, int last) {
	if (depth == M) {
		for (int i = 0; i < M; i++)
			cout << v[i] << ' ';
		cout << "\n";
		return;
	}

	for (int i = 1; i <= N; i++) {
		if (i >= last) {
			v[depth] = i;
			print(depth + 1, i);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;
	print(0, 1);

	return 0;
}