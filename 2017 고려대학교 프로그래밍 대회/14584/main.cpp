#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string.h>
using namespace std;

string caesar(string plane, int n) {
	char cypchar[100];
	strcpy(cypchar, plane.c_str());

	for (int i = 0; cypchar[i] != '\0'; i++) {
		if (int(cypchar[i]) + n > 122) cypchar[i] -= 26;
		cypchar[i] += n;
	}

	string cyp(cypchar);
	return cyp;
}

int main() {
	string cypher, key[20], decode;
	char tmp[100];
	int N;

	cin >> cypher;
	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> key[i];

	for (int i = 0; i < 26; i++) {
		decode = caesar(cypher, i);

		for (int j = 0; j < N; j++) {
			if (decode.find(key[j]) != string::npos) {
				cout << decode;
				break;
			}
		}
	}
	

	return 0;
}