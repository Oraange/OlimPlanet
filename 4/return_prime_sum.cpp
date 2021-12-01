#include <vector>
#include <iostream>
#include <thread>
#include <cmath>

using namespace std;

vector<bool> isPrime = {true,};

void CheckPrime(unsigned int N) {
    for (int i=2;i*i<=N;i++) {
        if (isPrime[i]) {
            for (int j=i*i; j<=N; j+=i) {
                isPrime[j] = false;
            }
        }
    }
    return;
}

unsigned int SumOfAllPrimeNumbersLessThan() {
    unsigned int primeSum = 0;

    for (int i=2; i<isPrime.size(); i++) {
        if (isPrime[i]) primeSum += i;
    }

    return primeSum;
}

int main() {
    unsigned int N;
    cin >> N;
    if (N<=1) return 0;

    isPrime.resize(N, true);

    int thr_num = int(sqrt(N));
    thread *thr = new thread[thr_num];
    for (int i=0; i<thr_num; i++) thr[i] = thread(CheckPrime, N);
    for (int i=0; i<thr_num; i++) thr[i].join();

    return SumOfAllPrimeNumbersLessThan();
}
