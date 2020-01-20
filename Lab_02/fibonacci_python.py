def fib_series(series_length):
    if series_length <= 1:
        return series_length

    fib = 1
    fib_prev = 1
    for i in range(series_length - 2):
        i += 2
        temp = fib
        fib += fib_prev
        fib_prev = temp
    return fib

print(fib_series(10))

# int fibo(int n){
#  if(n <= 1){
#   return n;
#  }
#  int fibo = 1;
#  int fiboPrev = 1;
#  for(int i = 2; i < n; ++i){
#   int temp = fibo;
#   fibo += fiboPrev;
#   fiboPrev = temp;
#  }
#  return fibo;
# }