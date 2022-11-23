'use strict';
$(() => {
  const translateHello = () => {
    const BASE_URL = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();
    $.get(`${BASE_URL}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').keydown((ev) => {
    if (ev.key === 'Enter') translateHello();
  });
});