#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int m, M;
	
	int k;
	cin >> k;

	if (N == 1) {
		cout << k * k << endl;
		return 0;
	}

	m = M = k;

	for (int i = 1; i < N; i++) {
		int k;
		cin >> k;
		
		if (k < m) m = k;
		if (k > M) M = k;
	}

	cout << m * M << endl;

	return 0;
}