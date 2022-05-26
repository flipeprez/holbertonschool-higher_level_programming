$(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    $.get(url, function () {
      const trans = ['hello'];
      $('#hello').text(trans);
    });
  }); 

  $(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    const hellores = $('div#hello');
  
    function gethello () {
      return $.get({
        url: url,
        dataType: 'json'
      });
    }
  
    gethello().then((res) => {
      hellores.text(res.hello);
    });
  });