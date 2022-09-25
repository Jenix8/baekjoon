#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int W, H, X, Y, P;
	cin >> W >> H >> X >> Y >> P;
	int count = 0;
	int x, y;
	for (int i = 0; i < P; i++) {
		cin >> x >> y;
		
		if (x - X >= 0 && x - X <= W) {
			if (y - Y >= 0 && y - Y <= H) {
				count++;
				continue;
			}
		}

		if (pow(x - X, 2) + pow(y - (Y + H / 2), 2) <= 0.25 * H * H) {
			count++;
			continue;
		}

		if (pow(x - (X + W), 2) + pow(y - (Y + H / 2), 2) <= 0.25 * H * H) {
			count++;
			continue;
		}
	}
	cout << count << endl;

	return 0;
}