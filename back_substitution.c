#include <stdlib.h>
#include <stdio.h>

void matrix_print(int dim, double *m)
{
  int i;

  for (i = 0; i < dim * dim; i++) {
    printf("|%f|", m[i]);

    if ((i + 1) % 3 == 0) {
      printf("\n");
    }
  }
  printf("\n");
}

void vector_print(int dim, double *v)
{
  int i;

  for (i = 0; i < dim; i++) {
    printf("|%f|\n", v[i]);
  }
  printf("\n");
}

void back_substitute(int dim, double *a, double *b, double *x)
{
  int row, col;
  double curr, prev;

  for (row = dim; row >= 0; row--) {
    prev = 0.0;
    for (col = row; col < dim; col++) {
      prev += x[col] * a[row * dim + col];
    }

    curr = (b[row] - prev) / a[row * dim + row];
    x[row] = curr;
  }

  matrix_print(3, a);
  vector_print(3, b);
  vector_print(3, x);
}

int main(int argc, char *argv[])
{
  double a[9] = {
    3.0, 1.0, 2.0,
    0.0, 3.0, 4.0,
    0.0, 0.0, 5.0,
  };

  double b[3] = {
    6.0, 3.0, 1.0,
  };

  double x[3];

  back_substitute(3, a, b, x);

  return EXIT_SUCCESS;
}
