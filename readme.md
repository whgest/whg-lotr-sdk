### Intro

Welcome to whg-lotr-sdk. One does not simply call an API. This SDK expedites access and use of 
[The One API](https://the-one-api.dev/) for developers using Python 3.7 or above.

### Installation

whg-lotr-sdk is installable from pip. 

```pip install whg-lotr-sdk```

Or, grab the source code at https://github.com/whgest/whg-lotr-sdk.

To install dependencies, run ```pip install -r requirements.txt``` at the command line in the sdk directory.

### Test

To verify setup was successful, enter ```pytest``` at the command line in your sdk directory to run unit tests if you cloned
the source code, or ```pytest --pyargs lotr_sdk.tests``` if you installed the package from pip.


### Basic Usage

First you must request and receive an API key from The One API. Set it in your environment
as the key ```LOTR_API_KEY```.

Once your key is set, import and instantiate the SDK handler as shown below.

```
from lotr_sdk.sdk import LotrSdk 

sdk = LotrSdk()

```

The SDK handler has several subhandlers to request different types of data. To get a list of all movies, use the ```movies```
property of your instantiated sdk. ```movies``` has two methods: ```get_all``` and ```get_by_id```.

```
result = sdk.movie.get_all()
print(result.movies)
```

The response will have a list of movies as well as metadata concerned with pagination, sorting, and filtering.

Each movie object has several data points, including an id. We can use that id to fetch just that movie object:

```
movie = sdk.movie.get_by_id("5cd95395de30eff6ebccde5d")
print(movie)
```

This will print just the data for *Return of the King*. 

Quotes work the same way:

```
result = sdk.quote.get_all()
print(result.quotes)

movie = sdk.quote.get_by_id("5cd96e05de30eff6ebcce7e9")
print(quote)
```

Quotes has one more feature, though: you can grab all quotes from a movie by using its movie_id.

```
result = sdk.quote.get_by_movie_id('5cd95395de30eff6ebccde5d')
print(result.quotes)
```

This will print only the quotes from *Return of the King*. 


### Pagination, Filtering, Sorting

The ```get_all()``` methods, including ```get_by_movie_id```, support pagination, filtering, and sorting as described in
the The One API documentation [here](https://the-one-api.dev/documentation).

```
result = sdk.quote.get_all_by_movie_id('5cd95395de30eff6ebccde5d', limit=5, page=2)
print(result.quotes)
```

From this call we get quotes 5-10 from *Return of the King*. 