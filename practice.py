import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells

    # data
    import polars as pl
    import polars.selectors as cs
    import altair as alt

    alt.theme.enable("fivethirtyeight")

    # utils
    import os
    from pyhere import here
    from pathlib import Path

    # marimo
    import marimo as mo

    core_imports = [
        ("polars", pl),
        ("altair", alt),
        ("marimo", mo),
    ]
    for package, alias in core_imports:
        print(f"{package}:{alias.__version__}")


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ## Data
    For all questions, please assume the datasets (`cars.parquet`, `car_listings.parquet`, and `regions.csv`) are located in a `./data/` subfolder relative to your script or notebook.




    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Cars
    📁 **File:** `./data/cars.parquet`

    🚙 **Source:** https://jiji.co.ke/cars

    📖 **Description:**
    This dataset contains the core listing information for cars available on Jiji.co.ke. Each row represents a distinct car advertisement and includes unique identifiers for both the listing and the user who posted it. It also specifies the region of the listing, the ad's title, and detailed pricing information. The price is *inconveniently* provided in both a ready-to-display format and a structured JSON format.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    _df = mo.sql(
        f"""
        from
            read_parquet('./data/cars.parquet')
        limit
            5
        """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Car Listings
    📁 **File:** `./data/car_listings.csv`

    🚙 **(Example) Source:** https://jiji.co.ke/thika/cars/toyota-succeed-2007-white-yogtOZErD8R3fKAPXb86DsnX.html

    📖 **Description:**
    This dataset offers detailed attributes for each car listing. It contains vehicle specifications such as the make, model, year of manufacture, color, and current condition. It also includes performance metrics like the number of views the listing has.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    _df = mo.sql(
        f"""
        from
            read_parquet('./data/car_listings.parquet')
        limit
            5
        """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Regions
    📁 **File:** `./data/regions.csv`

    📖 **Description:** This dataset contains geo information about the listing regions. It maps each region_id to a more descriptive region name, a URL-friendly "slug," and the county where the region is situated.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    _df = mo.sql(
        f"""
        from
            read_csv('./data/regions.csv')
        limit
            5
        """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Questions""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 1

    **Getting Started - Reading and Cleaning Data**

    **Objective:** This question introduces the process of loading data from different file formats (Parquet and CSV) and performing initial data cleaning by renaming columns for consistency.

    **Task:**
    Your first assignment is to load the `cars` and `car_listings` datasets into Polars DataFrames. Both datasets are stored in parquet files, `cars.parquet` and `car_listings.parquet`. After loading, standardize the column names in the `car_listings` DataFrame to "snake_case" (e.g., `LISTING ID` should become `listing_id`). To confirm your work, display the first few rows of each DataFrame.


    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint

    *   Use the `pl.read_parquet()` function to load the data (e.g., `pl.read_parquet('your_dataset.parquet')`).
    *   To rename columns, Python's string methods like `.lower()` and `.replace()` will be very useful here.
    *   **Documentation Links:**
        *   [`polars.read_parquet()`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_parquet.html)
        *   [`DataFrame.rename()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.rename.html#polars.DataFrame.rename)
    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 2

    **Data Types and Transformation**

    **Objective:** This exercise focuses on inspecting and modifying column data types, and extracting valuable information from string columns.

    **Task:**
    In the `car_listings` DataFrame, the `date_created` column is currently stored as a string. Your task is to convert this column to a proper datetime type. Additionally, the `cars` DataFrame contains a `price_obj` column of type [struct](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Struct.html#polars.datatypes.Struct). Extract the numerical price `value` from this column and create a new integer column named `price`.


    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint
    *   Use the `.with_columns()` method to add or modify columns.
    *   For date conversion, use an expression with `pl.col('date_created').str.to_datetime()`. You may need to specify the format of the date string.
    *   To extract data from a struct, use `pl.col('price_obj').struct.field('value')` to access the nested `value` field. 
    *   **Documentation Links:**
        *   [`DataFrame.with_columns()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.with_columns.html)
        *   [`Series.str.to_datetime()`](https://docs.pola.rs/api/python/stable/reference/series/api/polars.Series.str.to_datetime.html)
        *   [`Series.struct.field()`](https://docs.pola.rs/api/python/stable/reference/series/api/polars.Series.struct.field.html)
        *   [`chrono`](https://docs.rs/chrono/latest/chrono/format/strftime/index.html)

    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 3
    **Merging Datasets**

    **Objective:** Learn how to combine data from multiple DataFrames using a shared key, a fundamental operation in data analysis.

    **Task:**
    You now have two separate DataFrames: one with basic car listing information and another with detailed car attributes. Your goal is to merge these two DataFrames into a single, comprehensive DataFrame using the `listing_id` column. To further enrich the data, join the resulting DataFrame with the `regions.csv` dataset (you'll need to read it first) on the `region_id` column. Display the first 5 rows of the final merged DataFrame to verify the result.


    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint
    *   Use the `.join()` method on a DataFrame.
    *   Specify the column to join on using the `on` parameter.
    *   You will need to perform two separate joins to combine all three datasets.
    *   **Documentation Links:**
        *   [`DataFrame.join()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.join.html)
        *   [`polars.read_csv()`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html)


    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 4
    **Filtering for Insights**

    **Objective:** This question teaches you how to select specific subsets of data based on defined criteria, allowing for more focused analysis.

    **Task:**
    Using the merged DataFrame from the previous question, perform the following filtering operations:
    1.  Isolate all car listings located in "Nairobi" county.
    2.  From the Nairobi listings, identify all cars that are "Foreign Used."
    3.  Further narrow down these results to include only cars manufactured in or after 2018.

    How many cars in the dataset meet all of these criteria?

    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint
    *   Use the `.filter()` method.
    *   You can create complex conditions by combining multiple expressions with the `&` (and) operator.
    *   Use comparison operators like `==` (equals) and `>=` (greater than or equal to).
    *   **Documentation Link:**
        *   [`DataFrame.filter()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.filter.html)


    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 5
    **Grouping and Aggregation**

    **Objective:** This task will help you understand how to group data by a specific category and perform aggregate calculations to summarize the information.

    **Task:**
    Using the fully merged and cleaned DataFrame, calculate the average price of cars for each `make` (e.g., Toyota, Subaru, BMW). In addition to the average price, determine the total number of listings for each make. Your final output should be a DataFrame that displays the make, the average price, and the count of listings, sorted by the average price in descending order.



    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint
    *   Chain the `.group_by()` and `.agg()` methods.
    *   Inside `.agg()`, define the aggregations you want to perform, such as `pl.mean('price')` and `pl.count()`. You can use `.alias()` to rename the resulting columns.
    *   After aggregation, use the `.sort()` method to order your results.
    *   **Documentation Links:**
        *   [`DataFrame.group_by()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.group_by.html)
        *   [`GroupBy.agg()`](https://docs.pola.rs/api/python/stable/reference/groupby/api/polars.GroupBy.agg.html)
        *   [`DataFrame.sort()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html)
    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 6
    **Visualization**

    **Objective:** This final question introduces the basics of data visualization, teaching you how to create a simple plot directly from a Polars DataFrame.

    **Task:**
    Based on the aggregated data from the previous question, create a bar chart to visualize the average price for the top 10 most expensive car makes. The x-axis should represent the car `make`, and the y-axis should display the average `price`. Ensure your plot includes a clear title and labels for both axes.

    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### 💡 Hint
    *   Polars has a built-in `.plot` accessor that uses the **Altair** library.
    *   Start with your sorted, aggregated DataFrame and select the top 10 rows using the `.head(10)` method.
    *   You can then directly call the `.plot.bar()` method on this new DataFrame. Set the `x` parameter to your 'make' column and the `y` parameter to your average price column (e.g., `df.plot.bar(x='make', y='price_mean')`).
    *   **Documentation Links:**
        *   [`DataFrame.plot`](https://docs.pola.rs/api/python/stable/reference/dataframe/plot.html)
        *   [`DataFrame.head()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.head.html)
    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Question 7 (Bonus)
    **Objective:** This final question challenges you to revisit the entire analysis from questions 1 through 5. Your goal is to reproduce the final aggregated result from Question 5 by rebuilding the whole data pipeline using either marimo's (DuckDB) SQL cells or Polars' Lazy API.

    **Task:** Choose either Path A or Path B below to rebuild the entire data pipeline and produce the final result from Question 5: the average price and listing count for each car make, sorted by average price.

    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### **Path A: Leveraging DuckDB**

    If you have a background in SQL or want to see how Polars integrates with the SQL world, this path is for you. You will use SQL cells to perform all the joining, transformation, and aggregation steps in a single, comprehensive query.

    **Specific Task:**
    Load the three initial DataFrames (`cars`, `car_listings`, `regions`) using SQL and then use a single SQL cell in your marimo notebook to write a query that joins them, performs the necessary cleaning and filtering, and produces the final aggregated table from Question 5.
    """
    )
    return


@app.cell
def _():
    _df = mo.sql(
        f"""

        """
    )
    return


@app.cell
def _():
    _df = mo.sql(
        f"""

        """
    )
    return


@app.cell
def _():
    _df = mo.sql(
        f"""

        """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    #### **Path B: Method Chaining with LazyFrames**

    If you want to experience the full power of Polars' query optimizer, this path is for you. You will rewrite your entire workflow—from reading the files to the final aggregation—as a single, continuous chain of operations using Polars' LazyFrame API.

    **Specific Task:**
    Refactor your entire solution from Question 1 to 5 into one chain of methods. Start by scanning the files lazily and only trigger the computation with a single `.collect()` call at the very end to produce the final table from Question 5.
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
