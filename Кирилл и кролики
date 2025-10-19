#include <iostream>
 
using namespace std;
 
int main()
{
    long long n, a, b;
    cin >> n >> a >> b;
    if (n % 2 != 0)
    {
        cout << -1;
    }
    else
    {
        n /= 2;
        long long max_r = n / a;
        if (max_r <= 0)
        {
            cout << -1;
        }
        else if ((n % a) / max_r <= b - a) 
        {
            cout << max_r;
        }
        else
        {
            cout << -1;
        }
    }
    return 0;
}
