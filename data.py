from AnilistPython import Anilist

class AnimeSearch():
    def __init__(self):
        self.anilist = Anilist()

    def anime_search(self, input_by_user):
        anime = self.anilist.get_anime(input_by_user)

        anime_image = anime["cover_image"]
        anime_name = anime["name_english"]
        anime_description = anime["desc"]
        anime_description = anime_description.replace("<br>", "")
        anime_description = anime_description.replace("<i>", '"')
        anime_description = anime_description.replace("</i>", '"')
        new_anime_description = anime_description.replace("<b>", '"')

        anime_status = anime["airing_status"]
        anime_airing_span = f"{anime['starting_time']} - {anime['ending_time']}"
        anime_format = anime["airing_format"]
        anime_episodes = anime["airing_episodes"]
        anime_genres = anime["genres"]
        anime_season = anime["season"]

        anime_full_info = f'''Name: {anime_name}\n\nEpisodes: {anime_episodes}\n\nAiring: {anime_airing_span}\n\nFormat: {anime_format}\n\nStatus: {anime_status}\n\nSeason Aired: {anime_season}\n\nGenres: {anime_genres}\n\nSynopsis:\n{new_anime_description}'''
        return anime_full_info

# anime_input = input("Enter the name of the anime: ")
# print("\n")
# anime_search(anime_input)

# manga = anilist.get_manga_with_id(113399)
# # manga_title = (manga["name_english"])
# print(manga)