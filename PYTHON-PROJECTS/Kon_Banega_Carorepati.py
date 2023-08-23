
print('\n=============================================================')
print('\tWelcome to the game (KON BANEGA CAROREPATI)')
print('=============================================================')

while True:
    print("\n\t1. Type -Rules- to read the rules of the game.")
    print("\n\t2. Type -Start- to start the game.")
    print("\n\t3. Type -Exit- to exit the game.")

    user_input = input('\nEnter your input: ')

    match user_input:
        case 'Rules':
            print('\n=============================================================')
            print('\t\t\t RULES OF GAME')
            print('=============================================================\n')

            print("1. There are some questions in game and you have to give a correct answer of each question. \n2. All questions are compulsory. \n3. Each and every question contain 4 options you have to chose 1 correct answer out of four. \n4. each correct answer have some specific prizepool that is given below:- \n\n\t A) 1st Question  - Rs.100 \n\t B) 2nd Question  - Rs.500 \n\t C) 3rd Question  - Rs.1000  \n\t D) 4rth Question - Rs.10,000 \n\t e) 5th Question  - Rs.50,000 \n\t f) 6th Question  - Rs.1,00,000 \n\t g) 7th Question  - Rs.10,00,000 \n\t h) 8th Question  - Rs.30,00,000 \n\t i) 9th Question  - Rs.70,00,000 \n\t j) 10th Question - Rs.1,00,00,000\n\n")

        case 'Start':
            print('\n=============================================================')
            print('\t\t\t ALL THE VERY BEST')
            print('=============================================================\n')

            ques_list = [
                ["1: The International Literacy Day is observed on","September 8","November 28","May 2","September 22","September 8",'a'],

                ["2: The language of Lakshadweep. a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu","Malayalam",'c'],

                ["3: In which group of places the Kumbha Mela is held every twelve years?","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,\'Haridwar","Prayag. Haridwar, Ujjain,. Nasik",'b'],

                ["4: Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism",'d'],

                ["5: Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2","Oct 14",'b'],

                ["6: Which of the following was the theme of the World Red Cross and Red Crescent Day?","Dignity for all - focus on women","Dignity for all - focus on Children","Focus on health for all","Nourishment for all-focus on children","Dignity for all - focus on Children",'b'],

                ["7: September 27 is celebrated every year as","Teacher\'s Day","National Integration Day","World Tourism Day","International Literacy Day","World Tourism Day",'c'],

                ["8: Who is the author of \'Manas Ka-Hans\' ?","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar",'d'],

                ["9: The death anniversary of which of the following leaders is observed as Martyrs\' Day?","Smt. Indira Gandhi","PT. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri","Mahatma Gandhi",'c'],

                ["10:  Who is the author of the epic Meghdoot?","Vishakadatta","Valmiki","Banabhatta","Kalidas",'d'],
            ]

            price = [100,500,1000,10000,50000,100000,1000000,5000000,10000000,70000000]
            
            for i in range(len(ques_list)):
                ques = ques_list[i]
                print(f'~ The question on your computer screen is for Rs.{price[i]} ~\n')
                print(ques_list[i][0])
                print(f"\n\ta) {ques_list[i][1]} \n\tb) {ques_list[i][2]} \n\tc) {ques_list[i][3]} \n\td) {ques_list[i][4]}")

                ans = input("\n\tEnter your answer: ")
                if (ans == ques_list[i][-1]):
                    print('\n\t[~ Right Answer ~]\n')
                    print(f'\t~ Congratulations You won - Rs.{price[i]} ~\n')
                    print('------------------------------------------------------------------------------------\n')
                elif (ans!='a' and ans!='b' and ans!='c' and ans!='d'):
                    print('\n\t[~ Wrong input! You cannot enter the input out of options (A,B,C,D) ~]\n')
                    print('------------------------------------------------------------------------------------\n')
                    print('~Your Game is end here! because You enter a wrong input. You can only continue your game by giving correct answer or correct input otherwise you cannot play further.~\n')
                    break
                elif (ans != ques_list[i][-1]):
                    print('\n\t[~ Wrong Answer! ~]')
                    print('\n\tCorrect answer: ',ques_list[i][-1],'-',ques_list[i][-2])
                    print('------------------------------------------------------------------------------------\n')
                    print('~Your Game is end here! because You enter a wrong answer. You can only continue your game by giving correct answer otherwise you cannot play further.~\n')
                    break
        case 'Exit':
            print('\n **** THANKS FOR PLAYING! GOODBYE! ***\n')
            break      