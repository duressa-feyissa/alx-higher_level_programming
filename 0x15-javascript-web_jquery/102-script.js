'use strict';
$(() => {
  $('INPUT#btn_translate').click(() => {
    const BASE_URL = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();

    $.get(`${BASE_URL}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});