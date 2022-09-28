import streamlit
from recipe_scrapers import scrape_me
import pandas

streamlit.title('Recipe Nutrition Calculator')
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
ingredients_df = pandas.DataFrame(scraper.ingredients())
streamlit.dataframe(ingredients_df)


streamlit.text(scraper.nutrients())
streamlit.text(type(scraper.nutrients()))
nutrition_df = pandas.DataFrame.from_dict(scraper.nutrients(), orient='index',
                       columns=['Type', 'Value']).index([0])
streamlit.dataframe(nutrition_df)