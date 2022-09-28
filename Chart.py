import matplotlib.pyplot as plt

def makeMacroChart(nutrients):
    macros = [nutrients.get('carbohydrateContent').strip(' g'), nutrients.get('fatContent').strip(' g'), 
            nutrients.get('proteinContent').strip(' g')]

    labels = 'Carbs', 'Fat', 'Protein'

    fig1, ax1 = plt.subplots()
    ax1.pie(macros, labels=labels, autopct='%1.1f%%',
        startangle=90)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return fig1