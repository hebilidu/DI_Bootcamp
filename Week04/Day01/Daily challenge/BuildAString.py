# Week04 Day01 - Daily Challenge - Build up a string
# Created on  : 210425 by : lidu
# Modified on : 210425 by : lidu

def main():
    answer = input('Please enter a 10 character long string : ')
    answer_length = len(answer)
    if answer_length < 10:
        print('String is too short')
    elif answer_length > 10:
        print('String is too long')

    out_txt = 'The first character is "{}" and the last one is "{}"'.format(answer[0],answer[-1])
    print(out_txt)

if __name__ == "__main__":
    main()