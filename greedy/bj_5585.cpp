#include <iostream>
using namespace std;

int main() {
	int price;
	cin >> price;
	int sum = 1000 - price;
	int total = 0;
	int token[6] = { 500,100,50,10,5,1 };
	for (int i = 0; i < 6; i++) {
		while (sum >= token[i]) {
			sum -= token[i];
			total++;
		}
	}
	cout << total;
}