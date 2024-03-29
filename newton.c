#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double approximate_derivative(double (*fn)(double), double x)
{
  double h;

  h = 1.0e-6;

  return (fn(x + h) - fn(x - h)) / (2 * h);
}

double function_3a(double x)
{
  return x*x*x -6.0*x*x + 4.0*x + 12.0;
}

double function_3b(double x)
{
  return exp(sin(x)*sin(x)*sin(x)) + x*x*x*x*x*x - 2.0*x*x*x*x - x*x*x - 1.0;
}

double function_3e(double x)
{
  return x / (sqrt(x*x + 1));
}

double function_3d(double x)
{
  return x*x*x - x;
}

double function_exercise3(double x)
{
  return x / sqrt(x*x + 1);
}

double function_exercise3_prime(double x)
{
  return 1 / ((x*x + 1) * sqrt(x*x + 1));
}

void solve_numerically_with_approximation(
  double (*fn)(double),
  double x,
  int iterations
)
{
  for (; iterations >= 0; iterations--)
  {
    x = x - fn(x) / approximate_derivative(fn, x);

    printf("x = %.16f\n", x);
  }
}

void solve_numerically(
  double (*fn)(double),
  double (*fn_prime)(double),
  double x,
  int iterations
)
{
  for (; iterations >= 0; iterations--)
  {
    x = x - fn(x) / fn_prime(x);

    printf("x = %e\n", x);
  }
}

int main(int argc, char *argv[])
{
  int iterations;

  if (argc != 2) {
    return EXIT_FAILURE;
  }

  iterations = atoi(argv[1]);

  solve_numerically(function_exercise3, function_exercise3_prime, 0.9, 10);

  return EXIT_SUCCESS;
}
