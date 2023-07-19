import requests
from bs4 import BeautifulSoup
from loguru import logger


def check_for_errors(url):
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        logger.error("Неправильно введена ссылка! Попробуйте еще раз."
                     " Пример правильно введенной ссылки: https://music.apple.com/us/artist/XXXXXXXX/111111111")
        return
    except requests.exceptions.InvalidSchema:
        logger.error("Произошла ошибка! Попробуйте ввести ссылку еще раз."
                     " Пример правильно введенной ссылки: https://music.apple.com/us/artist/XXXXXXXX/111111111")
        return
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return
    return response


def main():
    link = input("Введите ссылку на профиль исполнителя в сервисе Apple Music: ")
    check = check_for_errors(link)
    if not check:
        return
    amount = 1
    soup = BeautifulSoup(check.text, 'html.parser')
    artist = soup.find('h1', class_='artist-header__name svelte-12wr480').text
    print(f"Топ 10 самых популярных песен {artist} по мнению Apple music:")
    songs = soup.find_all('a', class_='click-action svelte-1nh012k')
    for song in songs[1:11]:
        print(f"{amount}. {song.text}")
        amount += 1


main()
