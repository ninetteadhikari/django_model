import React, { Component } from 'react';

export default class MovieList extends Component {
  render() {
    let selectedMovie = this.props.movieList.filter(data => {
      return (
        data.original_title.toLowerCase() === this.props.userInput.toLowerCase()
      );
    });
    let select = selectedMovie[0];

    return (
      <>
        {console.log('selected movie', selectedMovie)}
        {console.log('selected movie2', select)}

        {selectedMovie.map(movie => {
          return (
            <div key={movie.id}>
              <img src={`http://image.tmdb.org/t/p/w185${movie.poster_path}`} alt='movie poster' />
              <h1>{movie.original_title}</h1>
              <p>Rating {movie.vote_average}</p>
            </div>
          );
        })}
      </>
    );
  }
}
