import os
import requests
import time
from colorama import Fore, init

init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_art():
    art = f"""
{Fore.GREEN}
  _   _ ____             ___      _       _   
| | | / ___|           / _ \ ___(_)_ __ | |_ 
| | | \___ \   _____  | | | / __| | '_ \| __|
| |_| |___) | |_____| | |_| \__ \ | | | | |_ 
 \___/|____/           \___/|___/_|_| |_|\__|        
{Fore.RESET}
    """
    print(art)
    print(f"{Fore.YELLOW}╔{'═' * 30}╗")
    print(f"║ {'1. Поиск по нику':<28} ║")
    print(f"║ {'2. Выход':<28} ║")
    print(f"╚{'═' * 30}╝{Fore.RESET}")

def check_username(nick):
    sites = {
        "VK": f"https://vk.com/{nick}",
        "Facebook": f"https://facebook.com/{nick}",
        "Instagram": f"https://instagram.com/{nick}",
        "Twitter/X": f"https://x.com/{nick}",
        "TikTok": f"https://tiktok.com/@{nick}",
        "Snapchat": f"https://snapchat.com/add/{nick}",
        "Threads": f"https://threads.net/@{nick}",
        "Telegram": f"https://t.me/{nick}",
        "Discord": f"https://discord.com/users/{nick}",
        "Steam": f"https://steamcommunity.com/id/{nick}",
        "Twitch": f"https://twitch.tv/{nick}",
        "Epic Games": f"https://epicgames.com/account/personal?username={nick}",
        "GitHub": f"https://github.com/{nick}",
        "GitLab": f"https://gitlab.com/{nick}",
        "Stack Overflow": f"https://stackoverflow.com/users/{nick}",
        "Dev.to": f"https://dev.to/{nick}",
        "Reddit": f"https://reddit.com/u/{nick}",
        "Pinterest": f"https://pinterest.com/{nick}",
        "Tumblr": f"https://{nick}.tumblr.com",
        "Medium": f"https://medium.com/@{nick}",
        "Quora": f"https://quora.com/profile/{nick}",
        "YouTube": f"https://youtube.com/@{nick}",
        "SoundCloud": f"https://soundcloud.com/{nick}",
        "Spotify": f"https://open.spotify.com/user/{nick}",
        "Last.fm": f"https://last.fm/user/{nick}",
        "Patreon": f"https://patreon.com/{nick}",
        "Flickr": f"https://flickr.com/people/{nick}",
        "DeviantArt": f"https://{nick}.deviantart.com",
        "Wikipedia": f"https://wikipedia.org/wiki/User:{nick}",
        "Keybase": f"https://keybase.io/{nick}"
    }

    print(f"\n{Fore.YELLOW}🔍 Поиск аккаунтов для: {nick}{Fore.RESET}\n")

    found = 0
    total = len(sites)
    
    for name, url in sites.items():
        try:
            response = requests.get(url, timeout=5, allow_redirects=False)
            if (response.status_code == 200 and 
                not any(e in response.url.lower() for e in ["error", "404"])):
                print(f"{Fore.GREEN}[+] {name}: {url}{Fore.RESET}")
                found += 1
            else:
                print(f"{Fore.RED}[-] {name}: Не найдено{Fore.RESET}")
        except:
            print(f"{Fore.RED}[-] {name}: Ошибка проверки{Fore.RESET}")
    
    print(f"\n{Fore.YELLOW} Результаты:{Fore.RESET}")
    print(f"{Fore.GREEN} Найдено: {found} аккаунтов{Fore.RESET}")
    print(f"{Fore.RED} Не найдено: {total - found} аккаунтов{Fore.RESET}")
    print(f"\n{Fore.CYAN} Пояснение:{Fore.RESET}")
    print(f"{Fore.GREEN}Зелёный - аккаунт существует{Fore.RESET}")
    print(f"{Fore.RED}Красный - аккаунт не найден{Fore.RESET}")

def main():
    try:
        import requests
    except ImportError:
        print(f"{Fore.RED}[!] Устанавливаем requests...{Fore.RESET}")
        os.system("pip install requests")
        clear()

    while True:
        clear()
        print_art()
        choice = input("\nВыберите действие: ")

        if choice == "1":
            nick = input("Введите ник: ").strip()
            if nick:
                check_username(nick)
                input("\nНажмите Enter чтобы продолжить...")
            else:
                print(f"{Fore.RED} Ник не может быть пустым!{Fore.RESET}")
                time.sleep(1)
        elif choice == "2":
            print(f"{Fore.RED}Выход...{Fore.RESET}")
            break
        else:
            print(f"{Fore.RED} Неверный выбор!{Fore.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
