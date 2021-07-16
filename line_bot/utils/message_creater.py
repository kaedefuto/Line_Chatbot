def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    if message == '今日の天気は':
        message = '雨に決まってるだろうが'
    if message == 'こんにちは':
        message = 'こんちはー'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message