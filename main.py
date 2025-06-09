import os
import subprocess
import sys
import time
import logging


logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def install_library(library):
    
    try:
        __import__(library)
        print(f"[+] {library} True")
    except ImportError:
        print(f"[!] Устанавливаем {library}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"[+] {library} успешно установлен")
        except subprocess.CalledProcessError as e:
            print(f"[!] Ошибка установки {library}: {str(e)}")
            print(f"Установите вручную: pip install {library}")
            input("Нажмите Enter для выхода...")
            sys.exit(1)


for lib in ["colorama", "requests"]:
    install_library(lib)

from colorama import Fore, init
import requests


init(autoreset=True)

def clear():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def print_art():
    
    art = f"""
{Fore.GREEN}
  /$$$$$$  /$$                           /$$                        
 /$$__  $$| $$                          | $$                        
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$                  
| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/                  
| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/                   
| $$    $$| $$  | $$| $$_____/| $$      | $$_  $$                   
|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$                  
 \______/ |__/  |__/ \_______/ \_______/|__/  \__/                  
                                                                    
                                                                    
                                                                    
 /$$                 /$$                     /$$                    
| $$                | $$                    |__/                    
| $$$$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$  /$$  /$$$$$$  /$$$$$$$ 
| $$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$| $$ /$$__  $$| $$__  $$
| $$  \ $$| $$  | $$| $$| $$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$| $$| $$_____/| $$  | $$| $$| $$  | $$| $$  | $$
| $$$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/| $$  | $$
|_______/  \____  $$|__/ \_______/ \____  $$|__/ \______/ |__/  |__/
           /$$  | $$               /$$  \ $$                        
          |  $$$$$$/              |  $$$$$$/                        
           \______/                \______/                                    
{Fore.RESET}
    """
    print(art)
    print(f"{Fore.YELLOW}╔{'═' * 30}╗")
    print(f"║ {'1. Поиск по нику':<28} ║")
    print(f"║ {'2. Выход':<28} ║")
    print(f"╚{'═' * 30}╝{Fore.RESET}")

def check_username(nick):
    
    sites = {
    "VK": "https://vk.com/{nick}",
    "Facebook": "https://facebook.com/{nick}",
    "Instagram": "https://instagram.com/{nick}",
    "Twitter/X": "https://x.com/{nick}",
    "TikTok": "https://tiktok.com/@{nick}",
    "Snapchat": "https://snapchat.com/add/{nick}",
    "Threads": "https://threads.net/@{nick}",
    "Telegram": "https://t.me/{nick}",
    "Discord": "https://discord.com/users/{nick}",
    "Steam": "https://steamcommunity.com/id/{nick}",
    "Twitch": "https://twitch.tv/{nick}",
    "Epic Games": "https://epicgames.com/account/personal?username={nick}",
    "GitHub": "https://github.com/{nick}",
    "GitLab": "https://gitlab.com/{nick}",
    "Stack Overflow": "https://stackoverflow.com/users/{nick}",
    "Dev.to": "https://dev.to/{nick}",
    "Reddit": "https://reddit.com/u/{nick}",
    "Pinterest": "https://pinterest.com/{nick}",
    "Tumblr": "https://{nick}.tumblr.com",
    "Medium": "https://medium.com/@{nick}",
    "Quora": "https://quora.com/profile/{nick}",
    "YouTube": "https://youtube.com/@{nick}",
    "SoundCloud": "https://soundcloud.com/{nick}",
    "Spotify": "https://open.spotify.com/user/{nick}",
    "Last.fm": "https://last.fm/user/{nick}",
    "Patreon": "https://patreon.com/{nick}",
    "Flickr": "https://flickr.com/people/{nick}",
    "DeviantArt": "https://{nick}.deviantart.com",
    "Wikipedia": "https://wikipedia.org/wiki/User:{nick}",
    "Keybase": "https://keybase.io/{nick}",
    "LinkedIn": "https://linkedin.com/in/{nick}",
    "Behance": "https://behance.net/{nick}",
    "Dribbble": "https://dribbble.com/{nick}",
    "Vimeo": "https://vimeo.com/{nick}",
    "Mixcloud": "https://mixcloud.com/{nick}",
    "Goodreads": "https://goodreads.com/{nick}",
    "Bandcamp": "https://bandcamp.com/{nick}",
    "Etsy": "https://etsy.com/shop/{nick}",
    "ArtStation": "https://artstation.com/{nick}",
    "CodePen": "https://codepen.io/{nick}",
    "HackerRank": "https://hackerrank.com/{nick}",
    "LeetCode": "https://leetcode.com/{nick}",
    "Bitbucket": "https://bitbucket.org/{nick}",
    "Dailymotion": "https://dailymotion.com/{nick}",
    "Strava": "https://strava.com/athletes/{nick}",
    "Fiverr": "https://fiverr.com/{nick}",
    "Upwork": "https://upwork.com/freelancers/{nick}",
    "Trello": "https://trello.com/{nick}",
    "BeReal": "https://bereal.com/{nick}",
    "Letterboxd": "https://letterboxd.com/{nick}",
    "Mastodon": "https://mastodon.social/@{nick}",
    "Bluesky": "https://bsky.app/profile/{nick}",
    "Clubhouse": "https://clubhouse.com/@{nick}",
    "ReverbNation": "https://reverbnation.com/{nick}",
    "Smule": "https://smule.com/{nick}",
    "Wattpad": "https://wattpad.com/user/{nick}",
    "Couchsurfing": "https://couchsurfing.com/people/{nick}",
    "Myspace": "https://myspace.com/{nick}",
    "500px": "https://500px.com/{nick}",
    "VSCO": "https://vsco.co/{nick}",
    "Ello": "https://ello.co/{nick}",
    "ProductHunt": "https://producthunt.com/@{nick}",
    "AngelList": "https://angel.co/u/{nick}",
    "WeHeartIt": "https://weheartit.com/{nick}",
    "Mix": "https://mix.com/{nick}",
    "Houzz": "https://houzz.com/user/{nick}",
    "Meetup": "https://meetup.com/members/{nick}",
    "Codewars": "https://codewars.com/users/{nick}",
    "Kaggle": "https://kaggle.com/{nick}",
    "Instructables": "https://instructables.com/member/{nick}",
    "Hackaday": "https://hackaday.io/{nick}",
    "Dtube": "https://d.tube/#!/c/{nick}",
    "Lichess": "https://lichess.org/@/{nick}",
    "Chess.com": "https://chess.com/member/{nick}",
    "Tripadvisor": "https://tripadvisor.com/members/{nick}",
    "Badoo": "https://badoo.com/profile/{nick}",
    "OkCupid": "https://okcupid.com/profile/{nick}",
    "Duolingo": "https://duolingo.com/profile/{nick}",
    "Imgur": "https://imgur.com/user/{nick}",
    "Periscope": "https://pscp.tv/{nick}",
    "Odnoklassniki": "https://ok.ru/{nick}",
    "Weibo": "https://weibo.com/{nick}",
    "QQ": "https://user.qzone.qq.com/{nick}",
    "Taringa": "https://taringa.net/{nick}",
    "Viadeo": "https://viadeo.com/profile/{nick}",
    "Xing": "https://xing.com/profile/{nick}",
    "Ravelry": "https://ravelry.com/people/{nick}",
    "Untappd": "https://untappd.com/user/{nick}",
    "Substack": "https://{nick}.substack.com",
    "Ko-fi": "https://ko-fi.com/{nick}",
    "OnlyFans": "https://onlyfans.com/{nick}",
    "Carbonmade": "https://{nick}.carbonmade.com",
    "Contently": "https://contently.com/{nick}",
    "Hackerearth": "https://hackerearth.com/@{nick}",
    "Topcoder": "https://topcoder.com/members/{nick}",
    "Freelancer": "https://freelancer.com/u/{nick}",
    "Minds": "https://minds.com/{nick}",
    "Gab": "https://gab.com/{nick}",
    "Parler": "https://parler.com/{nick}",
    "Amino": "https://aminoapps.com/u/{nick}",
    "KakaoTalk": "https://kakaotalk.com/@{nick}",
    "Line": "https://line.me/ti/p/~{nick}",
    "Douban": "https://douban.com/people/{nick}",
    "Renren": "https://renren.com/profile/{nick}",
    "WeChat": "https://wechat.com/{nick}",
    "Bilibili": "https://space.bilibili.com/{nick}",
    "Youku": "https://i.youku.com/{nick}",
    "Zhihu": "https://zhihu.com/people/{nick}",
    "Battle.net": "https://battle.net/profile/{nick}",
    "Roblox": "https://roblox.com/users/{nick}/profile",
    "Origin": "https://origin.com/profile/{nick}",
    "Itch.io": "https://{nick}.itch.io",
    "GameJolt": "https://gamejolt.com/@{nick}",
    "Newgrounds": "https://{nick}.newgrounds.com",
    "Kongregate": "https://kongregate.com/accounts/{nick}",
    "ArmorGames": "https://armorgames.com/user/{nick}",
    "Miniclip": "https://miniclip.com/user/{nick}",
    "Xbox": "https://xbox.com/en-US/profiles/{nick}",
    "PlayStation": "https://psnprofiles.com/{nick}",
    "Nintendo": "https://my.nintendo.com/profile/{nick}",
    "Coroflot": "https://coroflot.com/{nick}",
    "Freelance.ru": "https://freelance.ru/{nick}",
    "Toptal": "https://toptal.com/resume/{nick}",
    "Guru": "https://guru.com/freelancers/{nick}",
    "PeoplePerHour": "https://peopleperhour.com/freelancer/{nick}",
    "ModelMayhem": "https://modelmayhem.com/{nick}",
    "FolioHD": "https://{nick}.foliohd.com",
    "Dribbble Portfolios": "https://dribbble.com/{nick}/portfolio",
    "Cargo": "https://{nick}.cargo.site",
    "Portfolium": "https://portfolium.com/{nick}",
    "Authorea": "https://authorea.com/users/{nick}",
    "ResearchGate": "https://researchgate.net/profile/{nick}",
    "Academia.edu": "https://{nick}.academia.edu",
    "Overleaf": "https://overleaf.com/{nick}",
    "Figshare": "https://figshare.com/authors/{nick}",
    "Mendeley": "https://mendeley.com/profiles/{nick}",
    "Zotero": "https://zotero.org/{nick}",
    "Codeforces": "https://codeforces.com/profile/{nick}",
    "AtCoder": "https://atcoder.jp/users/{nick}",
    "TopHacker": "https://tophacker.com/users/{nick}",
    "Sublime": "https://sublime.com/users/{nick}",
    "HackTheBox": "https://hackthebox.com/profile/{nick}",
    "TryHackMe": "https://tryhackme.com/p/{nick}",
    "OverTheWire": "https://overthewire.org/profile/{nick}",
    "CSES": "https://cses.fi/user/{nick}",
    "CodeChef": "https://codechef.com/users/{nick}",
    "Spoj": "https://spoj.com/users/{nick}",
    "ProjectEuler": "https://projecteuler.net/profile/{nick}",
    "Exercism": "https://exercism.org/profiles/{nick}",
    "FreeCodeCamp": "https://freecodecamp.org/{nick}",
    "Replit": "https://replit.com/@{nick}",
    "Glitch": "https://{nick}.glitch.me",
    "CodeSandbox": "https://codesandbox.io/u/{nick}",
    "JSFiddle": "https://jsfiddle.net/user/{nick}",
    "StackBlitz": "https://stackblitz.com/@{nick}",
    "LiveJournal": "https://{nick}.livejournal.com",
    "Dreamwidth": "https://{nick}.dreamwidth.org",
    "Blogger": "https://{nick}.blogspot.com",
    "WordPress": "https://{nick}.wordpress.com",
    "Wix": "https://{nick}.wixsite.com",
    "Squarespace": "https://{nick}.squarespace.com",
    "Weebly": "https://{nick}.weebly.com",
    "Ghost": "https://{nick}.ghost.io",
    "Notion": "https://{nick}.notion.site",
    "Evernote": "https://evernote.com/{nick}",
    "Pocket": "https://getpocket.com/@{nick}",
    "Diigo": "https://diigo.com/profile/{nick}",
    "Instapaper": "https://instapaper.com/u/{nick}",
    "Raindrop": "https://raindrop.io/{nick}",
    "Pinboard": "https://pinboard.in/u:{nick}",
    "Digg": "https://digg.com/@{nick}",
    "StumbleUpon": "https://stumbleupon.com/stumbler/{nick}",
    "Flipboard": "https://flipboard.com/@{nick}",
    "Feedly": "https://feedly.com/i/subscription/feed/{nick}",
    "Zotero Groups": "https://zotero.org/groups/{nick}",
    "Goodreads Groups": "https://goodreads.com/user/show/{nick}",
    "LibraryThing": "https://librarything.com/profile/{nick}",
    "BookCrossing": "https://bookcrossing.com/mybookshelf/{nick}",
    "Anobii": "https://anobii.com/{nick}/profile",
    "Shelfari": "https://shelfari.com/{nick}",
    "Discogs": "https://discogs.com/user/{nick}",
    "RateYourMusic": "https://rateyourmusic.com/~{nick}",
    "Mixlr": "https://mixlr.com/{nick}",
    "Soundtrap": "https://soundtrap.com/{nick}",
    "Audiomack": "https://audiomack.com/{nick}",
    "Reverb": "https://reverb.com/shop/{nick}",
    "BandLab": "https://bandlab.com/{nick}",
    "Splice": "https://splice.com/{nick}",
    "Kompoz": "https://kompoz.com/music/artist/{nick}",
    "Vampr": "https://vampr.me/{nick}",
    "Songkick": "https://songkick.com/users/{nick}",
    "Setlist.fm": "https://setlist.fm/user/{nick}",
    "ResidentAdvisor": "https://ra.co/dj/{nick}",
    "Beatport": "https://beatport.com/artist/{nick}",
    "Mixmag": "https://mixmag.net/dj/{nick}",
    "BoilerRoom": "https://boilerroom.tv/artist/{nick}",
    "SoundBetter": "https://soundbetter.com/profiles/{nick}",
    "Freesound": "https://freesound.org/people/{nick}",
    "Musixmatch": "https://musixmatch.com/profile/{nick}",
    "Genius": "https://genius.com/{nick}",
    "WhoSampled": "https://whosampled.com/user/{nick}",
    "Vocal": "https://vocal.media/authors/{nick}",
    "Steemit": "https://steemit.com/@{nick}",
    "Hive": "https://hive.blog/@{nick}",
    "PeakD": "https://peakd.com/@{nick}",
    "Busy": "https://busy.org/@{nick}",
    "Voice": "https://voice.com/u/{nick}",
    "LBRY": "https://lbry.tv/@{nick}",
    "Odysee": "https://odysee.com/@{nick}",
    "BitChute": "https://bitchute.com/channel/{nick}",
    "Rumble": "https://rumble.com/c/{nick}",
    "Locals": "https://{nick}.locals.com",
    "Gettr": "https://gettr.com/user/{nick}",
    "TruthSocial": "https://truthsocial.com/@{nick}",
    "MeWe": "https://mewe.com/i/{nick}",
    "Clouthub": "https://clouthub.com/{nick}",
    "Nextdoor": "https://nextdoor.com/profile/{nick}",
    "Yubo": "https://yubo.live/en/profile/{nick}",
    "Houseparty": "https://houseparty.com/user/{nick}",
    "Vero": "https://vero.co/{nick}",
    "Peach": "https://peachapp.com/{nick}",
    "Ello Creators": "https://ello.co/{nick}/creators",
    "Artfol": "https://artfol.co/{nick}",
    "PixelFed": "https://pixelfed.social/{nick}",
    "Plurk": "https://plurk.com/{nick}",
    "Tagged": "https://tagged.com/{nick}",
    "Hi5": "https://hi5.com/{nick}",
    "MeetMe": "https://meetme.com/{nick}",
    "Twoo": "https://twoo.com/{nick}",
    "BlackPlanet": "https://blackplanet.com/{nick}",
    "Migme": "https://migme.com/{nick}",
    "Skyrock": "https://skyrock.com/{nick}",
    "Cyworld": "https://cyworld.com/{nick}",
    "Bebo": "https://bebo.com/{nick}",
    "Orkut": "https://orkut.com/{nick}",
    "Friendster": "https://friendster.com/{nick}",
    "Classmates": "https://classmates.com/user/profile/{nick}",
    "Reunion": "https://reunion.com/{nick}",
    "MyHeritage": "https://myheritage.com/{nick}",
    "Ancestry": "https://ancestry.com/profile/{nick}",
    "Geni": "https://geni.com/people/{nick}",
    "FamilySearch": "https://familysearch.org/profile/{nick}",
    "23andMe": "https://23andme.com/user/{nick}",
    "MyLife": "https://mylife.com/{nick}",
    "Spokeo": "https://spokeo.com/{nick}",
    "Whitepages": "https://whitepages.com/name/{nick}",
    "Zillow": "https://zillow.com/profile/{nick}",
    "Redfin": "https://redfin.com/profile/{nick}",
    "Airbnb": "https://airbnb.com/users/show/{nick}",
    "Vrbo": "https://vrbo.com/traveler/{nick}",
    "Booking": "https://booking.com/profile/{nick}",
    "Expedia": "https://expedia.com/user/{nick}",
    "Kayak": "https://kayak.com/profile/{nick}",
    "Orbitz": "https://orbitz.com/user/{nick}",
    "Travelocity": "https://travelocity.com/user/{nick}",
    "TripIt": "https://tripit.com/people/{nick}",
    "Wanderu": "https://wanderu.com/en-us/profile/{nick}",
    "Roadtrippers": "https://roadtrippers.com/users/{nick}",
    "NomadList": "https://nomadlist.com/@{nick}",
    "Couchsurfing Groups": "https://couchsurfing.com/groups/{nick}",
    "Warmshowers": "https://warmshowers.org/user/{nick}",
    "Helpx": "https://helpx.net/profile/{nick}",
    "Workaway": "https://workaway.info/en/host/{nick}",
    "WWOOF": "https://wwoof.net/profile/{nick}",
    "TrustedHousesitters": "https://trustedhousesitters.com/profile/{nick}",
    "MindMyHouse": "https://mindmyhouse.com/sitters/{nick}",
    "HouseCarers": "https://housecarers.com/sitter/{nick}",
    "Nomador": "https://nomador.com/profile/{nick}",
    "PetSitter": "https://petsitter.com/{nick}",
    "Rover": "https://rover.com/members/{nick}",
    "DogVacay": "https://dogvacay.com/{nick}",
    "Care": "https://care.com/{nick}",
    "Sittercity": "https://sittercity.com/profile/{nick}",
    "UrbanSitter": "https://urbansitter.com/{nick}",
    "TaskRabbit": "https://taskrabbit.com/profile/{nick}",
    "Thumbtack": "https://thumbtack.com/profile/{nick}",
    "Handy": "https://handy.com/pro/{nick}",
    "Angi": "https://angi.com/profile/{nick}",
    "HomeAdvisor": "https://homeadvisor.com/sp/{nick}",
    "Yelp": "https://yelp.com/user_details?userid={nick}",
    "YellowPages": "https://yellowpages.com/profile/{nick}",
    "Foursquare": "https://foursquare.com/user/{nick}",
    "Swarm": "https://swarmapp.com/{nick}",
    "Untappd Breweries": "https://untappd.com/brewery/{nick}",
    "BeerAdvocate": "https://beeradvocate.com/user/profile/{nick}",
    "RateBeer": "https://ratebeer.com/user/{nick}",
    "HomebrewTalk": "https://homebrewtalk.com/members/{nick}",
    "Brewtoad": "https://brewtoad.com/users/{nick}",
    "BrewersFriend": "https://brewersfriend.com/homebrew/brewer/{nick}",
    "GoodFood": "https://goodfood.com.au/user/{nick}",
    "Yummly": "https://yummly.com/profile/{nick}",
    "Allrecipes": "https://allrecipes.com/cook/{nick}",
    "Epicurious": "https://epicurious.com/user/{nick}",
    "Food52": "https://food52.com/users/{nick}",
    "SeriousEats": "https://seriouseats.com/user/profile/{nick}",
    "Tastemade": "https://tastemade.com/@{nick}",
    "Cookpad": "https://cookpad.com/us/users/{nick}",
    "MyFitnessPal": "https://myfitnesspal.com/profile/{nick}",
    "Fitbit": "https://fitbit.com/user/{nick}",
    "GarminConnect": "https://connect.garmin.com/profile/{nick}",
    "MapMyRun": "https://mapmyrun.com/profile/{nick}",
    "Runkeeper": "https://runkeeper.com/user/{nick}",
    "Peloton": "https://members.onepeloton.com/members/{nick}",
    "Zwift": "https://zwift.com/athlete/{nick}",
    "RideWithGPS": "https://ridewithgps.com/users/{nick}",
    "Komoot": "https://komoot.com/user/{nick}",
    "AllTrails": "https://alltrails.com/members/{nick}",
    "HikingProject": "https://hikingproject.com/user/{nick}",
    "TrailRunProject": "https://trailrunproject.com/user/{nick}",
    "MTBProject": "https://mtbproject.com/user/{nick}",
    "ClimbingProject": "https://climbingproject.com/user/{nick}",
    "CycleWorks": "https://cycleworks.com/profile/{nick}",
    "TrainerRoad": "https://trainerroad.com/profile/{nick}",
    "TrainingPeaks": "https://trainingpeaks.com/athlete/{nick}",
    "Athlinks": "https://athlinks.com/athlete/{nick}",
    "SportTracks": "https://sporttracks.mobi/user/{nick}",
    "Endomondo": "https://endomondo.com/profile/{nick}",
    "PolarFlow": "https://flow.polar.com/profile/{nick}",
    "Suunto": "https://suunto.com/mysuunto/{nick}",
    "Coros": "https://coros.com/profile/{nick}",
    "GaiaGPS": "https://gaiagps.com/profile/{nick}",
    "ViewRanger": "https://viewranger.com/user/{nick}",
    "OutdoorActive": "https://outdooractive.com/en/member/{nick}",
    "Wikiloc": "https://wikiloc.com/wikiloc/user.do?id={nick}",
    "Geocaching": "https://geocaching.com/p/{nick}",
    "Letterboxing": "https://letterboxing.org/members/{nick}",
    "Munzee": "https://munzee.com/m/{nick}",
    "Opencaching": "https://opencaching.com/{nick}",
    "AtlasQuest": "https://atlasquest.com/members/{nick}",
    "Waymarking": "https://waymarking.com/users/{nick}",
    "Groundspeak": "https://groundspeak.com/profile/{nick}",
    "AdventureLab": "https://labs.geocaching.com/profile/{nick}",
    "Strava Segments": "https://strava.com/segments/{nick}",
    "Fitocracy": "https://fitocracy.com/profile/{nick}",
    "Hevy": "https://hevyapp.com/user/{nick}",
    "Strong": "https://strong.app/profile/{nick}",
    "Jefit": "https://jefit.com/{nick}",
    "Bodybuilding.com": "https://bodybuilding.com/profiles/{nick}",
    "MuscleWiki": "https://musclewiki.com/user/{nick}",
    "FitNotes": "https://fitnotes.app/user/{nick}",
    "FitDay": "https://fitday.com/fitness/profile/{nick}",
    "Cronometer": "https://cronometer.com/profile/{nick}",
    "LoseIt": "https://loseit.com/profile/{nick}",
    "Noom": "https://noom.com/profile/{nick}",
    "WeightWatchers": "https://weightwatchers.com/profile/{nick}",
    "MyPlate": "https://myplate.gov/profile/{nick}",
    "Lifesum": "https://lifesum.com/profile/{nick}",
    "Yazio": "https://yazio.com/profile/{nick}",
    "Healthi": "https://healthiapp.com/profile/{nick}",
    "SparkPeople": "https://sparkpeople.com/myspark/members/{nick}",
    "FatSecret": "https://fatsecret.com/member/{nick}",
    "CalorieKing": "https://calorieking.com/profile/{nick}",
    "Nutritionix": "https://nutritionix.com/profile/{nick}",
    "DietDoctor": "https://dietdoctor.com/profile/{nick}",
    "KetoConnect": "https://ketoconnect.net/user/{nick}",
    "CarbManager": "https://carbmanager.com/profile/{nick}",
    "Atkins": "https://atkins.com/profile/{nick}",
    "PaleoLeap": "https://paleoleap.com/profile/{nick}",
    "Whole30": "https://whole30.com/profile/{nick}",
    "FitMenCook": "https://fitmencook.com/profile/{nick}",
    "BudgetBytes": "https://budgetbytes.com/author/{nick}",
    "MinimalistBaker": "https://minimalistbaker.com/author/{nick}",
    "SmittenKitchen": "https://smittenkitchen.com/author/{nick}",
    "PinchOfYum": "https://pinchofyum.com/author/{nick}",
    "HalfBakedHarvest": "https://halfbakedharvest.com/author/{nick}",
    "AmbitiousKitchen": "https://ambitiouskitchen.com/author/{nick}",
    "LoveAndLemons": "https://loveandlemons.com/author/{nick}",
    "CookieAndKate": "https://cookieandkate.com/author/{nick}",
    "OhSheGlows": "https://ohsheglows.com/author/{nick}",
    "TheKitchn": "https://thekitchn.com/author/{nick}",
    "BonAppetit": "https://bonappetit.com/people/{nick}",
    "Epicurious Recipes": "https://epicurious.com/recipes/member/{nick}",
    "Tasty": "https://tasty.co/user/{nick}",
    "BingingWithBabish": "https://bingingwithbabish.com/user/{nick}",
    "JoshuaWeissman": "https://joshuaweissman.com/user/{nick}",
    "SortedFood": "https://sortedfood.com/user/{nick}",
    "FoodWishes": "https://foodwishes.com/user/{nick}",
    "SeriousEats Recipes": "https://seriouseats.com/recipes/{nick}",
    "ChefSteps": "https://chefsteps.com/profile/{nick}",
    "CookingLight": "https://cookinglight.com/profile/{nick}",
    "EatingWell": "https://eatingwell.com/profile/{nick}",
    "Delish": "https://delish.com/profile/{nick}",
    "FoodNetwork": "https://foodnetwork.com/profiles/{nick}",
    "TasteOfHome": "https://tasteofhome.com/member/{nick}",
    "SimplyRecipes": "https://simplyrecipes.com/author/{nick}",
    "JoyOfBaking": "https://joyofbaking.com/author/{nick}",
    "SallysBakingAddiction": "https://sallysbakingaddiction.com/author/{nick}",
    "KingArthurBaking": "https://kingarthurbaking.com/author/{nick}",
    "BakersBanquet": "https://bakersbanquet.com/author/{nick}",
    "ThePioneerWoman": "https://thepioneerwoman.com/author/{nick}",
    "Skinnytaste": "https://skinnytaste.com/author/{nick}",
    "Downshiftology": "https://downshiftology.com/author/{nick}",
    "GimmeSomeOven": "https://gimmesomeoven.com/author/{nick}",
    "ClosetCooking": "https://closetcooking.com/author/{nick}",
    "DamnDelicious": "https://damndelicious.net/author/{nick}",
    "CafeDelites": "https://cafedelites.com/author/{nick}",
    "TheRecipeCritic": "https://therecipecritic.com/author/{nick}",
    "SpendWithPennies": "https://spendwithpennies.com/author/{nick}",
    "WellPlated": "https://wellplated.com/author/{nick}",
    "InspiredTaste": "https://inspiredtaste.net/author/{nick}",
    "SpruceEats": "https://thespruceeats.com/author/{nick}",
    "MyRecipes": "https://myrecipes.com/author/{nick}",
    "SouthernLiving": "https://southernliving.com/author/{nick}",
    "BetterHomesGardens": "https://bhg.com/author/{nick}",
    "MarthaStewart": "https://marthastewart.com/author/{nick}",
    "RealSimple": "https://realsimple.com/author/{nick}",
    "GoodHousekeeping": "https://goodhousekeeping.com/author/{nick}",
    "CountryLiving": "https://countryliving.com/author/{nick}",
    "HouseBeautiful": "https://housebeautiful.com/author/{nick}",
    "ElleDecor": "https://elledecor.com/author/{nick}",
    "ArchitecturalDigest": "https://architecturaldigest.com/author/{nick}",
    "Dwell": "https://dwell.com/author/{nick}",
    "ApartmentTherapy": "https://apartmenttherapy.com/author/{nick}",
    "DesignMilk": "https://designmilk.com/author/{nick}",
    "Core77": "https://core77.com/users/{nick}",
    "YankoDesign": "https://yankodesign.com/author/{nick}",
    "Dezeen": "https://dezeen.com/author/{nick}",
    "ArchDaily": "https://archdaily.com/author/{nick}",
    "Inhabitat": "https://inhabitat.com/author/{nick}",
    "Treehugger": "https://treehugger.com/author/{nick}",
    "EcoWatch": "https://ecowatch.com/author/{nick}",
    "MotherEarthNews": "https://motherearthnews.com/author/{nick}",
    "ModernFarmer": "https://modernfarmer.com/author/{nick}",
    "UrbanFarm": "https://urbanfarm.org/author/{nick}",
    "Gardenista": "https://gardenista.com/author/{nick}",
    "TheSpruce": "https://thespruce.com/author/{nick}",
    "FineGardening": "https://finegardening.com/author/{nick}",
    "GardenersWorld": "https://gardenersworld.com/user/{nick}",
    "Horticulture": "https://hortmag.com/author/{nick}",
    "GrowVeg": "https://growveg.com/profile/{nick}",
    "Burpee": "https://burpee.com/gardener/{nick}",
    "SeedSavers": "https://seedsavers.org/profile/{nick}",
    "JohnnySeeds": "https://johnnyseeds.com/gardener/{nick}",
    "TerritorialSeed": "https://territorialseed.com/profile/{nick}",
    "BotanicalInterests": "https://botanicalinterests.com/profile/{nick}",
    "HighMowingSeeds": "https://highmowingseeds.com/profile/{nick}",
    "BakerCreekSeeds": "https://rareseeds.com/profile/{nick}",
    "EdenBrothers": "https://edenbrothers.com/profile/{nick}",
    "GrowOrganic": "https://groworganic.com/profile/{nick}",
    "SustainableSeed": "https://sustainableseedco.com/profile/{nick}",
    "HeirloomSeeds": "https://heirloomseeds.com/profile/{nick}",
    "SeedSaversExchange": "https://seedsaversexchange.org/profile/{nick}",
    "VictorySeeds": "https://victoryseeds.com/profile/{nick}",
    "TrueLeafMarket": "https://trueleafmarket.com/profile/{nick}",
    "UrbanGardener": "https://urbangardener.com/profile/{nick}",
    "Permies": "https://permies.com/u/{nick}",
    "HomesteadingToday": "https://homesteadingtoday.com/members/{nick}",
    "BackYardChickens": "https://backyardchickens.com/members/{nick}",
    "TheFarmingForum": "https://thefarmingforum.co.uk/index.php?members/{nick}",
    "FarmersWeekly": "https://farmersweekly.co.nz/profile/{nick}",
    "Agriville": "https://agriville.com/members/{nick}",
    "TheCattleSite": "https://thecattlesite.com/community/{nick}",
    "DairyFarmer": "https://dairyfarmer.co.uk/profile/{nick}",
    "PoultryWorld": "https://poultryworld.net/profile/{nick}",
    "PigProgress": "https://pigprogress.net/profile/{nick}",
    "FishFarm": "https://fishfarm.com/profile/{nick}",
    "Aquaculture": "https://aquaculture.com/profile/{nick}",
    "Hydroponics": "https://hydroponics.com/profile/{nick}",
    "Aeroponics": "https://aeroponics.com/profile/{nick}",
    "VerticalFarming": "https://verticalfarming.com/profile/{nick}",
    "UrbanAgNews": "https://urbanagnews.com/profile/{nick}",
    "GrowEasy": "https://groweasy.com/profile/{nick}",
    "GrowersNetwork": "https://growersnetwork.org/members/{nick}",
    "CannabisNow": "https://cannabisnow.com/profile/{nick}",
    "HighTimes": "https://hightimes.com/author/{nick}",
    "Leafly": "https://leafly.com/profile/{nick}",
    "Weedmaps": "https://weedmaps.com/users/{nick}",
    "PotGuide": "https://potguide.com/profile/{nick}",
    "CannaConnection": "https://cannaconnection.com/users/{nick}",
    "GrowWeedEasy": "https://growweedeasy.com/author/{nick}",
    "ILoveGrowingMarijuana": "https://ilovegrowingmarijuana.com/author/{nick}",
    "SeedSupreme": "https://seedsupreme.com/profile/{nick}",
    "Seedsman": "https://seedsman.com/profile/{nick}",
    "CropKingSeeds": "https://cropkingseeds.com/profile/{nick}",
    "MSNL": "https://msnl.com/profile/{nick}",
    "ILGM": "https://ilgm.com/profile/{nick}",
    "TrueNorthSeedBank": "https://truenorthseedbank.com/profile/{nick}",
    "HempDepot": "https://hempdepot.com/profile/{nick}",
    "CBDistillery": "https://cbdistillery.com/profile/{nick}",
    "CBDPure": "https://cbdpure.com/profile/{nick}",
    "NuLeafNaturals": "https://nuleafnaturals.com/profile/{nick}",
    "CharlotteWeb": "https://charlottesweb.com/profile/{nick}",
    "Medterra": "https://medterra.com/profile/{nick}",
    "GreenRoads": "https://greenroads.com/profile/{nick}",
    "LazarusNaturals": "https://lazarusnaturals.com/profile/{nick}",
    "JoyOrganics": "https://joyorganics.com/profile/{nick}",
    "CBDfx": "https://cbdfx.com/profile/{nick}",
    "HempBombs": "https://hempbombs.com/profile/{nick}",
    "KoiCBD": "https://koicbd.com/profile/{nick}",
    "DiamondCBD": "https://diamondcbd.com/profile/{nick}",
    "PureKana": "https://purekana.com/profile/{nick}",
    "CBDAmericanShaman": "https://cbdamericanshaman.com/profile/{nick}",
    "JustCBD": "https://justcbdstore.com/profile/{nick}",
    "VapeBright": "https://vapebright.com/profile/{nick}",
    "HempVada": "https://hempvada.com/profile/{nick}",
    "Elixinol": "https://elixinol.com/profile/{nick}",
    "Endoca": "https://endoca.com/profile/{nick}",
    "PharmaHemp": "https://pharmahemp.com/profile/{nick}",
    "CBDLife": "https://cbdlifeuk.com/profile/{nick}",
    "BlessedCBD": "https://blessedcbd.co.uk/profile/{nick}",
    "Provacan": "https://provacan.co.uk/profile/{nick}",
    "Hempura": "https://hempura.shop/profile/{nick}",
    "CBDVapeJuice": "https://cbdvapejuice.net/profile/{nick}",
    "Vapoholic": "https://vapoholic.co.uk/profile/{nick}",
    "VapeUK": "https://vapeuk.co.uk/profile/{nick}",
    "VapeClub": "https://vapeclub.co.uk/profile/{nick}",
    "VapeSuperstore": "https://vapesuperstore.co.uk/profile/{nick}",
    "VapeShop": "https://vapeshop.co.uk/profile/{nick}",
    "VapeWild": "https://vapewild.com/profile/{nick}",
    "VaporDNA": "https://vapordna.com/profile/{nick}",
    "ElementVape": "https://elementvape.com/profile/{nick}",
    "VapeSourcing": "https://vapesourcing.com/profile/{nick}",
    "VapeNW": "https://vapenw.com/profile/{nick}",
    "VaporBeast": "https://vaporbeast.com/profile/{nick}",
    "VapeRoyalty": "https://vaperoyalty.com/profile/{nick}",
    "VapeStreet": "https://vapestreet.com/profile/{nick}",
    "Vaping": "https://vaping.com/profile/{nick}",
    "VapeWorld": "https://vapeworld.com/profile/{nick}",
    "VaporFi": "https://vaporfi.com/profile/{nick}",
    "DirectVapor": "https://directvapor.com/profile/{nick}",
    "EightVape": "https://eightvape.com/profile/{nick}",
    "VapeSourcingUK": "https://vapesourcing.uk/profile/{nick}",
    "VapeBargains": "https://vapebargains.co.uk/profile/{nick}",
    "VapeDeals": "https://vapedeals.com/profile/{nick}",
    "VapeSale": "https://vapesale.com/profile/{nick}",
    "VapeDiscount": "https://vapediscount.com/profile/{nick}",
    "VapeOffers": "https://vapeoffers.com/profile/{nick}",
    "VapePromo": "https://vapepromo.com/profile/{nick}",
    "VapeCodes": "https://vapecodes.com/profile/{nick}",
    "VapeCoupons": "https://vapecoupons.com/profile/{nick}",
    "VapeRewards": "https://vaperewards.com/profile/{nick}",
    "VapeLoyalty": "https://vapeloyalty.com/profile/{nick}",
    "VapePoints": "https://vapepoints.com/profile/{nick}",
    "VapeCashback": "https://vapecashback.com/profile/{nick}",
    "VapeRebates": "https://vaperebates.com/profile/{nick}",
    "VapeSavings": "https://vapesavings.com/profile/{nick}",
    "VapeClearance": "https://vapeclearance.com/profile/{nick}",
    "VapeOutlet": "https://vapeoutlet.co.uk/profile/{nick}",
    "VapeWarehouse": "https://vapewarehouse.com/profile/{nick}",
    "VapeMarket": "https://vapemarket.com/profile/{nick}",
    "VapeShopOnline": "https://vapeshoponline.com/profile/{nick}",
    "VapeEmporium": "https://vapeemporium.com/profile/{nick}",
    "VapeHaven": "https://vapehaven.com/profile/{nick}",
    "VapeZone": "https://vapezone.com/profile/{nick}",
    "VapeCity": "https://vapecity.com/profile/{nick}",
    "VapeTown": "https://vapetown.com/profile/{nick}",
    "VapeVillage": "https://vapevillage.com/profile/{nick}",
    "VapeHub": "https://vapehub.com/profile/{nick}",
    "VapeCentral": "https://vapecentral.com/profile/{nick}"
}

    print(f"\n{Fore.YELLOW}🔍 Поиск аккаунтов для: {nick}{Fore.RESET}\n")

    found = 0
    total = len(sites)
    
    for name, url in sites.items():
        try:
            response = requests.get(url.format(nick=nick), timeout=5, allow_redirects=False)
            if response.status_code == 200 and not any(e in response.url.lower() for e in ["error", "404"]):
                print(f"{Fore.GREEN}[+] {name}: {url.format(nick=nick)}{Fore.RESET}")
                found += 1
            else:
                print(f"{Fore.RED}[-] {name}: Не найдено{Fore.RESET}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[-] {name}: Ошибка проверки ({str(e)}){Fore.RESET}")
            logging.error(f"Ошибка при проверке {name} ({url.format(nick=nick)}): {str(e)}")
        time.sleep(0.5)  
    
    print(f"\n{Fore.YELLOW} Результаты{Fore.RESET}")
    print(f"{Fore.GREEN} Найдено {found} аккаунтов из {total}{Fore.RESET}")
    print(f"{Fore.RED} Не найдено {total - found} аккаунтов{Fore.RESET}")
    print(f"\n{Fore.CYAN} Пояснение{Fore.RESET}")
    print(f"{Fore.GREEN}Зелёный - аккаунт существует{Fore.RESET}")
    print(f"{Fore.RED}Красный - аккаунт не найден{Fore.RESET}")

def main():
    
    while True:
        try:
            clear()
            print_art()
            choice = input("\nВыберите действие: ")

            if choice == "1":
                nick = input("Введите ник: ").strip()
                if nick:
                    check_username(nick)
                    input("\nНажмите Enter чтобы продолжить...")
                else:
                    print(f"{Fore.RED}Ник не может быть пустым!{Fore.RESET}")
                    time.sleep(1)
            elif choice == "2":
                print(f"{Fore.RED}Выход...{Fore.RESET}")
                input("Нажмите Enter для выхода...")
                break
            else:
                print(f"{Fore.RED}Неверный выбор!{Fore.RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Программа остановлена пользователем{Fore.RESET}")
            input("Нажмите Enter для выхода...")
            break
        except Exception as e:
            print(f"{Fore.RED}Произошла ошибка: {str(e)}{Fore.RESET}")
            logging.error(f"Необработанная ошибка: {str(e)}")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{Fore.RED}ошибка: {str(e)}{Fore.RESET}")
        logging.error(f"Критическая ошибка при запуске: {str(e)}")
        input("Нажмите Enter для выхода...")
