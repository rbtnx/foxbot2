import '../css/index.css';

$("input[name='playtime']").TouchSpin({
    min: 10,
    max: 600,
    step: 5, 
    boostat: 20,
    maxboostedstep: 50,
    verticalbuttons: true,
    verticalupclass: 'fas fa-angle-up fa-lg',
    verticaldownclass: 'fas fa-angle-down fa-lg',
    postfix: 'minutes'
  })

  $("input[name='playnum']").TouchSpin({
    min: 2,
    max: 7,
    boostat: 4,
    verticalbuttons: true,
    verticalupclass: 'fas fa-angle-up fa-lg',
    verticaldownclass: 'fas fa-angle-down fa-lg',
    postfix: 'players'
  });