from random import randint


def start(claim):
    print('Некоторый запрос создан.')
    claim['state'] = 'analyze'


def analyze(claim):
    print('Анализ запроса.')
    if randint(0, 1) == 1:
        print('Запрос принят в обработку.')
        claim['state'] = 'processing'
    else:
        print('Запрос не принят в обработку')
        claim['state'] = 'clarify'


def processing(claim):
    print('Запрос выполнен.')
    claim['state'] = 'close'


def clarify(claim):
    if randint(0, 5) == 5:
        print('Пользователь отозвал запрос.')
        claim['state'] = 'close'
    else:
        print('Дополнительная информация получена.')
        claim['state'] = 'analyze'


def close(claim):
    print('')
    claim['state'] = None


state_functions = {
    'start': start,
    'analyze': analyze,
    'processing': processing,
    'clarify': clarify,
    'close': close
}


def run_claim():
    claim = {'state': 'start'}
    while claim['state'] is not None:
        current_state_function = state_functions[claim['state']]
        current_state_function(claim)


if __name__ == "__main__":
    run_claim()