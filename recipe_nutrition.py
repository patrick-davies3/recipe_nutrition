import streamlit
from recipe_scrapers import scrape_me
import pandas as pd
import matplotlib.pyplot as plt

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
macros = [nutrients.get('carbohydrateContent').strip(' g'), nutrients.get('fatContent').strip(' g'), 
            nutrients.get('proteinContent').strip(' g')]

labels = 'Carbs', 'Fat', 'Protein'

fig1, ax1 = plt.subplots()
ax1.pie(macros, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

streamlit.pyplot(fig1)