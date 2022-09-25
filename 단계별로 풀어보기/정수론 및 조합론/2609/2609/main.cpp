#include <iostream>
using namespace std;

int gcd(int a, int b) {
	int r;
	while (b != 0) {
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int main() {
	int a, b;
	cin >> a >> b;
	cout << gcd(a, b) << endl;
	cout << a * b / gcd(a, b) << endl;
	return 0;
}