$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  data.results.forEach(movie => {
    const item = $('<li></li>').text(movie.title);
    $('UL#list_movies').append(item);
  });
});
