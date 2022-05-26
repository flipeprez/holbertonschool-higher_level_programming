$(function () {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    $.get(url, function (data, textStatus) {
      var name = data['name'];
      $('#character').append(name);
    });
  });