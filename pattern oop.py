from random import randint


class BaseClass:
    def __init__(self):
        self.state = 'start'

    def start(self):
        print('Некоторый запрос создан.')
        self.state = 'analyze'

    def analyze(self):
        print('Анализ запроса...')
        if randint(0, 1) == 1:
            print('Запрос принят в обработку.')
            self.state = 'processing'
        else:
            print('Запрос не принят в обработку.')
            self.state = 'clarify'

    def processing(self):
        print('Запрос выполнен.')
        self.state = 'close'

    def clarify(self):
        if randint(0, 5) == 5:
            print('Пользователь отозвал запрос.')
            self.state = 'close'
        else:
            print('Дополнительная информация получена.')
            self.state = 'analyze'

    def close(self):
        print('')
        self.state = None

    def run(self):
        while self.state is not None:
            if self.state == 'start':
                self.start()
            elif self.state == 'analyze':
                self.analyze()
            elif self.state == 'processing':
                self.processing()
            elif self.state == 'clarify':
                self.clarify()
            elif self.state == 'close':
                self.close()


if __name__ == "__main__":
    claim = BaseClass()
    claim.run()