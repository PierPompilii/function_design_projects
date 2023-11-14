1- Describe the problem

As a user:
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2-Design the function signature

```python
def estimate_reading_time(text):
    #paramenter:
#    size of a string 
    #return
# average of time to read a text eg 10 minutes for 2000 words 
pass 
```


3-Create examples as test

given 0 text words
return the time

estimate_reading_time (0) = 0
given a text with 200 words 
it return the time that takes to read that

estimate_reading_time(200 words) => [1]


given a text with less than 200 words 
return the time that takes to read that

estimate_reading_time_less200(100 words) => [0.5]

given a text with more than 200 words
return the time 

estimate_reading_time_more200(450 words) => [2.25]

4-Implement behaviour