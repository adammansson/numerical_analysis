#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void matrix_print(int dim, double *m)
{
  int i;

  printf("\n");
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

  printf("\n");
  for (i = 0; i < dim; i++) {
    printf("|%f|\n", v[i]);
  }
  printf("\n");
}

void back_substitution(int dim, double *a, double *b, double *x)
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
}

void forward_substitution(int dim, double *a, double *b, double *x)
{
  int row, col;
  double curr, prev;

  for (row = 0; row < dim; row++) {
    prev = 0.0;
    for (col = row; col >= 0; col--) {
      prev += x[col] * a[row * dim + col];
    }

    curr = (b[row] - prev) / a[row * dim + row];
    x[row] = curr;
  }
}

void gaussian_elimination(int dim, double *a, double *b)
{
  int row, other_row, col;
  double mult;

  for (row = 0; row < dim - 1; row++) {
    for (other_row = row + 1; other_row < dim; other_row++) {
      mult = a[other_row * dim + row] / a[row * dim + row];

      for (col = row; col < dim; col++) {
        a[other_row * dim + col] = a[other_row * dim + col] - mult * a[row * dim + col];
      }

      b[other_row] = b[other_row] - mult * b[row];
    }
  }
}

void gaussian_solve(int dim, double *a, double *b, double *x)
{
  gaussian_elimination(dim, a, b);
  back_substitution(3, a, b, x);
}

void lu_decomposition(int dim, double *a, double *l, double *u)
{
  int row, other_row, col;
  double mult;

  memset(l, 0, 9 * sizeof(double));
  for (row = 0; row < dim; row++) {
    l[row * dim + row] = 1;
  }

  memcpy(u, a, 9 * sizeof(double));

  for (row = 0; row < dim - 1; row++) {
    for (other_row = row + 1; other_row < dim; other_row++) {
      mult = u[other_row * dim + row] / u[row * dim + row];
      l[other_row * dim + row] = mult;

      for (col = row; col < dim; col++) {
        u[other_row * dim + col] = u[other_row * dim + col] - mult * u[row * dim + col];
      }
    }
  }
}

void matrix_multiplication(int dim, double *a, double *b, double *c)
{
  int row, col, i;
  double sum;

  for (row = 0; row < dim; row++) {
    for (col = 0; col < dim; col++) {
      sum = 0.0;
      for (i = 0; i < dim; i++) {
        sum += a[row * dim + i] * b[i * dim + col];
      }
      c[row * dim + col] = sum;
    }
  }
}

void lu_solve(int dim, double *a, double *b, double *x)
{
  double l[9];
  double u[9];
  double c[3];

  lu_decomposition(3, a, l, u);
  forward_substitution(3, l, b, c);
  back_substitution(3, u, c, x);
}

int main(int argc, char *argv[])
{
  /*
  double a[9] = {
    3.0, 1.0, 2.0,
    0.0, 3.0, 4.0,
    0.0, 0.0, 5.0,
  };

  double a[9] = {
    5.0, 0.0, 0.0,
    4.0, 3.0, 0.0,
    2.0, 1.0, 3.0,
  };

  double b[3] = {
    6.0, 3.0, 1.0,
  };

  double a1[9] = {
    3, -0.5, 0.6,
    4.7, 2, 2.3,
    0.1, -5, 9.1,
  };

  double b1[3] = {
    4.57, 8.14, 46.76,
  };

  double x1[3];

  gaussian_solve(3, a1, b1, x1);
  vector_print(3, x1);

  double a2[9] = {
    1, 1, 1,
    1, -1, 2,
    3, 1, 4,
  };

  double b2[3] = {
    1, 1, 1,
  };

  double x2[3];

  gaussian_solve(3, a2, b2, x2);
  vector_print(3, x2);
  */

  double a3[9] = {
    4, 2, 0,
    4, 4, 2,
    2, 2, 3,
  };

  double b3[3] = {
    1, 2, 3,
  };

  double x[3];

  double l3[9];
  double u3[9];
  double r3[9];

  lu_decomposition(3, a3, l3, u3);
  matrix_print(3, l3);
  matrix_print(3, u3);

  matrix_multiplication(3, l3, u3, r3);
  matrix_print(3, r3);

  lu_solve(3, a3, b3, x);
  vector_print(3, x);

  return EXIT_SUCCESS;
}
