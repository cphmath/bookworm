# Bookworm
Data analysis of Seattle Public Library checkouts by title 2005-2020 from
https://data.seattle.gov/Community/Checkouts-by-Title/tmmm-ytt6

### Analysis
With everyone inside the last few months, I have been reading a lot more. I
wanted to see if others in Seattle had done the same. I analyzed digital
checkout trends from 2017-2020 to see if there was an incremental increase in
digital checkouts during covid-19

See the full analysis in [notebooks/digital_checkout_incrementality](https://github.com/cphmath/bookworm/tree/master/notebooks/digital_checkout_incrementality.ipynb)


### Setup
After cloning the repo, create a file called config.yml in the main directory.
Minimally, add the following information:
```
app_token: None
domain: "data.seattle.gov"
dataset_id: 'tmmm-ytt6' # Checkouts By Title dataset identifier
```
If you have an app token for data.seattle.gov you can add that as a string in
front of app_token, but you can run the code without one.

I wrote this code using python 3.8.3 and all the modules I used can be installed
with `pip install -r requirements.txt`
