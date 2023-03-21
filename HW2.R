# HW2
# sapply, lapply elapsed time comparison

# data
data <- rnorm(1000000, 0, 1)

# Using sapply
t <- Sys.time()
data_sapply <- sapply(list(data), function(x){round(x,2)})
t_sapply <- Sys.time()

print(t_sapply - t)

# Time difference of 0.04321408 secs

# Using for loop
func <- function(x){round(x,2) ; invisible(x)} # make result invisible
t <- Sys.time()
for (x in data) {
  func(x)
}
t_for <- Sys.time()

print(t_for - t) 

# Time difference of 0.422363 secs