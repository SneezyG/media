from faker import Faker

faker = Faker()

def generate_movie():
    name = faker.sentence(nb_words=4)
    protagonists = faker.paragraph()
    poster = faker.url()
    trailer = faker.url()
    start_date = faker.date_this_decade().strftime('%Y-%m-%d')
    status = "coming_up"
    ranking = 0
    return {
        "name": name,
        "protagonists": protagonists,
        "poster": poster,
        "trailer": trailer,
        "start_date": start_date,
        "status": status,
        "ranking": ranking
    }









