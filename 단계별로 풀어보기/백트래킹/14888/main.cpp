#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int calc(int a, int b, int oper) {
	if (oper == 0) return a + b;
	if (oper == 1) return a - b;
	if (oper == 2) return a * b;
	if (oper == 3) return (int)(a / b);
}

int main() {
	int N, tmpi;
	vector<int> nums;
	vector<int> order;
	int opers[4] = { 0, 1, 2, 3 }; // respectively, + - * /

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> tmpi;
		nums.push_back(tmpi);
	}
	for (int i = 0; i < 4; i++) {
		cin >> tmpi;
		for (int j = 0; j < tmpi; j++) order.push_back(i);
	}

	int res, M = -1e9, m = 1e9;

	do {
		res = nums[0];
		for (int i = 1; i < N; i++) 
			res = calc(res, nums[i], order[i - 1]);

		if (M < res) M = res;
		if (m > res) m = res;

	} while (next_permutation(order.begin(), order.end()));

	printf("%d\n%d\n", M, m);

	return 0;
}