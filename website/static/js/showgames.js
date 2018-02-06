var slick = require('slick-carousel')

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/slick.css';


$('.games-carousel').slick({
    lazyLoad: 'ondemand',
    slidesToShow: 3,
    slidesToScroll: 1
});