
import corona

corona_data = corona.data[0]

# State
# cases
# recovered 
# active 

total_recovered = 0
most_recovered = corona_data[0]['recovered']
most_recovered_state = corona_data[0]['state']
least_recovered = corona_data[0]['recovered']
least_recovered_state = corona_data[0]['state']

# find state with most recovered
# find state with least recovered

# print(corona_data)

for i in corona_data:
    print(f"""\n
          State : {corona_data[i]['state']}
          Cases : {corona_data[i]['cases']}
          Recovered : {corona_data[i]['recovered']}
          Active : {corona_data[i]['active']} 
          """)
    total_recovered += corona_data[i]['recovered']
    if corona_data[i]['recovered'] > most_recovered:
        most_recovered_state = corona_data[i]['state']
        most_recovered = corona_data[i]['recovered']
    if corona_data[i]['recovered'] < least_recovered:
        least_recovered_state = corona_data[i]['state']
        least_recovered = corona_data[i]['recovered']

print(f"""\n
      Total recovered cases : {total_recovered}
      Most recovered cases : {most_recovered_state} - {most_recovered}
      Least recovered cases : {least_recovered_state} - {least_recovered}
      """)    