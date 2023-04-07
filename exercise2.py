from classes.People import People

def searchPerson(word:str):
    """found a proffession by given name

    Args:
        word (str): Person's name

    Returns:
        str: found profession
    """
    people  = People()
    return people.search(word)