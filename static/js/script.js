  $(document)
    .ready(function() {

      $('.main').visibility({
        type: 'fixed',
        offset: 0
      });
      // create sidebar and attach to menu open
      $('.ui.sidebar')
        .sidebar('attach events', '.toc.item')
      ;
      $('.main.mymenu.menu  .ui.dropdown').dropdown({
        on: 'hover'
      });
    });
    
    $('.ui.rating')
  .rating({
    initialRating: 3,
    maxRating: 5
  })
 ;
  $('.ui.accordion').accordion('refresh');


    $('.ui.dropdown').dropdown();
             /* Back to top fade */
    $(window).scroll(function (event) {
        var scroll = $(window).scrollTop();
        $('#toTop').hide();
        if (scroll > 300) {
            $('#toTop').show();
        } else {
            $('#toTop').hide();
        }

    })
  ;