# Canned code for R (using tidyverse packages)


Tips:
Look at each table and figure out what is the key
Count unqiues for each column, remove duplicates
Make sure that unique identifiers (eg people ID) are the same in tables that are to be joined



# IMPORTING DATA

# Read in many CSVs with sa me headers:
files <- dir("data/", pattern = "\\.csv$", full.names = TRUE)
df <- vector("list", length(files))
for (i in seq_along(files)) {
  df[[i]] <- read_csv(file = files[[i]])
}
df <- bind_rows(df)
df


# DATA WRANGLING

# data types
# find the types of each column:
str()

# filter table
table %>% filter(Year == '2004')

# Reassign errors in column 'col'
table_clean <- table %>%
  mutate(
    col = ifelse(col == 'error', 'new value', col)
  )



# Simple aggregations: 
table %>% group_by(column) %>% count() # Select column, count(*) from table group by column


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

count(colname)
count(unique(colname))
# remove duplicates:
df <- df %>% unique()


# PLOTTING

# Save multiple plots: 
library(ggplot2)
plots <- mtcars %>%
  split(.$cyl) %>%
  map(~ggplot(., aes(mpg, wt)) + geom_point())
paths <- stringr::str_c(names(plots), ".pdf")
pwalk(list(paths, plots), ggsave, path = tempdir())
