const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios');
const moment = require('moment');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

const API_KEY = b08hj8493h7764a953c56b7febnh87;

app.post('/weather', (req, res) => {
  const { city } = req.body;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;

  axios.get(url)
    .then(response => {
      const { data } = response;
      const weatherData = {
        city: data.name,
        temperature: data.main.temp,
        humidity: data.main.humidity,
        windSpeed: data.wind.speed,
        description: data.weather[0].description,
        icon: data.weather[0].icon,
        date: moment().format('MMMM Do YYYY, h:mm:ss a')
      };

      res.json(weatherData);
    })
    .catch(error => {
      res.status(404).json({
        message: 'City not found'
      });
    });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
