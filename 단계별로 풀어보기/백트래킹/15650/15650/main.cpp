#include <iostream>
using namespace std;

int N, M;
int v[9];

void print(int depth, int last) {
	if (depth == M) {
		for (int i = 0; i < M; i++)
			cout << v[i] << ' ';
		cout << endl;
	}

	for (int i = 1; i <= N; i++) {
		if (i > last) {
			v[depth] = i;
			print(depth + 1, i);
			v[depth] = 0;
		}
	}
}

int main() {
	cin >> N >> M;
	print(0, 0);
}