#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void calculate()
{
  double N;
  double area;

  cin>>N; 

  area = pow(N, 2.0);

  cout<<area<<endl;
 }
 
int main()
{
  calculate(); 
  return 0;
}