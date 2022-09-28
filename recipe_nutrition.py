import streamlit
from recipe_scrapers import scrape_me
import pandas as pd
import matplotlib.pyplot as plt
import Chart as ch

streamlit.title('Recipe Nutrition Calculator')
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
ingredients_df = pd.DataFrame(scraper.ingredients())
streamlit.dataframe(ingredients_df)


streamlit.text(scraper.nutrients())
streamlit.text(type(scraper.nutrients()))
nutrients = scraper.nutrients()
nutrition_df = pd.Series(nutrients, name ='Value')
nutrition_df.index.name = 'Type'
nutrition_df.reset_index()
streamlit.dataframe(nutrition_df)


streamlit.pyplot(ch.makeMacroChart(nutrients))