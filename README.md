# 🌡️ Extreme Temperature Analysis using Hadoop MapReduce

This project detects the hottest cities per year from the [Historical Hourly Weather Data](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data) using Hadoop MapReduce.

We process the `temperature.csv` file in two MapReduce steps:
1. Find the hottest city for each **day**.
2. Then, from the daily results, find the hottest city for each **year** in Celsius.

📥 Output  
<img src="https://github.com/user-attachments/assets/6a89c7ab-8a86-463e-bcca-1f2bf2ebe7f0" width="500"/>

---

## 📁 Project Structure

weather_data/
    ├── temperature.csv # Input dataset
    ├── mapper.py # Mapper for daily maximum
    ├── reducer.py # Reducer for daily maximum
    ├── mapper2.py # Mapper for yearly maximum
    ├── reducer2.py # Reducer for yearly maximum (with Celsius conversion)
    ├── README.md # This file 

---
## 📌 Setup & Prerequisites

Ensure you have the following:
- Hadoop installed and running (tested on Hadoop 2.x/3.x)
- Python 3 installed
- Dataset: [temperature.csv](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data)

---

## ✅ Step-by-Step Instructions

### Step 1: Upload Dataset to HDFS

```bash
# Create input directory in HDFS
hdfs dfs -mkdir -p /user/vindyani/input_temp

# Upload temperature.csv to HDFS
hdfs dfs -put temperature.csv /user/vindyani/input_temp/

```

### Step 2: Run First MapReduce Job (Daily Maximums)

This job finds the hottest city per day.

```bash
hadoop jar /path/to/hadoop-streaming.jar \
 -input /input_temp/temperature.csv \
 -output /output_temp_daily \
 -mapper mapper.py \
 -reducer reducer.py \
 -file mapper.py \
 -file reducer.py

```
📥 Output format:

```bash
2014-06-20	Eilat	316.2
2014-06-21	Phoenix	314.27
```

### Step 3: Run Second MapReduce Job (Yearly Maximums in °C)

This job analyzes daily hottest cities and finds the hottest city per year, converting temperatures from Kelvin to Celsius.

```bash
hadoop jar /path/to/hadoop-streaming.jar \
 -input /output_temp_daily \
 -output /output_temp_yearly \
 -mapper mapper2.py \
 -reducer reducer2.py \
 -file mapper2.py \
 -file reducer2.py
```
📥 Output format:

```bash
2012	Phoenix	43.30 °C
2013	Cairo	45.52 °C
2014	Dubai	46.06 °C
```
### View Output

```bash
hdfs dfs -cat /output_temp_yearly/part-00000
```

### Clean Up HDFS(Optional)

```bash
hdfs dfs -rm -r /input_temp
hdfs dfs -rm -r /output_temp_daily
hdfs dfs -rm -r /output_temp_yearly
```

### ⚠️ Notes

- Input temperatures are in Kelvin.

- Final results are in Celsius (rounded to 2 decimal places).

- All scripts use tab-separated fields.

- If any script fails, ensure it has executable permissions: ```bash chmod +x mapper.py reducer.py mapper2.py reducer2.py```
