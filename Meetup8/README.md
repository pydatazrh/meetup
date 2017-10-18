# Meetup 8
- Swiss Python Summit (Feb 16, 2018) - Submit your talk proposal before end of October
- PyData tools in Noble Prize for Physics - https://twitter.com/PyData/status/915263419703586816

## Dash Info

A repository for getting started with Dash using Jupyter and Docker (https://github.com/4Quant/DashIntro)


- Try using [![Binder](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/4Quant/DashIntro/master)

### Getting Started 

#### Build

To make the image yourself you can use the 
```
docker build . -t dashdemo
```

#### Pull (preferred)

```
docker pull 4quant/dashdemo
```


#### Run

```
docker run --rm -p 8888:8888 -p 9999:9999 -t dashdemo
```

#### Run (with editable notebooks)

```
docker run --rm -p 8888:8888 -p 9999:9999 -v $(pwd)/notebooks:/home/dash_demo/notebooks -t dashdemo
```

## Modern Python fund analytics

Check out the slide deck on [modern Python fund analytics](modern_pension_fund_analytics.pdf) with jupyter, pandas and dash. 
It gives a short overview of the analytics layer built with best practice open source methods by Pensionskasse Credit Suisse 
(Schweiz) and d-fine. Demo files not included, so for more information contact Christian Fischer or Markus Baden (@markusbaden).
