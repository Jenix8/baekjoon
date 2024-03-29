#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#define int long long
#define double long double
using namespace std;

void p20149()
{
	double x, y, t1, t2;
	int x1, y1, x2, y2, x3, y3, x4, y4;
	scanf("%lld %lld %lld %lld", &x1, &y1, &x2, &y2);
	scanf("%lld %lld %lld %lld", &x3, &y3, &x4, &y4);

	int A = y2 - y1;
	int B = x1 - x2;
	int E = x2 * y1 - x1 * y2;
	int C = y4 - y3;
	int D = x3 - x4;
	int F = x4 * y3 - x3 * y4;
	int deno = A * D - B * C;

	if (abs(x1 - x2) + abs(y1 - y2) == 0 || abs(x3 - x4) + abs(y3 - y4) == 0) printf("0\n");
	else if (deno != 0)
	{
		x = (B * F - E * D) / (double)deno;
		y = (E * C - A * F) / (double)deno;

		t1 = (x1 != x2) ? (x - x1) / (x2 - x1) : (y - y1) / (y2 - y1);
		t2 = (x3 != x4) ? (x - x3) / (x4 - x3) : (y - y3) / (y4 - y3);

		if (t1 >= 0 && t1 <= 1 && t2 >= 0 && t2 <= 1)
		{
			if (x - (int)x == 0 && y - (int)y == 0) printf("1\n%lld %lld\n", (int)x, (int)y);
			else if (x - (int)x == 0 && y - (int)y != 0) printf("1\n%lld %.16Lf\n", (int)x, y);
			else if (x - (int)x != 0 && y - (int)y == 0) printf("1\n%.16Lf %lld\n", x, (int)y);
			else if (x - (int)x != 0 && y - (int)y != 0) printf("1\n%.16Lf %.16Lf\n", x, y);
		}
		else printf("0\n");
	}
	else
	{
		if (A * x3 + B * y3 + E == 0)
		{
			int d = max(x1, max(x2, max(x3, x4))) - min(x1, min(x2, min(x3, x4)));
			int l1 = max(x1, x2) - min(x1, x2);
			int l2 = max(x3, x4) - min(x3, x4);

			if (d == 0 || l1 == 0 || l2 == 0)
			{
				d = max(y1, max(y2, max(y3, y4))) - min(y1, min(y2, min(y3, y4)));
				l1 = max(y1, y2) - min(y1, y2);
				l2 = max(y3, y4) - min(y3, y4);
			}

			if (d < l1 + l2) printf("1\n");
			else if (d > l1 + l2) printf("0\n");
			else
			{
				if (x1 == x3 && y1 == y3) printf("1\n%lld %lld\n", x1, y1);
				else if (x1 == x4 && y1 == y4) printf("1\n%lld %lld\n", x1, y1);
				else if (x2 == x3 && y2 == y3) printf("1\n%lld %lld\n", x2, y2);
				else if (x2 == x4 && y2 == y4) printf("1\n%lld %lld\n", x2, y2);
			}
		}
		else printf("0\n");
	}
}