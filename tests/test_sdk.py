from tests.mock_data import *
import lotr_sdk


def mock_get(*args, **kwargs):
    return kwargs["mock_data"]


def test_get_all_movies():
    sdk = lotr_sdk.LotrSdk()
    sdk.movie._get = mock_get_all_movies
    resp = sdk.movie.get_all()
    assert len(resp.movies) == 5
    assert resp.movies[0].academyAwardNominations


def test_get_movie():
    sdk = lotr_sdk.LotrSdk()
    sdk.movie._get = mock_get_movie
    resp = sdk.movie.get_by_id("5cd95395de30eff6ebccde5d")
    assert resp._id
    assert resp.academyAwardNominations


def test_get_all_quotes():
    sdk = lotr_sdk.LotrSdk()
    sdk.movie._get = mock_get_all_quotes()
    resp = sdk.quote.get_all()
    assert len(resp.quotes) == 1000
    assert resp.quotes[0].dialog


def test_get_quote():
    sdk = lotr_sdk.LotrSdk()
    sdk.movie._get = mock_get_quote
    resp = sdk.quote.get_by_id("5cd96e05de30eff6ebcce7e9")
    assert resp._id
    assert resp.dialog


def test_get_all_quotes_by_movie():
    sdk = lotr_sdk.LotrSdk()
    sdk.movie._get = mock_get_quotes_by_movie()
    resp = sdk.quote.get_by_movie_id("5cd95395de30eff6ebccde5d")
    assert len(resp.quotes) == 872
    assert resp.quotes[0].dialog
