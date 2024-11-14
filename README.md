# sqlalchemy-challenge

**Task**

*Part 1: Analyze and Explore the Climate Data*
    1. Use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database using SQLAlchemy ORM queries, Pandas, and Matplotlib. 
    2. Code effectively runs in Jupyter Notebook.

*Part 2: Design Your Climate App*
    1. Design a Flask API based on the queries that you just developed.
    2. Code effectively runs in VS code.

**Data Engineering**

    1. numpy 
    2. pandas 
    3. datetime
    4. matplotlib 
    5. matplotlib.pyplot
    6. style.use: fivethirtyeight
    4. sqlalchemy.ext.automap: automap_base
    5. sqlalchemy.orm: Session
    6. sqlalchemy: create_engine, func
    7. flask: Flask, jsonify

**Data Resources**

    1. Climate starter.ipynb 
    2. Hawaii sqlite file 
    3. hawaii measurement csv
    4. hawaii stations csv

**Coding**

    part. 1

        1. SQLAlchemy ORM was seemless. No issues

        2. Performing the exploratory analysis was challenging. Specifically, coding was hit or miss in attemping to calculate 
            the date one year from the last date in data set and using Pandas Plotting with Matplotlib to plot the data. 
            Assistance was required from the instructor and review of Jleigh101 at https://github.com/JLeigh101/sqlalchemy-challenge.git. 
            to point me in the right direction.

    
    Part 2.

        1. The following provided API's required a code adjustment to run effectively:

             "/api/v1.0/<start><br/>"
            "/api/v1.0/<start>/<end><br/>"

           specifically, the <> bracktes had to removed from the start and end statements in order for their respective @app.route() 
           and queries fucntion to opertate without errors.
        
        2. After making the aforementined adjustments, the Flask API performed the following:

           a. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified 
              start or start-end range.
           b. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
           c. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to 
              the end date, inclusive.

**Analysis results**

    The climate analysis of hawaii has shown that Station USC00519281 is the most active station wiht a minimum temperature of 54.0, maximum temperatue of 85.0, resulting in an average temperature of 72.0.


