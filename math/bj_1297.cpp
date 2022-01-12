#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int d, h, w;
    cin >> d >> h >> w;
    double k;
    k = sqrt(double(d * d) / double((h * h + w * w)));
    int height = h * k;
    int width = w * k;
    cout << height << ' ' << width << endl;
}