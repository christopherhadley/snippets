Canned code for R

loop for reading in lots of CSVs at once:

# Ex - read in multiple CSVs with same headers: 
# 1.csv: 
# a,b,c
# 1,2,3

#getwd()
files <- dir("data/", pattern = "\\.csv$", full.names = TRUE)
df <- vector("list", length(files))
for (i in seq_along(files)) {
  df[[i]] <- read_csv(file = files[[i]])
}
df <- bind_rows(df)
df


# Save multiple plots: 
library(ggplot2)
plots <- mtcars %>%
  split(.$cyl) %>%
  map(~ggplot(., aes(mpg, wt)) + geom_point())
paths <- stringr::str_c(names(plots), ".pdf")
pwalk(list(paths, plots), ggsave, path = tempdir())

#  Number of unique values per column: 
transaction_uniques <- vector("double", ncol(transaction))
names(transaction_uniques) <- names(transaction)
for (i in names(transaction)) {
  transaction_uniques[i] <- length(unique(transaction[[i]]))
}
transaction_uniques

# Re-order dotw factor from Sun, Mon, ... to Mon, ..., Sat, Sun
monday_first <- function(x) {
  forcats::fct_relevel(x, levels(x)[-1])  
}