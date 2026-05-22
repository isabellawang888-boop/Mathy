def quantity_subtraction():
    import time
    time.sleep(1)
    print('You have chosen the quantity system and subtraction operation.')
    time.sleep(1)
    print('Complete 60 easy subtraction questions.')
    time.sleep(1)
    print('You have 14 seconds per question.')
    time.sleep(1)
    print('Good luck!\n')
    time.sleep(1)

    def daily_mission():
        import random
        import time
        stars = 0
        qa = 0

        while qa < 60:
            a = random.randint(10, 80)
            b = random.randint(10, a)
            answer = a - b

            start_time = time.time()

            user_answer = input(f'What is {a} - {b}? ')

            end_time = time.time()
            time_taken = end_time - start_time

            # timer check
            if time_taken > 14:
                time.sleep(1)
                print('you take to long to answer!')
                time.sleep(1)
                print('Correct answer was', answer)

            else:
                # prevent crash
                if user_answer.isdigit():

                    if int(user_answer) == answer:
                        time.sleep(1)
                        print('Correct!')

                    else:
                        time.sleep(1)
                        print('Wrong!')
                        time.sleep(1)
                        print('Correct answer was', answer)

                else:
                    print('Please enter numbers only.')

            qa += 1

        print('Daily mission completed!')
        stars += 1
        time.sleep(1)
        print('You earned 1 star!')

    daily_mission()
