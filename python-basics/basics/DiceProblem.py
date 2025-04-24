def opposite_face_of_dice(n):
    match n:
        case 1:
            return 6
        case 2:
            return 5
        case 3:
            return 4
        case 4:
            return 3
        case 5:
            return 2
        case 6:
            return 1


def opposite_face_of_dice_2(n):
    # sum of any two opposite sides = 7 , 1+6 = 7
    return 7 - n


if __name__ == '__main__':
    print(opposite_face_of_dice(1))
    print(opposite_face_of_dice_2(4))
