import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('C:/Users/Usuario/Programación/Python/app/data.csv')
  data = list(filter(lambda item : item["Continent"] == "South America", data))
  
  countries = list(map(lambda x: x['Country'], data))
  #Implementación de las lambda Functión para  simplicar el porceso de Recopliació ne Datos
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country"],  labels, values)  # Remove the extra argument

if __name__ == '__main__':
  run()
  
