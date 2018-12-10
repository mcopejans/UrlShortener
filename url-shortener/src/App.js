import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class Reservation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        short_url:"",
        long_url:"",
        custom_url:""
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    if (target.name === "short_url") {
        this.state.short_url = target.value
    } else if (target.name === "custom_url") {
        this.state.custom_url = target.value
    } else {
        this.state.long_url = target.value
    }
  }

  handleSubmit(event) {
    if (this.state.short_url !== '' && this.state.long_url !== '') {
        alert("Please provide only one of both: short url or long url");
    }

    if (this.state.short_url === '' && this.state.long_url === '') {
        alert("Please provide at least one of both: short url or long url");
    }

    if (this.state.short_url !== '') {
        fetch("http://0.0.0.0:3001/enlarge?short_url=" + this.state.short_url)
          .then(res => res.json())
          .then(
            (result) => {
              this.setState({
                response: result
              });
              alert(result)
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            (error) => {
              this.setState({
                error
              });
            }
          )
    }

    if (this.state.long_url !== '') {
            var optional_suffix = '';
        if (this.state.custom_url !== '') {
          optional_suffix = "&custom_url=" + this.state.custom_url
        }
        fetch("http://0.0.0.0:3001/shorten?long_url=" + this.state.long_url + optional_suffix)
          .then(res => res.json())
          .then(
            (result) => {
              this.setState({
                response: result
              });
              alert(result)
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            (error) => {
              this.setState({
                error
              });
            }
          )
    }
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Long URL:
          <input
            name="long_url"
            type="text"
            onChange={this.handleInputChange} />
        </label>
        <label>
          Optional custom URL:
          <input
            name="custom_url"
            type="text"
            onChange={this.handleInputChange} />
        </label>
        <br />
        <label>
          Short URL:
          <input
            name="short_url"
            type="text"
            onChange={this.handleInputChange} />
        </label>
        <br />
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default Reservation;
