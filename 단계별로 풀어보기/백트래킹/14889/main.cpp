#include <iostream>
#include <vector>
#include <cstdlib>
#include <limits.h>
using namespace std;

int N, m = INT_MAX;
int v[10] = { 0, };
int S[20][20];
vector<int> score;

void calcScore() {
    int s = 0;
    for (int i = 0; i < N / 2; i++) {
        for (int j = i + 1; j < N / 2; j++)
            s += S[v[i]][v[j]] + S[v[j]][v[i]];
    }

    score.push_back(s);
}

void func(int depth, int last) {
    if (depth == N / 2) {
        calcScore();
        return;
    }

    for (int i = 0; i < N; i++) {
        if (i > last) {
            v[depth] = i;
            func(depth + 1, i);
            v[depth] = 0;
        }
    }
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> S[i][j];

    func(0, -1);

    int diff = 0, count = score.size();
    for (int i = 0; i < count / 2; i++) {
        diff = abs(score[i] - score[count - i - 1]);
        if (diff < m) m = diff;

        if (m == 0) break;
    }

    cout << m;

    return 0;
}