def method_caps():
    name = "thaamarai kannan"
    caps = name.capitalize()
    print(name)
    print(caps)
    return

def method_case():
    name = "Thaamarai Kannan SAS"
    # response = name.casefold()
    response = name.lower()
    print(response)
    return

def method_count():
    name = "ThaamaraiKannan SAS"
    para = """
    Bali is predominantly a Hindu country.
    Bali is known for its elaborate, traditional dancing.
    The dancing is inspired by its Hindi beliefs.
    Most of the dancing portrays tales of good versus evil.
    To watch the dancing is a breathtaking experience.
    Lombok has some impressive points of interest – the majestic Gunung Rinjani is an active volcano.
    It is the second highest peak in Indonesia.
    Art is a Balinese passion.
    Batik paintings and carved statues make popular souvenirs.
    Artists can be seen whittling and painting on the streets, particularly in Ubud.
    It is easy to appreciate each island as an attractive tourist destination.
    Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year.
    Snorkelling and diving around the nearby Gili Islands is magnificent.
    Marine fish, starfish, turtles and coral reef are present in abundance.
    Bali and Lombok are part of the Indonesian archipelago.
    Bali has some spectacular temples.
    The most significant is the Mother Temple, Besakih.
    The inhabitants of Lombok are mostly Muslim with a Hindu minority.
    Lombok remains the most understated of the two islands.
    Lombok has several temples worthy of a visit, though they are less prolific.
    Bali and Lombok are neighbouring islands.
    """
    response = para.count("Bali")
    print(response)
    print(type(response))
    return


def method_find():
    para = "Bali is predominantly a Hindu country. Bali is known for its elaborate, traditional dancing. The dancing is inspired by its Hindi beliefs. Most of the dancing portrays tales of good versus evil. To watch the dancing is a breathtaking experience. Lombok has some impressive points of interest - the majestic Gunung Rinjani is an active volcano. It is the second highest peak in Indonesia. Art is a Balinese passion. Batik paintings and carved statues make popular souvenirs. Artists can be seen whittling and painting on the streets, particularly in Ubud. It is easy to appreciate each island as an attractive tourist destination. Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. Snorkelling and diving around the nearby Gili Islands is magnificent. Marine fish, starfish, turtles and coral reef are present in abundance. Bali and Lombok are part of the Indonesian archipelago. Bali has some spectacular temples. The most significant is the Mother Temple, Besakih. The inhabitants of Lombok are mostly Muslim with a Hindu minority. Lombok remains the most understated of the two islands. Lombok has several temples worthy of a visit, though they are less prolific. Bali and Lombok are neighbouring islands."
    response = para.find("majestic")
    print(response)


def method_format():
    var1= "Gokul{}{}{}"
    response = var1.format("K", "age", "20")
    print(response)
    print(response.isalnum())
    return

def method_split():
    data = "apple-banana-orange-watermelon-pineapple"
    res = data.split("-")
    print(res)
    return

def method_replace():
    data = "apple-banana-orange-watermelon-pineapple-banana"
    print(data)
    res = data.replace("banana", "mango")
    print(res)
    return

def method_strip():
    data = "Thaamarai Kannan SAS           "
    print(len(data))
    res = data.strip()
    print(res)
    print(len(res))
    return

method_strip()