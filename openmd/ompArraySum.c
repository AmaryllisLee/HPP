/* arraySum.c uses an array to sum the values in an input file,
 *  whose name is specified on the command-line.
 * Huib Aldewereld, HU, HPP, 2020
 */

#include <stdio.h>      /* I/O stuff */
#include <stdlib.h>     /* calloc, etc. */
#include <omp.h>

void readArray(char * fileName, double ** a, int * n);
double sumArray(double * a, int numValues) ;

int main(int argc, char * argv[])
{
  int  howMany;
  double sum;
  double * a;
  int id;
  double start;
  double  end;

  if (argc != 2) {
    fprintf(stderr, "\n*** Usage: arraySum <inputFile>\n\n");
    exit(1);
  }

  // int n_threads[4] = {1, 2, 4, 8};

  #pragma omp parallel private(id)
  {
    id = omp_get_thread_num();

    if ( id == 0 ) {  // thread with ID 0 is master
        readArray(argv[1], &a, &howMany);
    }  
            // threads with IDs > 0 are workers 
    #pragma omp barrier

    int numThreads = omp_get_num_threads();
    int size =(int) howMany/  numThreads ;
    
    start = omp_get_wtime();
    sum  +=  sumArray(a, size);
    end = omp_get_wtime();
    printf("Elasped time = %f sec\n", end - start);
    printf("The sum of the values in the input file is %g\n",sum);
  }


    free(a);

    return 0;
}

  


/* readArray fills an array with values from a file.
 * Receive: fileName, a char*,
 *          a, the address of a pointer to an array,
 *          n, the address of an int.
 * PRE: fileName contains N, followed by N double values.
 * POST: a points to a dynamically allocated array
 *        containing the N values from fileName
 *        and n == N.
 */

void readArray(char * fileName, double ** a, int * n) {
  int count, howMany;
  double * tempA;
  FILE * fin;

  fin = fopen(fileName, "r");
  if (fin == NULL) {
    fprintf(stderr, "\n*** Unable to open input file '%s'\n\n",
                     fileName);
    exit(1);
  }

  fscanf(fin, "%d", &howMany);
  tempA = calloc(howMany, sizeof(double));
  if (tempA == NULL) {
    fprintf(stderr, "\n*** Unable to allocate %d-length array",
                     howMany);
    exit(1);
  }

  for (count = 0; count < howMany; count++)
   fscanf(fin, "%lf", &tempA[count]);

  fclose(fin);

  *n = howMany;
  *a = tempA;
}

/* sumArray sums the values in an array of doubles.
 * Receive: a, a pointer to the head of an array;
 *          numValues, the number of values in the array.
 * Return: the sum of the values in the array.
 */

double sumArray(double * a, int numValues) {
  int i;
  double result = 0.0;
  #pragma omp parallel for reduction(+:result) 
   for (i = 0; i < numValues; i++) {
     result += a[i];
  }

  return result;
}

