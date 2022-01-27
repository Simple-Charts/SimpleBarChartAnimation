# Simple Bar Chart Animation  
  This is the simplified source code for creating a bar chart animation.  

## Example  
  [![Simple Charts / COVID-19 Cases and Deaths](https://img.youtube.com/vi/UiOHQF8lKxA/0.jpg)](https://www.youtube.com/watch?v=UiOHQF8lKxA "Simple Charts / COVID-19 Cases and Deaths")

## Data Source
  - COVID-19 Dataset by Our World in Data  
     https://github.com/owid/covid-19-data

## Setup  
  1. install Anaconda3-2020.02  
      https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe
  2. create virtual environment and install packages  
      conda create -n bca python==3.7.6 anaconda  
      conda activate bca  
      conda install -c conda-forge opencv==3.4.1  

## Usage  
  1. put csv data file in the same folder as python script  
  2. send commands in virtual environment of python  
     cd {folder path}  
     python SimpleBarChartAnimation.py  
