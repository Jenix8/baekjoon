#include <iostream>
using namespace std;

int N, M;
int v[8] = { 0, };

void pr(int depth) {
	if (depth == M) {
		for (int i = 0; i < M; i++)
			cout << v[i] << " ";
		cout << "\n";
		return;
	}

	for (int i = 1; i <= N; i++) {
		v[depth] = i;
		pr(depth + 1);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;
	pr(0);
	return 0;
}