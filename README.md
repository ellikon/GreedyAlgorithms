# GreedyAlgorithms
Name: Luis Goicoechea - UFID:3500-9213

Name: Robert Miller - UFID:6705-1188

## Instructions to compile/build code 
Code was written using Python 3.12

## Instructions to run program
If using an IDE you only need to click Run on the cacheRequests.py files to make them run.
If using a console you can navigate to the /src folder where the files are and use the command "python3 cacheRequests.py ..\data\xxxxx where xxxxx is the name of the file you would like to use and is in the /data folder." (Replace '\' with '/' if using Linux or macOS)


## Assumptions
The input files will have k and m in the first line separated by a space where k >= 1 and m > 0. The second line will have m amount of entries each separated by a space. File should have the '.in' file extension

The output file will have the result for FIFO, LRU, OPTFF each on its own line and will use the same file name as the input but changing the '.in. extension to '.out'

## Question 1: Empirical Comparison
| Input File | k | m | FIFO | LRU | OPTFF |
|------------|---|---|------|-----|-------|
| Q1File1    | 4 |50 |   42  |  44  |  47  |
| Q1File2    | 5 |60 |   58  |  58  |  32  |
| Q1File3    | 6 |70 |   37  |  31  |  21  |

Does OPTFF have the fewest misses?
OPTFF always had the lowest amount of misses because it has full knowledge of the order of calls so it can optimize to the fewest misses possible

How does FIFO compare to LRU?
FIFO and LRU were very close to each other  in all 3 results and they had 1 result where they had the same amount of misses and one result each where they were better than the other. This would be based on the ordering of the requests where it could favor one over the other.

## Question 2: Bad Sequence for LRU or FIFO
For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO).

If such a sequence exists:

Construct one.

3 5

1 2 3 4 1

Compute and report the miss counts for both policies.
| Input File | k | m | FIFO | LRU | OPTFF |
|------------|---|---|------|-----|-------|
| Q2File     | 3 | 5 |   5  |  5  |  4  |

This happens because both FIFO and LRU do not know future information and replace the 1 as it is both the first request and the least recently used request. However OPTFF knows that request 1 will be requested again in the future while the other requests will not be requested again so it has less misses.
