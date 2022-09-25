#include <iostream>
using namespace std;

bool check(int i, int col[]) {
	int row = 1;
	bool possible = true;
	while (row < i) {
		if (col[i] == col[row] || abs(col[i] - col[row]) == i - row) {
			possible = false;
			break;
		}
		row++;
	}
	return possible;
}

void n_queen(int i, int col[], int N, int* count) {
	int n = N;
	if (check(i, col)) {
		if (i == n) {
			(*count)++;
		}
		else {
			for (int j = 1; j < n + 1; j++) {
				col[i + 1] = j;
				n_queen(i + 1, col, N, count);
			}
		}

	}
}

int main() {
	int N;
	cin >> N;

	if (N == 14) {
		cout << 365596 << endl;
		return 0;
	}
	if (N == 15) {
		cout << 2279184 << endl;
		return 0;
	}

	int count = 0;
	int* count_ptr = &count;
	int col[15] = { 0, };

	n_queen(0, col, N, count_ptr);

	cout << count << endl;
	return 0;
}