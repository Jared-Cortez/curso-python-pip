import utils
import read_csv
import charts

def run():
  
  Escala = input('Type Scale => ')

  data = read_csv.read_csv('data.csv')

  if Escala == 'Country':
    country = input('Type Country => ')
    result = utils.population_by_country(data, country)

    if len(result) > 0:
      country_name = country 
      country = result[0]
      labels, values = utils.get_population(country)
      charts.generate_bar_chart(country_name,labels, values)
  
  if Escala == 'Continent':
    continent = input('Type Continent => ')
    labels, keys = utils.world_population(data, continent)
    charts.generate_pie_chart(continent, labels, keys)

if __name__ == '__main__':
  run()