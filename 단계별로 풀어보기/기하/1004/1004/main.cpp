#include <iostream>
#include <cmath>
using namespace std;

bool inside(int x, int y, int cx, int cy, int r) {
	if (pow(x - cx, 2) + pow(y - cy, 2) < pow(r, 2))
		return true;
	return false;
}

int main() {
	int T;
	cin >> T;
	int saved[1000];

	for (int i = 0; i < T; i++) {
		
		int x1, y1, x2, y2, N;
		int count = 0;
		cin >> x1 >> y1 >> x2 >> y2;
		cin >> N;
		
		for (int j = 0; j < N; j++) {
			int cx, cy, r;
			cin >> cx >> cy >> r;
			
			if (inside(x1, y1, cx, cy, r) && !inside(x2, y2, cx, cy, r))
				count++;
			if (!inside(x1, y1, cx, cy, r) && inside(x2, y2, cx, cy, r))
				count++;
		}
		saved[i] = count;
	}

	for (int i = 0; i < T; i++)
		cout << saved[i] << endl;

	return 0;
}

