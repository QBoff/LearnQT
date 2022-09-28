import re
import string

number = input()


class formatException(Exception):
    pass


class wrongCountryCode(Exception):
    pass


class longNumberException(Exception):
    pass


class wrongOperatorCode(Exception):
    pass


try:
    def check_country_code(number: str):
        res = re.findall(r'^(\+7|8|\+359|\+55|\+1)', number)
        if not res:
            raise wrongCountryCode
        return res

    def checkStart(number: str):
        res = re.findall(
            r'^(\+7|8|\+359|\+55|\+1)\(?(\d{3})\)?\d{3}-?\d{4}$', number)
        if not res:
            raise formatException
        return res

    def bracketCheck(number: str):
        if number.count('(') == number.count(')') == 1 and number.find('(') < number.find(')')\
                or number.count('(') == number.count(')') == 0:
            return True
        # print("1213456ui")
        raise formatException

    def minusCheck(number: str):
        if '-' in number and "--" not in number and number[-1] != '-' or '-' not in number:
            return True
        raise formatException

    def checkWord(number: str):
        for w in string.ascii_letters:
            if w in number:
                raise formatException

        return True

    def main():
        global number
        number = number.replace(' ', '').replace("\t", "").replace("\n", "")
        # number = number.replace('(', '').replace(')', '').replace('-', '')
        # print(number)
        if all([checkStart(number), check_country_code(number), bracketCheck(number),
                minusCheck(number), checkWord(number)]):
            number = number.replace('(', '').replace(')', '').replace('-', '')
            number = number.replace('+', '')
            if len(number) != 11:
                raise longNumberException
                # quit()
            if "7" == number[0]:
                number = '+' + number
            elif "8" == number[0]:
                number = '+7' + number[1::]
            # print(number[2:5])

            if int(number[2:5]) not in range(910, 919 + 1) and int(number[2:5]) not in range(980, 989 + 1) \
                    and int(number[2:5]) not in range(920, 939 + 1) and int(number[2:5]) not in range(902, 906 + 1) \
                    and int(number[2:5]) not in range(960, 969 + 1):
                raise wrongOperatorCode

            print(number)
        else:
            raise formatException

    if __name__ == '__main__':
        main()

except formatException:
    print("неверный формат")
except longNumberException:
    print("неверное количество цифр")
except wrongOperatorCode:
    print("не определяется оператор сотовой связи")
except wrongCountryCode:
    print("не определяется код страны")
