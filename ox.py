import colorama
from colorama import Fore, Back, Style
import secrets
import sys

class Oxgame(object):

    def __init__(self):
        self.alphabet = 'ox'
        self.total_count = 0
        self.guess_right = 0

    def print_logo(self):
        logo = """
    ===============================
    =                             =
    =           OX GAME           =
    =                             =
    ===============================
        """
        bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color not in bad_colors]
        colored_chars = [secrets.choice(colors) + char for char in logo]
        print(''.join(colored_chars))

    def run(self):
        try:
            colorama.init()
            self.print_logo()
            print(Fore.GREEN)

            while (True):
                input_str = input("O와 X중 한글자를 입력하세요 : ")
                self.total_count += 1
                answer = secrets.choice(self.alphabet)
                if input_str.lower() == answer: #정답
                    self.guess_right += 1
                    print("정답입니다!")
                else: #오답
                    print(f"오답입니다! 정답은 {answer.upper()} 입니다.")
                print(f"점수 : {self.guess_right}/{self.total_count} ({round(self.guess_right/self.total_count*100, 1)}%)")
                print('')

        except KeyboardInterrupt:
            sys.exit(1)

def main():
    ox = Oxgame()
    ox.run()

if __name__ == '__main__':
    main()