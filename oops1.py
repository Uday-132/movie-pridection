import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
URLST = {
    "drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=te',
    "action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=te',
    "comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=te',
    "horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=te',
    "crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=te',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=te',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=te',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=te'
}
URLSE={
    "drama":'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=en',
    "action":'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=en',
    "comedy":'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=en',
    "horrer":'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=en',
    "crime":'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=en',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=en',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=en',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=en',
    }
URLSH={
    "drama":'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=hi',
    "action":'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=hi',
    "comedy":'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=hi',
    "horrer":'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=hi',
    "crime":'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=hi',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=hi',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=hi',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=hi',
    }
URLSK={
    "drama":'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=ka',
    "action":'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=ka',
    "comedy":'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=ka',
    "horror":'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=ka',
    "crime":'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=ka',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=ka',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=ka',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=ka',
    }
URLSTA={
    "drama":'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=ta',
    "action":'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=ta',
    "comedy":'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=ta',
    "horror":'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=ta',
    "crime":'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=ta',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=ta',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=ta',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=ta',
    }
URLSM={
    "drama":'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=ml',
    "action":'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=ml',
    "comedy":'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=ml',
    "horror":'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=ml',
    "crime":'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=ml',
    "fantasy":'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&languages=ml',
    "thriller":'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&languages=ml',
    "romance":'https://www.imdb.com/search/title/?title_type=feature&genres=romance&languages=ml',
    }
def main(emotion,language):
    if(language=='english'):
        url = URLSE.get(emotion)
    elif(language=='telugu'):
        url = URLST.get(emotion)
    elif(language=="hindi"):
        url=URLSH.get(emotion)
    elif(language=="tamil"):
        url=URLSTA.get(emotion)
    elif(language=="malayalam"):
        url=URLSM.get(emotion)
    elif(language=="kannada"):
        url=URLSK.get(emotion)
    print(emotion," Movies\n""link ---  ", url)
    if not url:
        print("Invalid emotion.")
        return []
    headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    soup = BeautifulSoup(response.text, "lxml")    
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles
if __name__ == '__main__':
    print("The Emotions are: ")
    print("Drama\nAction\nComedy\nHorrer\nCrime\nFantasy\nThriller\nRomance")
    emotion = input("Enter the emotion: ").strip()
    print("1.Telugu\n2.Hindi\n3.English\n4.Tamil\n5.Kannada\n6.Malayalam")
    language=input("Enter the langusge: ").strip()
    movie_titles = main(emotion,language)
    
    if not movie_titles:
        print("No titles found.... ")
    else:
        max_titles = 40 if emotion in ["Drama", "Action", "Comedy", "Horror", "Crime","fantasy","Thriller","Romance"] else 40
        for title in movie_titles[:max_titles]:
            print(title)
    df=pd.read_csv('data.csv')
    print(df)
    df.plot.bar()
    plt.show() 
