$(function () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const listMovies = $('#list_movies');
    $.get(url, function (data, status) {
      const results = data['results'];
      $.each(results, function (i, result) {
        listMovies.append('<li>' + result['title'] + '</li>');
      });
    });
  });