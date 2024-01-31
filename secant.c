#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void solve_numerically(
  double (*fn)(double),
  double x0,
  double x1,
  int iterations
)
{
  double temp;

  for (; iterations >= 0; iterations--)
  {
    temp = x1;
    x1 = x1 - (fn(x1) * (x1 - x0)) / (fn(x1) - fn(x0));
    x0 = temp;

    printf("xi = %.16f\n", x1);
  }
}

double function_3a(double x)
{
  return x*x*x -6.0*x*x + 4.0*x + 12.0;
}

double function_3b(double x)
{
  return exp(sin(x)*sin(x)*sin(x)) + x*x*x*x*x*x - 2.0*x*x*x*x - x*x*x - 1.0;
}

double function_4a(double x)
{
  return exp(x) + sin(x) - 4.0;
}

int main(int argc, char *argv[])
{
  int iterations;

  if (argc != 2) {
    return EXIT_FAILURE;
  }

  iterations = atoi(argv[1]);

  solve_numerically(function_3a, 3.9, 5.5, 10);

  return EXIT_SUCCESS;
}
