var slick = require('slick-carousel')
import '../css/slick.css';

$(document).ready(function(){
    $('.games-carousel').slick({
        lazyLoad: 'ondemand',
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1
    });
  });