import argparse

def main():
    parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('--verbose', action='store_true',
help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1,
help='Количество повторений строки')
    args = parser.parse_args()
    if args.verbose:
        print(f'Полученные аргументы: number={args.number},text="{args.text}", repeat={args.repeat}')
    
    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')
if __name__ == '__main__':
    main()