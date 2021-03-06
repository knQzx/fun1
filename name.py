import telebot
bot = telebot.TeleBot('token')

slovar_of_bykvy = {
    'A': '· −',
    'А': '· −',
    '· −': 'А',
    '· −': 'A',

    'B': '− · · ·-',
    'Б': '− · · ·-----',
    '− · · ·-': 'B',
    '− · · ·-----': 'Б',

    'W': '· − −	',
    'В': '· − − · − −',
    '· − −	': 'W',
    '· − − · − −': 'В',

    'G': '− − ·',
    'Г': '− − ·',
    '− − ·': 'G',
    '− − ·': 'Г',

    'D': '− · ·---------',
    'Д': '− · ·',
    '− · ·---------': 'D',
    '− · ·': 'Д',

    'E': '·',
    'Е': '·',
    'Ё': '····',
    '·': 'E',
    '·': 'Е',
    '····': 'Ё',

    'V': '· · · −',
    'Ж': '· · · −-',
    '· · · −-': 'Ж',
    '· · · −': 'V',

    'Z': '− − · ····',
    'З': '− − · ·',
    '− − · ····': 'Z',
    '− − · ·': 'З',

    'I': '· ·------',
    'И': '· ·',
    '· ·': 'И',
    '· ·------': 'I',

    'J': '·− − − −−',
    'Й': '· − − −',
    '·− − − −−': 'J',
    '· − − −': 'Й',


    'K': '− · −--------',
    'К': '− · −',
    '− · −--------': 'K',
    '− · −': 'К',



    'L': '· − ·· ·',
    'Л': '· − · ·',
    '· − ·· ·': 'L',
    '· − · ·': 'Л',


    'M': '− − - - - ·',
    'М': '− −',
    '− − - - - ·': 'M',
    '− −': 'М',

    'N': '··− ·',
    'Н': '− ·',
    '··− ·': 'N',
    '− ·': 'Н',

    'O': '− ··− ·− −',
    'О': '− − −',
    '− ··− ·− −': 'O',
    '− − −': 'О',

    'P': '· − − ·--',
    'П': '· − − ·',
    '· − − ·--': 'P',
    '· − − ·': 'П',

    'R': '· ·− ·',
    'Р': '· − ·',
    '· ·− ·': 'R',
    '· − ·': 'Р',

    'S': '··- · ·',
    'С': '· · ·',
    '··- · ·': 'S',
    '· · ·': 'С',

    'T': '−-',
    'Т': '−',
    '−-': 'T',
    '−': 'Т',

    'U': '· · · −· −',
    'У': '· · −',
    '· · · −· −': 'U',
    '· · −': 'У',

    'F': '· · − · −·',
    'Ф': '· · − ·',
    '· · − ·': 'Ф',
    '· · − · −·': 'F',


    'H': '· -·- · ·',
    'Х': '· · · ·',
    '· · · ·': 'Х',
    '· -·- · ·': 'H',

    'C': '· -·- · · − ·',
    'Ц': '− · − ·',
    '− · − ·': 'Ц',
    '· -·- · · − ·': 'C',


    'Ч': '− − − ·',
    '− − − ·': 'Ч',

    'Ш': '·− − − −·',
    '·− − − −·': 'Ш',

    'Q': '− ·− − · −',
    'Щ': '− − · −',
    '− − · −': 'Щ',
    '− ·− − · −': 'Q',

    'Ъ': '− − · − −',
    '− − · − −': 'Ъ',

    'Y': '· − −− · − −',
    'Ы': '− · − −',
    '· − −− · − −': 'Y',
    '− · − −': 'Ы',

    'Э': '− − ·· −− · −',
    '− − ·· −− · −': 'Э',

    'Ю': '−−− − ·· −− · −',
    '−−− − ·· −− · −': 'Ю',

    'Я': '−−− − ··  − −− · −',
    '−−− − ··  − −− · −': 'Я',


    'X': '− ·  · −· −',
    'Ь': '− · · −',
    '− ·  · −· −': 'X',
    '− · · −': 'Ь',

    '.': '· · · · · ·',
    '· · · · · ·': '.',

    ',': '· − · − · −',
    '· − · − · −': ',',

    ':': '− − − · · ·',
    '− − − · · ·': ':',

    ';': '− · − · − ·',
    '− · − · − ·': ';',

    '(': '− · − − · −',
    ')': '− · − − · − - ',
    '− · − − · −': '(',
    '− · − − · − - ': ')',

    "'": '· − − − − ·',
    '· − − − − ·': "'",

    '"': '· − − − − ·',
    '· − − − − ·': '"',

    '-': '− · · · · −',
    '− · · · · −': '-',

    '/': '− · · − ·',
    '− · · − ·': '/',

    '_': '· · − − · −',
    '· · − − · −': '_',

    '?': '· · − − · ·',
    '· · − − · ·': '?',

    '!': '− − · · − −',
    '− − · · − −': '!',

    '+': '· − · − ·',
    '· − · − ·': '+',

    ' ': '− · · · −',
    '− · · · −': ' ',

    '@': '· − − · − ·',
    '· − − · − ·': '@'
}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, напиши 'кодировка' или 'раскодировка' ")
    elif message.text == "кодировка":
        bot.send_message(message.from_user.id, 'Вводи свой текст для кодировки')
        bot.register_next_step_handler(message, get_kodirovka)
    elif message.text == "раскодировка":
        bot.send_message(message.from_user.id, 'Вводи свой текст для раскодировки')
        bot.register_next_step_handler(message, get_raskodirovka)
    else:
        bot.send_message(message.from_user.id, 'Вас приветствует бот созданный Денисом и Кириллом\nВвод вы можете писать любым регистром\nВывод печатается только нижним регистром\nНапишите Привет чтобы продолжить')

def get_kodirovka(message):
    global sp
    name = message.text
    sp = []
    for el in name.upper():
        if el in slovar_of_bykvy:
            sp.append(f'{slovar_of_bykvy[el]}|')
    string = ''.join(sp)
    bot.send_message(message.from_user.id, string)
    sp = []

sp = []

def get_raskodirovka(message):
    global sp
    d = (message.text).split('|')
    for el in d:
        if el in slovar_of_bykvy:
            sp.append(slovar_of_bykvy[el])
    myString = ''.join(sp)
    jjj = myString.lower()
    bot.send_message(message.from_user.id, f"{jjj}")
    sp = []








bot.polling(none_stop=True, interval=0)
