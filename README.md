# 14-Day Weather Forecast Using an ETL Pipeline

This project showcases the weather forecast for any city for the next two weeks using an ETL pipeline. It extracts weather data from the VisualCrossing Statistical forecast dataset and transforms the raw data for meaningful analysis. As this is a personal project, I have just selected the basic metadata such as min/max temperature, precipitation type, humidity, UV index, and a general description. The dataset supports any city globally, which can be searched by either its name or coordinates. Once the data is transformed, it will be loaded onto a relational database using postgresql and the python module sqlalchemy. I will also look into having it loaded into Google Cloud Platform's BigQuery

Data is extracted from the historical weather dataset from visualcrossing.com, using an API call to retrieve the data as JSON. Once parsed I can see all data gathered to see what I need compared to what I do not.
