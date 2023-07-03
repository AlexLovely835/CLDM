import re, random, argparse

def rollDice(dice_string, mod=0):
    dice_pattern = re.compile("\d*d\d*")
    if dice_pattern.match(dice_string):
        dice_roll = dice_string.split('d')
        num_of_dice = int(dice_roll[0])
        dice = int(dice_roll[1])
        if num_of_dice > 0 and dice > 1:
            result = 0
            for _ in range(num_of_dice):
                result += random.randint(1, dice)
            return result + mod
        else:
            raise ValueError("Cannot roll invalid dice string: dice strings must be in format such as 1d6 or 2d12.")
    else:
        raise ValueError("Cannot roll invalid dice string: dice strings must be in format such as 1d6 or 2d12.")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dice_string', type=str, help='Select dice string. i.e. 1d6')
    parser.add_argument('-m', dest='mod', type=int, help='Add a modifier to the dice roll.')
    args = parser.parse_args()
    print(rollDice(args.dice_string, args.mod))