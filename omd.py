"""Duck story"""


def step2_umbrella() -> None:
    """
    Print case duck with umbrella
    :return: None
    """
    print(
        'Утка-маляр 🦆 зонтик ☂️взяла.\n'
        'И прямо на нем по реке поплыла.'
    )


def step2_no_umbrella() -> None:
    """
    Print case duck without umbrella
    :return: None
    """
    print(
        'Утка-маляр 🦆 зонт ☂️ не взяла.\n'
        'Она ведь утка, ее перья не дают ей промокнуть.'
    )


def step1() -> None:
    """
    Print first question about duck
    :return: None
    """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
