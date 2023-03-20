from os import system, name
from time import sleep

cars = [
    {'name': 'Chevrolet Tracker' , 'price_per_day': 120 , 'available_quantity': 2 , 'total_quantity': 2},  # changed into a list in order to use enumerate function and make code dynamic
    {'name': 'Chevrolet Onix' , 'price_per_day': 90 , 'available_quantity': 3 , 'total_quantity': 3},      
    {'name': 'Hyundai HB20' , 'price_per_day': 85 , 'available_quantity': 3 , 'total_quantity': 3},
    {'name': 'Hyundai Tucson' , 'price_per_day': 120 , 'available_quantity': 2 , 'total_quantity': 2},
    {'name': 'Fiat Uno' , 'price_per_day': 60 , 'available_quantity': 2 , 'total_quantity': 2},
    {'name': 'Fiat Mobi' , 'price_per_day': 70 , 'available_quantity': 3 , 'total_quantity': 3},
    {'name': 'Fiat Pulse' , 'price_per_day': 130 , 'available_quantity': 1 , 'total_quantity': 1}
]

rented_cars = []

index_list_cars = []
index_list_rented = []

positive_answers = ['Yes' , 'yes' , 'YES' , 'yEs' , 'yeS' , 'yES' , 'YeS' , 'Y' , 'y']
negative_answers = ['No' , 'no' , 'NO' , 'nO' , 'N' , 'n']



def menu():

    system('cls' if name == 'nt' else 'clear')
    
    print('----- WELCOME TO CBN CAR RENTAL ------\n')
    print('[1] : Portfolio')
    print('[2] : Rent a car')
    print('[3] : Return a car')
    print('[9] : Exit')
    menu_select_item = input('\nPlease, choose an option: ')

    while menu_select_item not in '1239':
        menu_select_item = input('>>> Please, insert a valid option: ')

    return menu_select_item



def portfolio():

    system('cls' if name == 'nt' else 'clear')
    index_list_cars.clear()

    print('..:: PORTFOLIO ::..\n')

    for index,car in enumerate(cars): #sempre que usamos dois parametros no "for", precisamos de dois parametros no "in". enumerate retorna duas coisas (tupla), assim como o .items
        print(str(index+1) + ': ' + car['name'] + ' - U$D ' + str(car['price_per_day']) + '/day (' + str(car['available_quantity']) +'/' + str(car['total_quantity']) + ')')
        index_list_cars.append(str(index+1))

    input('\n--> Press ENTER to go back to menu.')




def rent_car():

    system('cls' if name == 'nt' else 'clear')
    index_list_cars.clear()

    print('..:: RENT A CAR ::..\n')

    for index,car in enumerate(cars):
        print(str(index+1) + ': ' + car['name'] + ' - U$D ' + str(car['price_per_day']) + '/day (' + str(car['available_quantity']) +'/' + str(car['total_quantity']) + ')')
        index_list_cars.append(str(index+1))

    rent_choice = input('\nWhich car do you want to rent? ')
    while rent_choice not in index_list_cars:
        rent_choice = input('>>> Please, insert a valid car: ')
    rent_choice_dict_index = int(rent_choice) - 1
    print(cars[rent_choice_dict_index]['name'] + ' selected.')
        
    sleep(1)

    rent_choice_days = input('\nFor how many days do you want to drive your ' + cars[rent_choice_dict_index]['name'] + '? ')
    while True:
        try:
            rent_choice_days = int(rent_choice_days)
            break
        except:
            rent_choice_days = input('>>>Please, insert a valid ammount of days: ')

    print('\nThe cost of your {} rental for {} days will be {} dollars' .format(cars[rent_choice_dict_index]['name'] , rent_choice_days , cars[rent_choice_dict_index]['price_per_day'] * rent_choice_days))
    rent_answer = input('>>> Confirm rent? (Y/N) ')
    print('')

    if rent_answer in positive_answers:
        if (cars[rent_choice_dict_index]['available_quantity'] == cars[rent_choice_dict_index]['total_quantity']) and (cars[rent_choice_dict_index]['total_quantity'] != 1): #todos carros disponiveis

            cars[rent_choice_dict_index].update({'available_quantity': (cars[rent_choice_dict_index]['available_quantity']) - 1})                           
            rented_cars.append(cars[rent_choice_dict_index])
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nif 1') #debug
            input('\nCar rented sucessfully! Press ENTER to end process.')     

        elif (cars[rent_choice_dict_index]['available_quantity'] > 1) and (cars[rent_choice_dict_index]['total_quantity'] > 1): #meio termo
#                                          2                 > 1  and                             3               > 1
            cars[rent_choice_dict_index].update({'available_quantity': (cars[rent_choice_dict_index]['available_quantity']) - 1})          
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 2') #debug
            input('\nCar rented sucessfully! Press ENTER to end process.')

        elif (cars[rent_choice_dict_index]['available_quantity'] == 1) and (cars[rent_choice_dict_index]['total_quantity'] > 1): ##faltando um carro para ter todos alugados e excluir a lista

            cars[rent_choice_dict_index].update({'available_quantity': (cars[rent_choice_dict_index]['available_quantity']) - 1})
            cars.remove(cars[rent_choice_dict_index])
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 3') #debug
            input('\nCar rented sucessfully! Press ENTER to end process.')
 
        elif (cars[rent_choice_dict_index]['available_quantity'] == 1) and (cars[rent_choice_dict_index]['total_quantity'] == 1): #CARRO UNICO
            
            cars[rent_choice_dict_index].update({'available_quantity': cars[rent_choice_dict_index]['available_quantity']-1})
            rented_cars.append(cars[rent_choice_dict_index])
            cars.remove(cars[rent_choice_dict_index])
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 4') #debug
            input('\nCar rented sucessfully! Press ENTER to end process.')

    elif rent_answer in negative_answers:
        print('\nRedirecting you to the menu...')
        sleep(2)            




def return_car():
    
    system('cls' if name == 'nt' else 'clear')
    index_list_rented.clear()

    print('..:: RETURN A CAR ::..\n')

    for index,car in enumerate(rented_cars):
        print(str(index+1) + ': ' + car['name'] + ' - ' + str((car['total_quantity'] - car['available_quantity'])) + ' rented')
        index_list_rented.append(str(index+1))

    return_choice = input('\nWhich car do you want to return? ')
    while return_choice not in index_list_rented:
        return_choice = input('>>> Please, insert a valid car: ')
    return_choice_dict_index = int(return_choice) - 1
    print(rented_cars[return_choice_dict_index]['name'] + ' selected.')

    sleep(1)

    return_answer = input('Confirm car return? (Y/N) ')
    if return_answer in positive_answers:

        if (rented_cars[return_choice_dict_index]['available_quantity'] == 0) and (rented_cars[return_choice_dict_index]['total_quantity'] == 1): #CARRO UNICO

            rented_cars[return_choice_dict_index].update({'available_quantity': rented_cars[return_choice_dict_index]['available_quantity']+1})
            cars.append(rented_cars[return_choice_dict_index])
            rented_cars.remove(rented_cars[return_choice_dict_index])
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nif 1') #debug
            input('\nCar returned sucessfully! Press ENTER to end process.')


        elif ((rented_cars[return_choice_dict_index]['total_quantity']) - (rented_cars[return_choice_dict_index]['available_quantity']) == 1) and (rented_cars[return_choice_dict_index]['total_quantity']) > 1: #faltando 1 carro para ter todos

            rented_cars[return_choice_dict_index].update({'available_quantity': rented_cars[return_choice_dict_index]['available_quantity']+1})
            rented_cars.remove(rented_cars[return_choice_dict_index]) 
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 2') #debug
            input('\nCar returned sucessfully! Press ENTER to end process.')

                
        elif (rented_cars[return_choice_dict_index]['available_quantity'] == 0) and (rented_cars[return_choice_dict_index]['total_quantity'] > 1): #todos estiverem alugados
                    
            rented_cars[return_choice_dict_index].update({'available_quantity': rented_cars[return_choice_dict_index]['available_quantity']+1})
            cars.append(rented_cars[return_choice_dict_index]) # 1/3 cars
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 3') #debug
            input('\nCar returned sucessfully! Press ENTER to end process.')

        elif (rented_cars[return_choice_dict_index]['available_quantity'] > 0) and (rented_cars[return_choice_dict_index]['total_quantity'] > 1): #meio termo 

            rented_cars[return_choice_dict_index].update({'available_quantity': rented_cars[return_choice_dict_index]['available_quantity']+1})
            print(cars) #debug
            print('') #debug
            print(rented_cars) #debug
            print('\nelif 4') #debug
            input('\nCar returned sucessfully! Press ENTER to end process.')

    elif return_answer in negative_answers:
        print('\nRedirecting you to the menu...')
        sleep(2) 


# Processamento do menu e chamada das funções
if __name__ == '__main__':

    menu_selected_choice = '0'            

    while menu_selected_choice != '9':
        menu_selected_choice = menu()    # o menu() apenas retorna um valor, mas o código não faz nada com isso
                                         # para isso, criamos a variável menu_selected_choice para salvar o retorno da função menu()
                                         # sempre que escrevemos menu(), a função vai ser executada.
                                         # não botamos parametro na função menu() para que o retorno seja a propria função? asimov

        if menu_selected_choice == '1':
            portfolio()
        elif menu_selected_choice == '2':
            rent_car()
        elif menu_selected_choice == '3':
            return_car()
        elif menu_selected_choice == '9':
            print('\nExiting...')
            sleep(2)
        else:
            print('\nInvalid option.')
            input('--> Press ENTER to go back to menu.')