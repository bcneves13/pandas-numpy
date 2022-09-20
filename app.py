from actions.rating_value import rating_value
def main():
    rating_value('News', 'rating_count_tot', 'news', 1)
    rating_value(['Music','Book'], 'rating_count_tot', 'music_book', 10)

if __name__ == "__main__":
    main()