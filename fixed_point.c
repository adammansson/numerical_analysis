#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double approximate_derivative(double (*fn)(double), double x)
{
  double h;

  h = 0.000000001;

  return (fn(x + h) - fn(x)) / h;
}

double function_7a1(double x)
{
  return (x*x*x - 2) / 2;
}

double function_7a2(double x)
{
  return pow(2*x + 2.0, 1.0 / 3.0);
}

double function_7b1(double x)
{
  return 7 - exp(x);
}

double function_7b2(double x)
{
  return log(7 - x);
}

double function_7c(double x)
{
  return log(4 - sin(x));
}

double function_4(double x)
{
  return cos(x) * cos(x);
}

double assignment3_3(double x)
{
  return (x + 2 / x) / 2;
}

void solve_numerically(
  double (*fn)(double),
  double x,
  int iterations
)
{
  if (fabs(approximate_derivative(fn, x)) >= 1) {
    printf("won't work\n");
    return;
  }

  for (; iterations >= 0; iterations--)
  {
    x = fn(x);

    printf("x = %.16f\n", x);
  }
}

int main(int argc, char *argv[])
{
  int iterations;

  if (argc != 2) {
    return EXIT_FAILURE;
  }

  iterations = atoi(argv[1]);

  // solve_numerically(function_4, 0.5, 200);
  solve_numerically(assignment3_3, 1.4, 200);
  printf("sqrt(2) = %.16f\n", sqrt(2.0));

  return EXIT_SUCCESS;
}
