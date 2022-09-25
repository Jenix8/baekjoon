#include <iostream>
using namespace std;

long long fact_fivenumber(long long N) {
	long long count = 0;
	for (long long i = 5; i <= N; i *= 5) {
		count += N / i;
	}
	return count;
}

long long fact_twonumber(long long N) {
	long long count = 0;
	for (long long i = 2; i <= N; i *= 2) {
		count += N / i;
	}
	return count;
}

int main() {
	int n, m;
	cin >> n >> m;
	long long a = fact_fivenumber(n) - fact_fivenumber(m) - fact_fivenumber(n - m);
	long long b = fact_twonumber(n) - fact_twonumber(m) - fact_twonumber(n - m);

	cout << min(a, b) << endl;

	return 0;
}