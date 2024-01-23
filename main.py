from random import randint


class BaseClass:
    def __init__(self):
        self.state = 'start'

    def process(self):
        while self.state is not None:
            if self.state == 'start':
                print('Некоторый запрос создан.')
                self.state = 'analyze'
            elif self.state == 'analyze':
                print('Анализ запроса.')
                if randint(0, 1) == 1:
                    print('Запрос принят в обработку.')
                    self.state = 'processing'
                else:
                    print('Запрос не принят в обработку')
                    self.state = 'clarify'
            elif self.state == 'processing':
                print('Запрос выполнен.')
                self.state = 'close'
            elif self.state == 'clarify':
                if randint(0, 5) == 5:
                    print('Пользователь отозвал запрос.')
                    self.state = 'close'
                else:
                    print('Дополнительная информация получена.')
                    self.state = 'analyze'
            elif self.state == 'close':
                print('')
                self.state = None


if __name__ == "__main__":
    claim_process = BaseClass()
    claim_process.process()