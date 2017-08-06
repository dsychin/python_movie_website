import media
import fresh_tomatoes

# List of movies
# Movie information from https://www.themoviedb.org
# Trailers from Youtube
scandal = media.Movie(
    "SCANDAL Documentary film HELLO WORLD",
    "https://image.tmdb.org/t/p/original/x3mFN0unqhlVO2NoHL5zm05DRZK.jpg",
    "https://www.youtube.com/watch?v=uroSQHVX0ks",
    "The first documentary film of Japanese female rock band SCANDAL will \
    receive a UK and European DVD release this February through JPU Records. \
    The film captures the highly successful four-piece as they travel \
    overseas on their first solo world tour.")
i_am_a_hero = media.Movie(
    "I Am A Hero",
    "https://image.tmdb.org/t/p/w640/4RnmHtCLtbBHD9jagVlcSzJTWX6.jpg",
    "https://www.youtube.com/watch?v=sZu3sVK3JOE",
    "Hideo Suzuki is a 35-year-old mangaka assistant, whose life seem to be \
    stuck around his exhausting but low-paying job, unfulfilled dreams, \
    strange hallucinations and unsatisfying relationships. He sees himself \
    as a supporting character in his own life, has low self-esteem, resulting \
    in frustration. One day, the world as Hideo knows it is shattered by the \
    presence of a disease that turns people into homicidal maniacs, whose \
    first instinct is to attack and devour the nearest human.")
chihayafuru = media.Movie(
    "Chihayafuru",
    "https://image.tmdb.org/t/p/w640/jC5Dp2U5IjmjVXO7GbTNn9G8j9J.jpg",
    "https://www.youtube.com/watch?v=nANfoAIMWdc",
    "When Chihaya Ayase was in the 6th grade of elementary school, she met \
    Arata Wataya. Arata Wataya transferred from Fukui Prefecture. Taichi \
    Mashima was Chihaya Ayase's friend since they were little. Arata got \
    close to Chihaya and Taichi from the card game karuta. Four years later, \
    Chihaya is a high school student. Chihaya learns that Arata, who went \
    back to Fukui Prefecture, doesn't play karuta anymore. Believing they \
    will meet Arata again, Chihaya and Taichi starts a karuta club at their \
    high school.")
your_name = media.Movie(
    "Your Name.",
    "https://image.tmdb.org/t/p/w640/xq1Ugd62d23K2knRUx6xxuALTZB.jpg",
    "https://www.youtube.com/watch?v=xU47nhruN-Q",
    "High schoolers Mitsuha and Taki are complete strangers living separate \
    lives. But one night, they suddenly switch places. Mitsuha wakes up in \
    Taki's body, and he in hers. This bizarre occurrence continues to happen \
    randomly, and the two must adjust their lives around each other.")
the_martian = media.Movie(
    "The Martian",
    "https://image.tmdb.org/t/p/w640/5aGhaIHYuQbqlHWvWYqMCnj40y2.jpg",
    "https://www.youtube.com/watch?v=Ue4PCI0NamI",
    "During a manned mission to Mars, Astronaut Mark Watney is presumed dead \
    after a fierce storm and left behind by his crew. But Watney has survived \
    and finds himself stranded and alone on the hostile planet. With only \
    meager supplies, he must draw upon his ingenuity, wit and spirit to \
    subsist and find a way to signal to Earth that he is alive.")
whiplash = media.Movie(
    "Whiplash",
    "https://image.tmdb.org/t/p/w640/lIv1QinFqz4dlp5U4lQ6HaiskOZ.jpg",
    "https://www.youtube.com/watch?v=Df1xkYYbYrY",
    "Under the direction of a ruthless instructor, a talented young drummer \
    begins to pursue perfection at any cost, even his humanity.")

# Add movies to an array
movies = [scandal, i_am_a_hero, chihayafuru, your_name, the_martian, whiplash]
# Pass list of movies to fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
