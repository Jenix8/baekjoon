#include <iostream>

using namespace std;

const int SN = 6;

int main() {
	int k, area;
	int direction[SN];
	int length[SN];

	cin >> k;
	for (int i = 0; i < SN; i++) 
		cin >> direction[i] >> length[i];

	for (int i = 0; i < SN; i++) {
		if (direction[i] == direction[(i + 2) % SN]) {
			if (direction[(i + 1) % SN] == direction[(i + 3) % SN]) {
				area = length[(i + 4) % SN] * length[(i + 5) % SN]
					- length[(i + 1) % SN] * length[(i + 2) % SN];
			}
		}
	}

	cout << k * area << endl;
	return 0;
}