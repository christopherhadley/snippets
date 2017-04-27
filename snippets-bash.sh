# Snippets of code for bash command line



# EXPLORING CONTENTS OF FILES

# Find length (numer of lines) of all CSV files in a dir: 
ls -1 *.csv | xargs wc -l

# Maniputlating CSVs
# Extract first column
cut -d , -f 1 input-test.csv
# .. save to another file:
cut -d , -f 1 input-test.csv >> postcodes_a.csv

# CONCATENATING FILES ETC

# create a text file
touch foo.bar

# create a new file with some contents:
cat > foo.csv
1,2,3
4,5,6
control+c

echo "1,2,3" > foo.csv

# Append some stuff to a file:
cat >> foo.csv
1,2,3
4,5,6
control+c

# Add contents of one file to another:
cat < foo.csv >> 1.csv

# < is intput
# > is output

# Copy first 50 lines of one file to a new one
head -50 old.csv >> new.csv



# RENAMING FILES

# batch rename files - eg: I have several *_test.csv files, and want to remove this suffix - use the following
for f in *.csv; do echo mv "$f" "${f/\_test/}"; done # the echo allows you to check that the script produces the right output before going ahead with it
for f in *.csv; do mv "$f" "${f/\_test/}"; done
# characters need to be escaped etc

# replace '*foo*.csv' with '*bar*.csv'
for f in *.csv; do echo mv "$f" "${f/foo/bar}"; done

# you can also use rename (install via brew)
rename 's/^linux_//' linux_*.mp4





# FINDING

# find files in all directories below the current: 
 find . -name 'filenamewearelookingfor'







# GIT STUFF

# download a single file (useful for downlaod a single CSV from GitHub without cloning a repo - hit 'raw' button)
# this saves it to the cwd: 
curl -O https://raw.githubusercontent.com/fivethirtyeight/data/master/thanksgiving-2015/thanksgiving-2015-poll-data.csv
# this outputs to stdout:
curl https://raw.githubusercontent.com/fivethirtyeight/data/master/thanksgiving-2015/thanksgiving-2015-poll-data.csv