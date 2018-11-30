/* Copyright (c) Michael Holmblad
   The code in this file was created by Michael Holmblad.
   If you use this code
 */


#include <stdio.h>
#include <gsl/gsl_rng.h>
#include <limits.h>

int
main (void)
{
  FILE *f = fopen("number.txt", "w+");
  if (f == NULL)
  {
    printf("Could not open file ");
    exit(1);
  }
  
  const gsl_rng_type * T;
  gsl_rng * r;

  int i, n = 300000000;
  double nextx;

  gsl_rng_env_setup();

  T = gsl_rng_default;
  r = gsl_rng_alloc (T);
  
  fprintf(f,"#================================================================\n");
  fprintf(f,"# Generator Tent First Try seed = %lu\n");
  fprintf(f,"#================================================================\n");
  fprintf(f,"type: d\n");
  fprintf(f,"count: %d\n", n);
  fprintf(f,"numbit: 32\n");

  for (i = 0; i < n; i++)
    {
      double u = gsl_rng_uniform (r);
      double current = u;
      if(current <= 1.0/3.0){
        nextx = 3.0 * current;
      }else if(current <= 2.0/3.0){
        nextx = 2.0 - 3.0 * current;
      }else if(current <= 1.0){
        nextx = 3.0 * current - 2.0;
      }
      
      long int final = nextx * UINT_MAX;
      fprintf (f,"%ld\n", final);
    }

  gsl_rng_free (r);

  return 0;
}
