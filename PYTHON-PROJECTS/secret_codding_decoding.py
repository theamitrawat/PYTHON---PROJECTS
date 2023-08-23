print('\n===========================================================================================================')
print('\t\t\t\t\tSECRET CODE DECODE PROGRAMME')
print('===========================================================================================================\n')

characters_list= ['a','b','/','c','d', 'f','|','e','#','g','h','~','i','j','!','k','l','@','m','n', '#','o','p','%','q' ,'r','^','s','t','&','u','v','*','w','x','(','y','z',')','B','A', '_','D','C','-','F','E','+','H','F','G','H','I','=','J','K','{','L','M','}','N' ,'O','P','Q','R','S',':','T','U',';','V','W','"','X','>','<','Z','Y','?','0','1','2','3','4','5','6','7','8','9',]

while True:

    print("\n\tInput [ code ] to convert your message to Secret Code message.")
    print("\tInput [ decode ] to decode your Secret message to normal message.")
    print("\tInput [ exit ] to exit the coding and decoding task.\n")

    user_input = input('~@input.your.command:~ ')
    match user_input:

        case 'code':
            import random

            message = input('\n\tEnter your Message: ')
            msg_words = message.split(" ")

            new_msg_code = []
            for sep_word in msg_words:
                if (len(sep_word)==3):
                    ran_word_1 = random.sample(characters_list,4)
                    ran_word_2 = random.sample(characters_list,4)                  
                    ran_string_1 = ''.join(ran_word_1)
                    ran_string_2 = ''.join(ran_word_2)
                    
                    new_string =  ran_string_1 + sep_word[1:] + ran_string_2 + sep_word[0] 
                    new_msg_code.append(new_string)                   

                elif (len(sep_word)>3):
                    ran_word_1 = random.sample(characters_list,4)
                    ran_word_2 = random.sample(characters_list,4)                  
                    ran_string_1 = ''.join(ran_word_1)
                    ran_string_2 = ''.join(ran_word_2)
                    
                    new_string =  sep_word[-2:]+ ran_string_1 + sep_word[:2] + ran_string_2 + sep_word[2:-2] 
                    new_msg_code.append(new_string)

                else:
                    new_msg_code.append(sep_word[::-1])
            print(f'\nSECRET CODED MESSAGE:-   {" ".join(new_msg_code)}')            

        case 'decode':

            message = input('\n\tEnter your Message: ')
            msg_words = message.split(" ")

            new_msg_code = []
            for sep_word in msg_words:
                if (len(sep_word)==11):
                                        
                    # new_string =  ran_string_1 + sep_word[1:] + ran_string_2 + sep_word[0]
                    new_string = sep_word[-1] + sep_word[4:6] 
                    new_msg_code.append(new_string)

                elif (len(sep_word)>11):
                    new_string =  sep_word[6:8] + sep_word[12:] + sep_word[:2] 
                    new_msg_code.append(new_string)

                else:
                    new_msg_code.append(sep_word[::-1])
            print(f'\n DECODED MESSAGE :-   {" ".join(new_msg_code)}\n')

        case 'exit':

            print('\n **** Thanks For Using our Programme! Goodbye! ***\n')
            break 