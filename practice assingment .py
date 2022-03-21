def main():
    score1,score2,score3,score4,score5,avg=calc_average()
    letter1,letter2,letter3,letter4,letter5,letter6= determine_grade(score1,score2,score3,score4,score5,avg)
    print('score                  numeric grade       letter grade')
    print('--------------------------------------------------------------')

    print(f'score 1:              {score1:12,.2f}         {letter1}')

    print(f'score 2:              {score2:12,.2f}         {letter2}')

    print(f'score 3:              {score3:12,.2f}         {letter3}')

    print(f'score 4:              {score4:12,.2f}         {letter4}')

    print(f'score 5:              {score5:12,.2f}         {letter5}')

    print(f'average score:        {avg:12,.2f}            {letter6}')



def calc_average():
    score1=float(input('enter test score: '))
    score2=float(input('enter test score: '))
    score3=float(input('enter test score: '))
    score4=float(input('enter test score: '))
    score5=float(input('enter test score: '))
    total=score1+score2+score3+score4+score5
    avg=total/5
    return score1,score2,score3,score4,score5,avg

def determine_grade(score1,score2,score3,score4,score5,avg):
    if score1>90 and score1<100:
        letter1='A'
    elif score1>80 and score1<89:
        letter1='B'
    elif score1>70 and score1<79:
        letter1='C'
    elif score1>60 and score1<69:
        letter1='D'
    else:
        letter1='F'
        if score2>90 and score2<100:
            letter2='A'
        elif score2>80 and score2<89:
            letter2='B'
        elif score2>70 and score2<79:
            letter2='C'
        elif score1>60 and score1<69:
            letter2='D'
        else:
            letter2='F'
            if score3>90 and score3<100:
                letter3='A'
            elif score3>80 and score3<89:
                letter3='B'
            elif score3>70 and score3<79:
                letter3='C'
            elif score3>60 and score3<69:
                letter3='D'
            else:
                letter3='F'
                if score4>90 and score4<100:
                    letter4='A'
                elif score4>80 and score4<89:
                    letter4='B'
                elif score4>70 and score4<79:
                    letter4='C'
                elif score4>60 and score4<69:
                    letter4='D'
                else:
                    letter4='F'
                    if score5>90 and score5<100:
                        letter5='A'
                    elif score5>80 and score5<89:
                        letter5='B'
                    elif score5>70 and score5<79:
                        letter5='C'
                    elif score5>60 and score5<69:
                        letter5='D'
                    else:
                        letter5='F'
                        if avg>90 and avg<100:
                            letter6='A'
                        elif avg>80 and avg<89:
                            letter6='B'
                        elif avg>70 and avg<79:
                            lette6='C'
                        elif avg>60 and avg<69:
                            letter6='D'
                        else:
                            letter6='F'
                        
    return letter1,letter2,letter3,letter4,letter5,letter6
main()
