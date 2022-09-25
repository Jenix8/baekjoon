#include <iostream>
using namespace std;

bool complete = false;

bool check(int s[9][9], int r, int c, int n) {
	// row
	for (int i = 0; i < 9; i++) {
		if (s[r][i] == n)
			return false;
	}

	// column
	for (int i = 0; i < 9; i++) {
		if (s[i][c] == n)
			return false;
	}

	// square
	int squareRow = r / 3;
	int squareCol = c / 3;
	for (int i = squareRow * 3; i < squareRow * 3 + 3; i++) {
		for (int j = squareCol * 3; j < squareCol * 3 + 3; j++) {
			if (s[i][j] == n)
				return false;
		}
	}

	return true;
}

void fill_sudoku(int depth, int count, int s[9][9], int row[81], int col[81]) {
	if (depth == count) {
		complete = true;
		return;
	}

	for (int n = 1; n <= 9; n++) {
		if (check(s, row[depth], col[depth], n)) {
			s[row[depth]][col[depth]] = n;
			fill_sudoku(depth + 1, count, s, row, col);

			if (complete) return;

			s[row[depth + 1]][col[depth + 1]] = 0;
		}
	}
}

int main() {
	int sudoku[9][9];
	int count = 0;
	int row[81], col[81];


	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> sudoku[i][j];
			if (sudoku[i][j] == 0) {
				row[count] = i;
				col[count++] = j;
			}
		}
	}

	fill_sudoku(0, count, sudoku, row, col);

	cout << '\n';

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << sudoku[i][j] << ' ';
		}
		cout << '\n';
	}
}