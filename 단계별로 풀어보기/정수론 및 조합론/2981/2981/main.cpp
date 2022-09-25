#include <iostream>
using namespace std;

int gcd(int a, int b) {
	if (a % b == 0) return b;
	if (b % a == 0) return a;
	
	int r;
	while (b != 0) {
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}

void print_divisors(int n) {
	for (int i = 2; i < (n / 2) + 1; i++)
		if (n % i == 0)
			cout << i << " ";
	cout << n << endl;
}

int main() {
	int N, temp, numbers[100], differ[99];
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> numbers[i];
		if (i != 0) differ[i - 1] = abs(numbers[i] - numbers[i - 1]);
	}

	for (int j = 0; j < N - 1; j++) {
		if (j == 0) temp = differ[j];
		else temp = gcd(differ[j], temp);
	}

	print_divisors(temp);

	return 0;
}