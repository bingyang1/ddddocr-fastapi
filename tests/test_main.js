const axios = require('axios');
const fs = require('fs');
const FormData = require('form-data');

const url = 'http://192.168.31.30:9898/ocr';
const imagePath = 'H5jW2j.png';

const imageBuffer = fs.readFileSync(imagePath);
const base64Image = imageBuffer.toString('base64');

const formData = new FormData();
formData.append('image', base64Image);
formData.append('probability', 'false');
formData.append('png_fix', 'false');

axios.post(url, formData)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });