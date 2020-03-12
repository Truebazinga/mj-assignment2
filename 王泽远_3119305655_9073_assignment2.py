import pytest
def texas_poker_process(all_card):
    White_card=[]
    Black_card=[]
    White_card_number=[]
    Black_card_number=[]
    White_card_flower=[]
    Black_card_flower=[]
    for i in range(7,12):
        White_card.append(all_card.split()[i])
        White_card_number.append(White_card[i-7][0])
        White_card_flower.append(White_card[i-7][1])
        if White_card_number[i-7]=='T':
            White_card_number[i-7]=10
        if White_card_number[i-7]=='J':
            White_card_number[i-7]=11
        if White_card_number[i-7]=='Q':
            White_card_number[i-7]=12
        if White_card_number[i-7]=='K':
            White_card_number[i-7]=13
        if White_card_number[i-7]=='A':
            White_card_number[i-7]=14
    for i in range(0,5):
        White_card_number[i]=int(White_card_number[i])
    White_card_number.sort(reverse=True)
    #return(White_card)
    for i in range (1,6):
        Black_card.append(all_card.split()[i])
        Black_card_number.append(Black_card[i-1][0])
        Black_card_flower.append(Black_card[i-1][1])
        if Black_card_number[i-1]=='T':
            Black_card_number[i-1]=10
        if Black_card_number[i-1]=='J':
            Black_card_number[i-1]=11
        if Black_card_number[i-1]=='Q':
            Black_card_number[i-1]=12
        if Black_card_number[i-1]=='K':
            Black_card_number[i-1]=13
        if Black_card_number[i-1]=='A':
            Black_card_number[i-1]=14
    for i in range(0,5):
        Black_card_number[i]=int(Black_card_number[i])
    Black_card_number.sort(reverse=True)
    #print(Black_card_number)
    return White_card_number,Black_card_number,White_card_flower,Black_card_flower

#print(texas_poker_process('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH'))


def pocker_category(card_number,card_flower):
    case_flower=(card_flower[0]==card_flower[1]==card_flower[2]==card_flower[3]==card_flower[4])
    case_shun=(card_number[0]==card_number[1]+1 and card_number[1]==card_number[2]+1 and card_number[2]==card_number[3]+1 and card_number[3]==card_number[4]+1 )
    case_same2=(card_number[0]==card_number[1] or card_number[1]==card_number[2] or card_number[2]==card_number[3] or card_number[3]==card_number[4])
    case_same2x2=((card_number[0]==card_number[1] or card_number[1]==card_number[2]) and (card_number[2]==card_number[3] or card_number[3]==card_number[4]))
    case_same3=((card_number[0]==card_number[1]==card_number[2]) or (card_number[1]==card_number[2]==card_number[3]) or (card_number[2]==card_number[3]==card_number[4]))
    case_same4=((card_number[0]==card_number[1]==card_number[2]==card_number[3]) or (card_number[1]==card_number[2]==card_number[3]==card_number[4]))
    case3and2=((card_number[0]==card_number[1] and card_number[2]==card_number[3]==card_number[4]) or (card_number[0]==card_number[1]==card_number[2] and card_number[3]==card_number[4]))
    #print(card_number[0])
    #print(card_number[4])
    #print(card_number[2])
    #print(case_shun)
    #print(case_flower)
    if (case_shun and case_flower):
        category=9 #同花顺
        category_name = 'Straight flush '
    elif (case_same4):
        category=8 #铁支
        category_name = 'Four of a kind '
    elif (case3and2):#葫芦
        category=7
        category_name = 'Full House '

    elif (case_flower):
        category=6 
        category_name = 'Flush '
    elif (case_shun):
        category=5
        category_name = 'Straight '
    elif (case_same3):
        category=4
        category_name= 'Three of a Kind '
    elif(case_same2 and case_same2x2):
        category=3
        category_name = 'Two Pairs '
    elif(case_same2):
        category=2
        category_name = 'Pair'

    else:
        category=1
        category_name = 'High Card '
    return category,category_name

#print(texas_poker_process('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S'))
#White_card_number,Black_card_number,White_card_flower,Black_card_flower=texas_poker_process('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S')
#White_category=pocker_category(White_card_number,White_card_flower)
#print(White_category)
def compare_category(White_card_number,Black_card_number,White_card_flower,Black_card_flower):
    White_category,White_category_name=pocker_category(White_card_number,White_card_flower)
    Black_category,Black_category_name=pocker_category(Black_card_number,Black_card_flower)
    if (White_category > Black_category):
        return("White wins")
    elif (Black_category > White_category):
        return("Black wins")
    elif (White_category==Black_category):
        if (White_category==9):
            if (White_card_number[0]>Black_card_number[0]):
                return("White wins")
            if (White_card_number[0]==Black_card_number[0]):
                return("Tie")
            if (White_card_number[0]<Black_card_number[0]):
                return("Black wins")
        elif (White_category==8):
            if (White_card_number[0]==White_card_number[1]):
                White_same4_index=0
            elif (White_card_number[0]!=White_card_number[1]):
                White_same4_index=1
            if (Black_card_number[0]==Black_card_number[1]):
                Black_same4_index=0
            elif (Black_card_number[0]!=Black_card_number[1]):
                Black_same4_index=1
            if (White_card_number[White_same4_index]>Black_card_number[Black_same4_index]):
                return("White wins")
            else :
                return("Black wins")
        elif (White_category==7):
            if(White_card_number[0]==White_card_number[1]==White_card_number[2]):
                White_same3and2_index=0
            elif (White_card_number[1]==White_card_number[2]==White_card_number[3]):
                White_same3and2_index=1
            else :
                White_same3and2_index=2
            if(Black_card_number[0]==Black_card_number[1]==Black_card_number[2]):
                Black_same3and2_index=0
            elif (Black_card_number[1]==Black_card_number[2]==Black_card_number[3]):
                Black_same3and2_index=1
            else :
                Black_same3and2_index=2
            if (White_card_number[White_same3and2_index]>Black_card_number[Black_same3and2_index]):
                return("White wins")
            else :
                return("Black wins")
        elif (White_category==6):
            for i in range(len(White_card_number)):
                if(White_card_number[i]>Black_card_number[i]):
                    return("White wins")
                    break
                elif(White_card_number[i]<Black_card_number[i]):
                    return("Black wins")
                    break
                elif (White_card_number[0]==Black_card_number[0]):
                    return("Tie")
        elif (White_category==5):
            if (White_card_number[0]>Black_card_number[0]):
                return("White wins")
            if (White_card_number[0]==Black_card_number[0]):
                return("Tie")
            if (White_card_number[0]<Black_card_number[0]):
                return("Black wins")
        elif (White_category==4):
            if(White_card_number[0]==White_card_number[1]==White_card_number[2]):
                White_same3_index=0
            elif (White_card_number[1]==White_card_number[2]==White_card_number[3]):
                White_same3_index=1
            else :
                White_same3_index=2
            if(Black_card_number[0]==Black_card_number[1]==Black_card_number[2]):
                Black_same3_index=0
            elif (Black_card_number[1]==Black_card_number[2]==Black_card_number[3]):
                Black_same3_index=1
            else :
                Black_same3_index=2
            if (White_card_number[White_same3_index]>Black_card_number[Black_same3_index]):
                return("White wins")
            else :
                return("Black wins")
        elif (White_category==3):
            White_2x2_number=[]
            White_2x2_number.append(White_card_number[1])
            White_2x2_number.append(White_card_number[3])
            if (White_card_number[1]==White_card_number[2]):
                White_2x2_number.append(White_card_number[0])
            elif (White_card_number[2]==White_card_number[3]):
                White_2x2_number.append(White_card_number[4])
            else:
                White_2x2_number.append(White_card_number[2])


            Black_2x2_number=[]
            Black_2x2_number.append(Black_card_number[1])
            Black_2x2_number.append(Black_card_number[3])
            if (Black_card_number[1]==Black_card_number[2]):
                Black_2x2_number.append(Black_card_number[0])
            elif (Black_card_number[2]==Black_card_number[3]):
                Black_2x2_number.append(Black_card_number[4])
            else:
                Black_2x2_number.append(Black_card_number[2])

            for i in range(len(White_2x2_number)):
                if(White_2x2_number[i]>Black_2x2_number[i]):
                    return("White wins")
                    break
                elif (White_2x2_number[i]<Black_2x2_number[i]):
                    return("Black wins")
                    break
                elif (i==4 and White_2x2_number[i]==Black_2x2_number[i]):
                    return("Tie")


        elif (White_category==2):
            White_same2_number=[]
            if(White_card_number[0]==White_card_number[1]):
                White_same2_number.append(White_card_number[0])
                White_same2_number.append(White_card_number[2])
                White_same2_number.append(White_card_number[3])
                White_same2_number.append(White_card_number[4])
            elif (White_card_number[1]==White_card_number[2]):
                White_same2_number.append(White_card_number[1])
                White_same2_number.append(White_card_number[0])
                White_same2_number.append(White_card_number[3])
                White_same2_number.append(White_card_number[4])
            elif (White_card_number[2]==White_card_number[3]):
                White_same2_number.append(White_card_number[2])
                White_same2_number.append(White_card_number[0])
                White_same2_number.append(White_card_number[1])
                White_same2_number.append(White_card_number[4])
            elif (White_card_number[3]==White_card_number[4]):
                White_same2_number.append(White_card_number[3])
                White_same2_number.append(White_card_number[0])
                White_same2_number.append(White_card_number[1])
                White_same2_number.append(White_card_number[2])

            Black_same2_number=[]
            if(Black_card_number[0]==Black_card_number[1]):
                Black_same2_number.append(Black_card_number[0])
                Black_same2_number.append(Black_card_number[2])
                Black_same2_number.append(Black_card_number[3])
                Black_same2_number.append(Black_card_number[4])
            elif (Black_card_number[1]==Black_card_number[2]):
                Black_same2_number.append(Black_card_number[1])
                Black_same2_number.append(Black_card_number[0])
                Black_same2_number.append(Black_card_number[3])
                Black_same2_number.append(Black_card_number[4])
            elif (Black_card_number[2]==Black_card_number[3]):
                Black_same2_number.append(Black_card_number[2])
                Black_same2_number.append(Black_card_number[0])
                Black_same2_number.append(Black_card_number[1])
                Black_same2_number.append(Black_card_number[4])
            elif (Black_card_number[3]==Black_card_number[4]):
                Black_same2_number.append(Black_card_number[3])
                Black_same2_number.append(Black_card_number[0])
                Black_same2_number.append(Black_card_number[1])
                Black_same2_number.append(Black_card_number[2])

            for i in range(len(Black_same2_number)):
                if(White_same2_number[i]>Black_same2_number[i]):
                    return("White wins")
                    break
                elif (White_same2_number[i]<Black_same2_number[i]):
                    return("Black wins")
                    break
                elif (White_same2_number[4]==Black_same2_number[4]):
                    return("Tie")

        elif(White_category==1):
            for i in range(len(White_card_number)):
                if(White_card_number[i]>Black_card_number[i]):
                    return("White wins")
                    break
                elif (White_card_number[i]<Black_card_number[i]):
                    return("Black wins")
                    break
                elif (i==4 and White_card_number[i]==Black_card_number[i]):
                    return("Tie")


#White_card_number,Black_card_number,White_card_flower,Black_card_flower=texas_poker_process('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH')
#return(White_card_number)
#print(compare_category(White_card_number,Black_card_number,White_card_flower,Black_card_flower))

def pocker_result(all_card):
    White_card_number,Black_card_number,White_card_flower,Black_card_flower=texas_poker_process(all_card)
    result=compare_category(White_card_number,Black_card_number,White_card_flower,Black_card_flower)
    return(result)

def test_san():
    assert pocker_result('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH') == 'White wins'

def test_full_house():
    assert pocker_result('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S') == 'Black wins'

def test_san2():
    assert pocker_result('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH') == 'Black wins'

def test_tie():
    assert pocker_result('Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH') == 'Tie'

def test_2and2():
    assert pocker_result('Black: 2H 2D 3H 3D 5H White: 3D 3S 4C 5S 4H') == 'White wins'

def test_sfandshun():
    assert pocker_result('Black: 4H 5H 6H 7H 8H White: 8C 9S TC JD QS') == 'Black wins'

def test_sfandth():
    assert pocker_result('Black: 8C 9C TC JC AC White: 4H 5H 6H 7H 8H') == 'White wins'

def test_2pair():
    assert pocker_result('Black: 8C 9C TC 8H 9H White: 9S 9D 8S 7H 8D') == 'Black wins'
if __name__ == '__main__':
    pytest.main(['D:\\practise\\mjweb\\Texas-Hold-em-Poker_test.py'])

