#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double calculate_middle(double lower, double upper)
{
  return (lower + upper) / 2;
}

double my_function(double x)
{
  return cos(x) - sin(x);
}

void solve_numerically(
  double (*fn)(double),
  double lower,
  double upper,
  int iterations
)
{
  double middle;

  for (; iterations >= 0; iterations--)
  {
    middle = calculate_middle(lower, upper);
    printf("middle = %f\n", middle);

    if (fn(lower) * fn(middle) < 0) {
      upper = middle;
    } else {
      lower = middle;
    }
  }
}

int main(int argc, char *argv[])
{
  int iterations;

  if (argc != 2) {
    return EXIT_FAILURE;
  }

  iterations = atoi(argv[1]);
  solve_numerically(my_function, 0.0, 1.0, iterations);

  return EXIT_SUCCESS;
}
