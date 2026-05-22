def quality_multiplication():
    import time
    time.sleep(1)
    print('You have chosen the quality system and multiplication operation.')
    time.sleep(1)
    print('Complete 40 hard multiplication questions.')
    time.sleep(1)
    print('You have 18 seconds per question.')
    time.sleep(1)
    print('You need 80% accuracy to earn a star.')
    time.sleep(1)
    print('Good luck!\n')
    time.sleep(1)

    def daily_mission():
        import random
        import time

        stars = 0
        qa = 0
        qac = 0

        while qa < 40:
            a = random.randint(20, 100)
            b = random.randint(20, 100)
            answer = a * b

            start_time = time.time()

            user_answer = input(f'What is {a} * {b}? ')

            end_time = time.time()
            time_taken = end_time - start_time

            # timer check
            if time_taken > 18:
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
                        qac += 1

                    else:
                        time.sleep(1)
                        print('Wrong!')
                        time.sleep(1)
                        print('Correct answer was', answer)

                else:
                    print('Please enter numbers only.')

            qa += 1

        accuracy = qac / qa * 100
        time.sleep(1)
        print('Daily mission completed!')
        time.sleep(1)
        print(f'Correct: {qac}/{qa}')
        time.sleep(1)
        print(f'Accuracy: {accuracy:.1f}%')

        if accuracy >= 80:
            stars += 1
            print('You earned 1 star!')
        else:
            print('No star earned today.')

    daily_mission()
