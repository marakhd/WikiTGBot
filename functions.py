#Импортируем фреймворк Wikipedia
import wikipedia

#Фцнкция получения данных
async def process_query(query: str) -> str:
    try:
        wikipedia.set_lang("ru")  # Установить язык для поиска на Wikipedia

        page = wikipedia.page(query)
        summary = page.summary

        # Ограничиваем длину ответа до 3950 символов и убираем лишние пробелы
        summary = ' '.join(summary[:3950].rsplit(' ', 1))

        # Находим индекс последней точки для сокращения текста
        index = summary.rfind('.')
        if index != -1:
            summary = summary[:index+1]

        return (f"\t{summary}"
                f'\n\nБольше деталей на <a href="{page.url}">Wikipedia</a>')
    except wikipedia.exceptions.PageError:
        return (f"Такой страницы нет на Wikipedia. "
                f'\nВы можете поискать в <a href="https://www.google.com/search?q={query.replace(" ", "+")}">Google</a>'
                f'\nИли в <a href="https://yandex.ru/search/?text={query.replace(" ", "+")}">Яндекс</a>')