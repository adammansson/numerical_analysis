#include <math.h>
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

void matrix_addition(int dim, double *a, double *b)
{
  int i, length;

  length = dim * dim;

  for (i = 0; i < length; i++) {
    a[i] += b[i];
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

double matrix_determinant(int dim, double *a)
{
  double *a_copy, *b_unused, det;
  int i;

  a_copy = malloc(sizeof(double) * dim * dim);
  b_unused = malloc(sizeof(double) * dim);

  memcpy(a_copy, a, sizeof(double) * dim * dim);

  gaussian_elimination(dim, a_copy, b_unused);

  det = 1;
  for (i = 0; i < dim; i++) {
    det *= a_copy[i * dim + i];
  }

  free(a_copy);
  free(b_unused);

  return det;
}

void jacobi_solve(int dim, double *a, double *b, double *x, int iterations)
{
  int row, col;
  double *old_x, sum;

  if (matrix_determinant(3, a) == 0.0) {
    printf("Determinant of A is 0, can't solve using Jacobi");
    exit(EXIT_FAILURE);
  }

  old_x = malloc(sizeof(double) * dim * dim);

  for (; iterations >= 0; iterations--) {
    memcpy(old_x, x, sizeof(double) * dim * dim);

    for (row = 0; row < dim; row++) {
      sum = b[row];
      for (col = 0; col < dim; col++) {
        if (col != row) {
          sum -= a[row * dim + col] * old_x[col];
        }
      }

      x[row] = sum / a[row * dim + row];
    }
  }

  free(old_x);
}

void test_jacobi()
{
  double a[9] = {
    10.2, 0, -1.1,
    0.1, 12.0, 0,
    0.1, 0.2, -9.3,
  };

  double b[3] = {
    1, 2, 0,
  };

  double x[3] = {
    0.1, 0.2, 0,
  };

  jacobi_solve(3, a, b, x, 3);

  vector_print(3, x);
}

void gauss_seidel_solve(int dim, double *a, double *b, double *x, int iterations)
{
  int row, col;
  double *old_x, sum;

  if (matrix_determinant(3, a) == 0.0) {
    printf("Determinant of A is 0, can't solve using Jacobi");
    exit(EXIT_FAILURE);
  }

  old_x = malloc(sizeof(double) * dim * dim);

  for (; iterations >= 0; iterations--) {
    memcpy(old_x, x, sizeof(double) * dim * dim);
    for (row = 0; row < dim; row++) {
      sum = b[row];
      for (col = 0; col < dim; col++) {
        if (col > row) {
          sum -= a[row * dim + col] * old_x[col];
        } else if (col < row){
          sum -= a[row * dim + col] * x[col];
        }
      }

      x[row] = sum / a[row * dim + row];
    }
  }

  free(old_x);
}

void test_gauss_seidel()
{
  double a[9] = {
    10, 0, 1,
    6, 12, 0,
    8, 0, 9,
  };

  double b[3] = {
    15, 30, 53,
  };

  double x[3] = {
    0, 1, 3,
  };

  gauss_seidel_solve(3, a, b, x, 6);

  vector_print(3, x);
}

void sor_solve(int dim, double *a, double *b, double *x, double omega, int iterations)
{
  int row, col;
  double *old_x, sum;

  if (matrix_determinant(3, a) == 0.0) {
    printf("Determinant of A is 0, can't solve using Jacobi");
    exit(EXIT_FAILURE);
  }

  old_x = malloc(sizeof(double) * dim * dim);

  for (; iterations >= 0; iterations--) {
    memcpy(old_x, x, sizeof(double) * dim * dim);
    for (row = 0; row < dim; row++) {
      sum = b[row];
      for (col = 0; col < dim; col++) {
        if (col > row) {
          sum -= a[row * dim + col] * old_x[col];
        } else if (col < row){
          sum -= a[row * dim + col] * x[col];
        }
      }

      x[row] = (1 - omega) * old_x[row] + omega * (sum / a[row * dim + row]);
    }
  }

  free(old_x);
}

void test_sor()
{
  double a[9] = {
    10, 0, 1,
    6, 12, 0,
    8, 0, 9,
  };

  double b[3] = {
    15, 30, 53,
  };

  double x[3] = {
    0, 1, 3,
  };

  sor_solve(3, a, b, x, 1.5, 10);

  vector_print(3, x);
}

double vector_infinity_norm(int dim, double *v)
{
  double max;
  max = 0;

  for (dim = dim - 1; dim >= 0; dim--) {
    if (fabs(v[dim]) > max) {
      max = fabs(v[dim]);
    }
  }

  return max;
}

double vector_2_norm(int dim, double *v)
{
  double sum;

  for (dim = dim - 1; dim >= 0; dim--) {
    sum += fabs(v[dim]) * fabs(v[dim]);
  }

  return sqrt(sum);
}

void exercise_3_1()
{
  double a[36] = {
    3, -1, 0, 0, 0, 1.0/2.0,
    -1, 3, -1, 0, 1.0/2.0, 0,
    0, -1, 3, -1, 0, 0,
    0, 0, -1, 3, -1, 0,
    0, 1.0/2.0, 0, -1, 3, -1,
    1.0/2.0, 0, 0, 0, -1, 3,
  };

  double b[6] = {
    5.0/2.0, 3.0/2.0, 1, 1, 3.0/2.0, 5.0/2.0,
  };

  double x[6];

  memset(x, 0, sizeof(double) * 6);
  jacobi_solve(6, a, b, x, 6);
  vector_print(6, x);
  printf("jacobi error = %f\n", fabs(vector_infinity_norm(6, x) - 1));

  memset(x, 0, sizeof(double) * 6);
  gauss_seidel_solve(6, a, b, x, 6);
  vector_print(6, x);
  printf("gauss-seidel error = %f\n", fabs(vector_infinity_norm(6, x) - 1));

  memset(x, 0, sizeof(double) * 6);
  sor_solve(6, a, b, x, 1.2, 6);
  vector_print(6, x);
  printf("sor error = %f\n", fabs(vector_infinity_norm(6, x) - 1));

  /*
   * CORRECT ANSWER:
   * [1, 1, 1, 1, 1, 1]
  */
}

void assignment3_2()
{
  double a[16] = {
    3, 1, 1, 0,
    1, 6, 3, -1,
    6, 0, 9, -2,
    1, 0, -1, -7,
  };

  double b[4] = {
    1, 1, 1, 1,
  };

  double x[4] = {
    0, 1, 1, 0,
  };

  jacobi_solve(4, a, b, x, 25);
  vector_print(4, x);
  printf("2norm = %f\n", vector_2_norm(4, x));
  // CORRECT ANSWER: 0.3858
}

void assignment3_3()
{
  double a[16] = {
    15, -5, 1, 1.1,
    0, 5, 2, -1,
    2, -1, 9, -1,
    1, 1.1, -1, -6,
  };

  double b[4] = {
    1, 1, 1, 1,
  };

  double x[4] = {
    2, 1, 1, 1,
  };

  jacobi_solve(4, a, b, x, 10);
  vector_print(4, x);
  printf("2norm = %f\n", vector_2_norm(4, x));
  // CORRECT ANSWER: 0.2423
}

int main(int argc, char *argv[])
{
  // test_jacobi();
  // test_gauss_seidel();
  // test_sor();
  // exercise_3_1();
  // assignment3_2();
  assignment3_3();

  return EXIT_SUCCESS;
}
